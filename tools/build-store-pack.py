#!/usr/bin/env python3
"""Builds packs/store from the ten industry packs.

The store pack is the "Maho Store" website on the maho/default theme: every product of every
industry, one category tree with one branch per industry, every review, and the home page that
links to the ten industry stores. Run it after any industry pack changes.

The website carries four store views: English, French, German and Italian. The catalog stays in
English, so the pack writes one review row per store view and one set of CMS pages per store view.

Usage: tools/build-store-pack.py
"""
import csv
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'specs'))
import translations  # noqa: E402  the store view copy of every spec, keyed by the English string
PACKS = os.path.join(ROOT, 'packs')
STORE = os.path.join(PACKS, 'store')
WEBSITE = 'base'
STORE_CODE = 'default'
ROOT_CATEGORY = 'Default Category'
# The store views of the Maho Store website, in the order of packs/_shared/stores.csv.
STORE_VIEWS = ['default', 'fr', 'de', 'it']
TABLES = {view: translations.table(view) for view in STORE_VIEWS[1:]}


def read(path):
    with open(path, newline='') as f:
        return list(csv.DictReader(f))


def write(path, rows, columns):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=columns, lineterminator='\n', extrasaction='ignore')
        w.writeheader()
        for row in rows:
            w.writerow({c: row.get(c, '') for c in columns})


def suffix(view):
    """The content file suffix of a store view. The English files keep their plain names."""
    return '' if view == STORE_CODE else '-' + view


def industries():
    """(code, industry name) per industry website, in the sort order of stores.csv."""
    rows = [r for r in read(os.path.join(PACKS, '_shared', 'stores.csv')) if r['website_code'] != WEBSITE]
    rows.sort(key=lambda r: int(r['website_sort_order']))
    return [(r['website_code'], r['root_category']) for r in rows]


MISSING = set()


def say(view, english):
    """The text of a store view. English falls through, and a gap is remembered for the report."""
    if view == STORE_CODE or english == '':
        return english
    value = TABLES[view].get(english)
    if value is None:
        MISSING.add(english)
        return english
    return value


def translated(rows, fields):
    """Each row, followed by one store scoped row per store view that has a translation."""
    out = []
    for row in rows:
        out.append(row)
        for view in STORE_VIEWS[1:]:
            values = {f: say(view, row.get(f, '')) for f in fields}
            if all(values[f] == row.get(f, '') for f in fields):
                continue
            out.append(dict(row, store_code=view, **values))
    return out


def categories(codes):
    rows = [dict(root=ROOT_CATEGORY, path='', name=ROOT_CATEGORY, is_active=1, include_in_menu=1, is_anchor=1,
                 description='Every product of the ten Maho demo stores, on the default theme.')]
    intro = root_descriptions(codes)
    for position, (code, name) in enumerate(codes, 1):
        image = f'store-{code}.webp'
        if not os.path.exists(os.path.join(STORE, 'media', 'catalog', 'category', image)):
            image = ''
        rows.append(dict(root=ROOT_CATEGORY, path=code, name=name, is_active=1, include_in_menu=1, is_anchor=1,
                         position=position, display_mode='PRODUCTS', image=image, description=intro[code]))
        for sub in read(os.path.join(PACKS, code, 'categories.csv')):
            if sub['path'] == '':
                continue
            rows.append(dict(root=ROOT_CATEGORY, path=f"{code}/{sub['path']}", name=sub['name'],
                             is_active=sub['is_active'], include_in_menu=sub['include_in_menu'], is_anchor=sub['is_anchor'],
                             position=sub['position'], display_mode='PRODUCTS', description=sub['description']))
    # A store row only carries the text, so it never creates a category or moves one.
    out = []
    for row in rows:
        out.append(row)
        for view in STORE_VIEWS[1:]:
            name, description = say(view, row['name']), say(view, row.get('description', ''))
            if name == row['name'] and description == row.get('description', ''):
                continue
            out.append(dict(root=row['root'], path=row['path'], store_code=view, name=name, description=description))
    return out


# The eight attributes Maho requires on a default scope row of a file that carries their columns
# (Mage_ImportExport_Model_Import_Entity_Product_Type_Abstract::isRowValid). The anchor row repeats
# them from the industry pack, unchanged.
REQUIRED = ['name', 'price', 'status', 'visibility', 'tax_class_id', 'weight', 'description', 'short_description']
# Rows per product. A store scoped row carries no sku and belongs to the last sku the importer read,
# but _saveProducts forgets that sku at the start of every bunch and drops the row without an error.
# A bunch is exactly 100 rows, so every product must take the same number of rows, and that number
# must divide 100. Five rows do: the anchor, two category slots and one row per translated store view.
ROWS_PER_PRODUCT = 5
CATEGORY_SLOTS = ROWS_PER_PRODUCT - 1 - len(STORE_VIEWS[1:])


def option_labels():
    """English option label to the label of each store view, for the value in a variant name.
    A label that needs no translation, a size or a weight, keeps its English form."""
    out = {}
    for r in read(os.path.join(PACKS, '_shared', 'attribute_options.csv')):
        if r.get('store_code', '') == '':
            out.setdefault(r['label'], {})
        else:
            out.setdefault(r['label_admin'], {})[r['store_code']] = r['label']
    return out


def product_name(view, english, labels, names):
    """A variant is named after its parent plus an option value, so both halves translate."""
    if english in TABLES[view]:
        return TABLES[view][english]
    for label, per_view in labels.items():
        if english.endswith(' ' + label) and english[:-len(label) - 1] in TABLES[view]:
            return TABLES[view][english[:-len(label) - 1]] + ' ' + per_view.get(view, label)
    if english not in names:
        MISSING.add(english)
    return english


def products(codes):
    """Five rows per product: the English anchor, the category slots, then one row per store view."""
    labels = option_labels()
    base_names = set()
    rows = []
    for code, industry in codes:
        order, data, sku = [], {}, None
        for r in read(os.path.join(PACKS, code, 'products.csv')):
            if r['sku'] != '':
                sku = r['sku']
                order.append(sku)
                data[sku] = dict(row=r, cats=[])
            if sku is None or r.get('_store', '') != '':
                continue
            if r['_category'] != '':
                data[sku]['cats'].append(f"{industry}/{r['_category']}")
        for sku in order:
            source, cats = data[sku]['row'], data[sku]['cats']
            anchor = {'sku': sku, '_product_websites': WEBSITE}
            for column in REQUIRED:
                anchor[column] = source[column]
            if cats:
                anchor['_root_category'] = ROOT_CATEGORY
                anchor['_category'] = cats[0]
            rows.append(anchor)
            # The category slots keep the row count even. An empty one carries no scope and is ignored.
            for slot in range(CATEGORY_SLOTS):
                cat = cats[slot + 1] if len(cats) > slot + 1 else ''
                rows.append({'_root_category': ROOT_CATEGORY if cat else '', '_category': cat})
            for view in STORE_VIEWS[1:]:
                description = say(view, source['description'])
                rows.append({'_store': view,
                             'name': product_name(view, source['name'], labels, base_names),
                             'description': description,
                             'short_description': description.split('. ')[0].rstrip('.') + '.'})
    return rows


def reviews(codes):
    """A review belongs to one store view, so every store view of the website gets its own row,
    with its own title and body. Maho has no translated review: it has a review per store."""
    rows = []
    for code, name in codes:
        path = os.path.join(PACKS, code, 'reviews.csv')
        if not os.path.exists(path):
            continue
        for r in read(path):
            for view in STORE_VIEWS:
                row = dict(r)
                row['store_code'] = view
                row['title'] = say(view, r['title'])
                row['detail'] = say(view, r['detail'])
                rows.append(row)
    return rows


SECTIONS = {
    'fashion': ('Dressed for the journey', 'A boutique with a sunlit rail of linen dresses and shirts in natural colours, a straw hat on a hook.', 'Linen that packs flat, denim that breaks in, and the bag to carry it.'),
    'electronics': ('Gear that earns its place', 'A tidy desk by a window with a laptop, headphones on a stand and a small speaker, cool morning light.', 'Nothing on the shelf that we would not keep ourselves.'),
    'food': ('From the farm, to the table', 'A kitchen table with a sourdough loaf, a bottle of olive oil, a wedge of cheese and a bowl of tomatoes.', 'Bread baked at four, oil pressed in November, cheese cut this morning.'),
    'books': ('Read something we would defend', 'A reading corner with an armchair, a stack of clothbound books and a brass lamp, late afternoon light.', 'Novels, guides and cookbooks our staff argue about.'),
    'jewelry': ('Small pieces, made slowly', 'A jeweller\'s bench with a thin gold ring under a loupe, tools and a scrap of velvet, warm light.', 'Rings, chains and studs in recycled gold and silver.'),
    'beauty': ('Short lists, long results', 'A bathroom shelf with frosted glass bottles, a folded linen towel and a sprig of eucalyptus in soft light.', 'Ten ingredients or fewer, in glass you refill.'),
    'home': ('A calm home, made slowly', 'A living room corner with an oak side table, a linen armchair, a wool throw and a paper lamp.', 'Oak, linen and stoneware from workshops we visit.'),
    'sports': ('Gear that keeps up', 'Trail running shoes and a small backpack on a stone step at the start of a mountain path at sunrise.', 'Shoes, layers and tools for the road, the trail and the pool.'),
    'kids': ('Made to be handed down', 'A child\'s room with a wooden stacking tower, a felt rabbit and a low shelf of picture books, morning light.', 'Wooden toys and soft clothes that survive a second child.'),
    'garden': ('Grown here, shipped with care', 'A potting bench with terracotta pots, seedlings in trays, a trowel and gloves, sun through a greenhouse.', 'Plants that arrive upright and tools that come sharp.'),
}
FEATURE_ICONS = ['building-store', 'shopping-cart', 'palette', 'code']
STARS = ' '.join(['{{icon name="star" variant="filled" size="18"}}'] * 5)

# Every string of the store pack pages, per store view. The English entry takes the industry
# intros, the taglines and the customer quotes from the industry packs, so they stay in one place.
# The industry names stay in English, because the catalog stays in English. A string that names
# an industry takes {industry} or {industry_lower}, and a string that names a shop takes {store}.
COPY = {
    'default': {
        'title_home': 'Maho Store',
        'meta_home': 'Ten demo stores on one Maho installation, one per industry theme, and every product in one store.',
        'badge': 'Ten stores, one street',
        'h1': 'Everything from ten shops, in one basket',
        'intro': ('This store carries the full catalog of the ten Maho demo shops. Each shop is also a website of its own, with its own '
                  'theme. Pick one below, or shop it all here.'),
        'choose': 'Choose a store',
        'new': 'New arrivals',
        'hero_alt': 'Ten stores on one street',
        'features': [('One installation', 'Eleven websites, one admin.'),
                     ('Every product', 'The whole catalog, one cart.'),
                     ('Ten themes', 'Each shop has its own look.'),
                     ('Open source', 'Maho is free software.')],
        'h2_stores': 'Ten shops, one street',
        'visit': 'Visit {store}',
        'shop_here': 'Shop {industry_lower} here',
        'picks': '{industry} picks',
        'h2_quotes': 'What our customers say',
        'verified': 'Verified buyer, {store}',
        'h2_news': 'Stay in the loop',
        'p_news': 'One email a month with what is new across the ten stores. No noise.',
        'title_about': 'About the Maho Store',
        'about_alt': 'A row of small shop fronts on a sunny street',
        'about_badge': 'About',
        'about_h2': 'One installation, eleven websites',
        'about_p1': 'The Maho Store is the front door of the Maho sample data. It runs on the default theme and sells the full catalog of the ten demo shops, from linen shirts to trail shoes to terracotta pots.',
        'about_p2': 'Each of the ten shops is also a website of its own on the same installation, with its own theme, categories, content and reviews. Use the store switcher in the corner to jump between them.',
        'about_p3': 'Every product, picture, review and article is generated demo data. Nothing here is for sale, and no order is processed.',
        'title_service': 'Customer Service',
        'svc_h2_ship': 'Shipping and delivery',
        'svc_ship': 'Orders placed before noon on a weekday ship the same day. Standard delivery takes two to four working days. Express delivery arrives the next working day. Plants, food and fragile items travel in their own packaging.',
        'svc_h2_ret': 'Returns',
        'svc_ret': 'You can return an unused item within 30 days of delivery. Start the return from your account page and print the prepaid label. Refunds reach the original payment method within five working days of receipt. Food, plants and personalised jewelry cannot be returned.',
        'svc_h2_pay': 'Payment',
        'svc_pay': 'We accept cards, PayPal and bank transfer. Every payment page is encrypted. We never store card numbers.',
        'svc_h2_contact': 'Contact',
        'svc_contact_pre': 'Write to us through the ',
        'svc_contact_link': 'contact page',
        'svc_contact_post': '. We answer within one working day.',
        'title_404': '404 Not Found',
        'nr_h1': 'Oops!',
        'nr_strong': '404 Page not found.',
        'nr_pre': ' Check the address, or head back to the ',
        'nr_link': 'home page',
        'nr_post': '.',
        'nr_h2': 'Were you looking for something else?',
        'nr_p': 'Here is what arrived this week.',
        'title_privacy': 'Privacy Policy',
        'pv_badge': 'Demo store',
        'pv_p': 'This is a demonstration store. It exists to show what Maho can do, not to sell anything, and this page is a placeholder rather than a legal document.',
        'pv_h2_data': 'What this demo does with your data',
        'pv_data': 'Nothing that lasts. The store runs on a test installation that is reset from time to time. Anything you type into a form here, an account, an address, a review, a newsletter sign up, is demo data. It is not read by a person, not shared with anyone, and it disappears with the next reset.',
        'pv_h2_cookies': 'Cookies',
        'pv_cookies': 'The store sets the session and preference cookies that every Maho installation needs to keep a cart, a login or a store choice between two pages. There is no analytics, advertising or tracking cookie on this demo.',
        'pv_h2_orders': 'Orders and payments',
        'pv_orders': 'No order placed here is processed, shipped or charged. Do not enter a real card number anywhere on this site.',
        'pv_h2_own': 'Your own store',
        'pv_own': 'When you run Maho for real, replace this page with a privacy policy that describes what your store collects and why. The page lives under CMS pages in the admin, and the cookie notice below it comes from the cookie restriction setting.',
        'notice': 'Demo store. Orders are not processed. ',
        'notice_link': 'Switch store',
    },
    'fr': {
        'title_home': 'Maho Store',
        'meta_home': 'Dix boutiques de démonstration sur une seule installation Maho, une par thème, et tous les produits dans une seule boutique.',
        'badge': 'Dix boutiques, une rue',
        'h1': 'Tout ce que vendent dix boutiques, dans un seul panier',
        'intro': ('Cette boutique propose le catalogue complet des dix boutiques de démonstration Maho. Chaque boutique est aussi un site '
                  'à part entière, avec son propre thème. Choisissez-en une ci-dessous, ou achetez tout ici.'),
        'choose': 'Choisir une boutique',
        'new': 'Nouveautés',
        'hero_alt': 'Dix boutiques dans une même rue',
        'features': [('Une seule installation', 'Onze sites, un seul back-office.'),
                     ('Tous les produits', 'Le catalogue entier, un seul panier.'),
                     ('Dix thèmes', 'Chaque boutique a son style.'),
                     ('Open source', 'Maho est un logiciel libre.')],
        'h2_stores': 'Dix boutiques, une seule rue',
        'visit': 'Visiter {store}',
        'shop_here': 'Acheter {industry} ici',
        'picks': 'Sélection {industry}',
        'h2_quotes': 'Ce que disent nos clients',
        'verified': 'Acheteur vérifié, {store}',
        'h2_news': 'Restez informé',
        'p_news': 'Un email par mois avec les nouveautés des dix boutiques. Rien de plus.',
        'intros': {
            'fashion': 'Des vêtements de voyage et des pièces du quotidien, pour la route.',
            'electronics': "Audio, informatique, photo et maison connectée, testés par ceux qui s'en servent.",
            'food': "Des produits en petites quantités, de fermes et d'artisans que nous connaissons par leur nom.",
            'books': "Une librairie indépendante, peu de rayons et beaucoup d'avis.",
            'jewelry': 'Des bijoux fins et de tous les jours, faits dans un petit atelier avec des métaux recyclés.',
            'beauty': "Soins du visage, soins du corps et parfums, en petites séries et avec peu d'ingrédients.",
            'home': 'Meubles, textiles et objets pour une maison calme, faits par des ateliers que nous visitons.',
            'sports': "De l'équipement pour la course, le vélo, la salle et le sentier, testé par ceux qui s'entraînent.",
            'kids': "Jouets, vêtements et objets pour petites chambres, choisis pour durer plus d'un enfant.",
            'garden': "Plantes, graines, pots et outils d'une pépinière qui cultive ce qu'elle vend.",
        },
        'taglines': {
            'fashion': 'Du lin qui se plie à plat, du denim qui se patine, et le sac pour tout porter.',
            'electronics': "Rien sur l'étagère que nous ne garderions pas nous-mêmes.",
            'food': "Du pain cuit à quatre heures, de l'huile pressée en novembre, du fromage coupé ce matin.",
            'books': 'Des romans, des guides et des livres de cuisine dont notre équipe débat.',
            'jewelry': 'Bagues, chaînes et puces en or et en argent recyclés.',
            'beauty': 'Dix ingrédients au maximum, dans du verre que vous remplissez à nouveau.',
            'home': "Chêne, lin et grès, d'ateliers que nous visitons.",
            'sports': 'Chaussures, couches et accessoires pour la route, le sentier et la piscine.',
            'kids': 'Des jouets en bois et des vêtements doux qui passent au deuxième enfant.',
            'garden': 'Des plantes qui arrivent droites et des outils qui arrivent affûtés.',
        },
        'quotes': ['Taille juste et le tissu fait cher. Lavé deux fois, aucun changement.',
                   'Vif, frais et clairement fait en petites quantités. Je recommanderai.',
                   "Les mesures correspondaient à ce que j'entendais. Une honnêteté rare."],
        'title_about': 'À propos du Maho Store',
        'about_alt': 'Une rangée de petites vitrines dans une rue ensoleillée',
        'about_badge': 'À propos',
        'about_h2': 'Une installation, onze sites',
        'about_p1': "Le Maho Store est la porte d'entrée des données de démonstration Maho. Il utilise le thème par défaut et vend le catalogue complet des dix boutiques de démonstration, de la chemise en lin aux chaussures de trail et aux pots en terre cuite.",
        'about_p2': "Chacune des dix boutiques est aussi un site à part entière sur la même installation, avec son thème, ses catégories, son contenu et ses avis. Utilisez le sélecteur de boutique dans le coin pour passer de l'une à l'autre.",
        'about_p3': "Chaque produit, image, avis et article est une donnée de démonstration générée. Rien n'est en vente ici, et aucune commande n'est traitée.",
        'title_service': 'Service client',
        'svc_h2_ship': 'Expédition et livraison',
        'svc_ship': 'Les commandes passées avant midi un jour ouvré partent le jour même. La livraison standard prend deux à quatre jours ouvrés. La livraison express arrive le jour ouvré suivant. Les plantes, les aliments et les articles fragiles voyagent dans leur propre emballage.',
        'svc_h2_ret': 'Retours',
        'svc_ret': "Vous pouvez retourner un article non utilisé dans les 30 jours qui suivent la livraison. Lancez le retour depuis votre compte et imprimez l'étiquette prépayée. Le remboursement arrive sur le moyen de paiement d'origine dans les cinq jours ouvrés après réception. Les aliments, les plantes et les bijoux personnalisés ne sont pas repris.",
        'svc_h2_pay': 'Paiement',
        'svc_pay': 'Nous acceptons les cartes, PayPal et le virement bancaire. Chaque page de paiement est chiffrée. Nous ne conservons jamais les numéros de carte.',
        'svc_h2_contact': 'Contact',
        'svc_contact_pre': 'Écrivez-nous depuis la ',
        'svc_contact_link': 'page de contact',
        'svc_contact_post': '. Nous répondons sous un jour ouvré.',
        'title_404': '404 Page introuvable',
        'nr_h1': 'Oups !',
        'nr_strong': '404 Page introuvable.',
        'nr_pre': " Vérifiez l'adresse, ou revenez à la ",
        'nr_link': "page d'accueil",
        'nr_post': '.',
        'nr_h2': 'Vous cherchiez autre chose ?',
        'nr_p': 'Voici ce qui est arrivé cette semaine.',
        'title_privacy': 'Politique de confidentialité',
        'pv_badge': 'Boutique de démonstration',
        'pv_p': 'Ceci est une boutique de démonstration. Elle existe pour montrer ce que Maho sait faire, pas pour vendre, et cette page est un texte de remplacement, pas un document légal.',
        'pv_h2_data': 'Ce que cette démonstration fait de vos données',
        'pv_data': "Rien qui dure. La boutique tourne sur une installation de test qui est remise à zéro de temps en temps. Tout ce que vous tapez dans un formulaire ici, un compte, une adresse, un avis, une inscription à la newsletter, est une donnée de démonstration. Personne ne la lit, elle n'est partagée avec personne, et elle disparaît à la remise à zéro suivante.",
        'pv_h2_cookies': 'Cookies',
        'pv_cookies': "La boutique pose les cookies de session et de préférence dont toute installation Maho a besoin pour garder un panier, une connexion ou un choix de boutique d'une page à l'autre. Il n'y a aucun cookie de mesure, de publicité ou de suivi sur cette démonstration.",
        'pv_h2_orders': 'Commandes et paiements',
        'pv_orders': "Aucune commande passée ici n'est traitée, expédiée ou facturée. N'entrez pas de vrai numéro de carte sur ce site.",
        'pv_h2_own': 'Votre propre boutique',
        'pv_own': "Quand vous utiliserez Maho pour de vrai, remplacez cette page par une politique de confidentialité qui décrit ce que votre boutique collecte et pourquoi. La page se trouve dans les pages CMS de l'administration, et l'avis sur les cookies en dessous vient du réglage de restriction des cookies.",
        'notice': 'Boutique de démonstration. Les commandes ne sont pas traitées. ',
        'notice_link': 'Changer de boutique',
    },
    'de': {
        'title_home': 'Maho Store',
        'meta_home': 'Zehn Demoshops auf einer Maho-Installation, einer je Theme, und alle Produkte in einem Shop.',
        'badge': 'Zehn Shops, eine Straße',
        'h1': 'Alles aus zehn Shops, in einem Warenkorb',
        'intro': ('Dieser Shop führt den kompletten Katalog der zehn Maho-Demoshops. Jeder Shop ist außerdem eine eigene Website mit '
                  'eigenem Theme. Wählen Sie unten einen aus, oder kaufen Sie alles hier.'),
        'choose': 'Shop wählen',
        'new': 'Neuheiten',
        'hero_alt': 'Zehn Shops in einer Straße',
        'features': [('Eine Installation', 'Elf Websites, ein Backend.'),
                     ('Alle Produkte', 'Der ganze Katalog, ein Warenkorb.'),
                     ('Zehn Themes', 'Jeder Shop hat sein eigenes Aussehen.'),
                     ('Open Source', 'Maho ist freie Software.')],
        'h2_stores': 'Zehn Shops, eine Straße',
        'visit': '{store} besuchen',
        'shop_here': '{industry} hier kaufen',
        'picks': 'Auswahl {industry}',
        'h2_quotes': 'Was unsere Kunden sagen',
        'verified': 'Verifizierter Käufer, {store}',
        'h2_news': 'Bleiben Sie auf dem Laufenden',
        'p_news': 'Eine E-Mail im Monat mit den Neuheiten aus den zehn Shops. Sonst nichts.',
        'intros': {
            'fashion': 'Reisekleidung und Lieblingsstücke für unterwegs.',
            'electronics': 'Audio, Computer, Kameras und Smart Home, getestet von Menschen, die es benutzen.',
            'food': 'Lebensmittel in kleinen Mengen, von Höfen und Herstellern, die wir beim Namen kennen.',
            'books': 'Eine unabhängige Buchhandlung mit kurzem Regal und langen Meinungen.',
            'jewelry': 'Feiner und alltäglicher Schmuck, in einer kleinen Werkstatt aus recycelten Metallen gefertigt.',
            'beauty': 'Gesichtspflege, Körperpflege und Duft, in kleinen Mengen und mit kurzen Zutatenlisten.',
            'home': 'Möbel, Textilien und Objekte für ein ruhiges Zuhause, aus Werkstätten, die wir besuchen.',
            'sports': 'Ausrüstung für Laufen, Radfahren, Studio und Trail, getestet von Menschen, die trainieren.',
            'kids': 'Spielzeug, Kleidung und Dinge für kleine Zimmer, gewählt für mehr als ein Kind.',
            'garden': 'Pflanzen, Samen, Töpfe und Werkzeug aus einer Gärtnerei, die anbaut, was sie verkauft.',
        },
        'taglines': {
            'fashion': 'Leinen, das flach packt, Denim, der einläuft, und die Tasche dazu.',
            'electronics': 'Nichts im Regal, das wir nicht selbst behalten würden.',
            'food': 'Brot um vier gebacken, Öl im November gepresst, Käse heute Morgen geschnitten.',
            'books': 'Romane, Ratgeber und Kochbücher, über die unser Team streitet.',
            'jewelry': 'Ringe, Ketten und Stecker aus recyceltem Gold und Silber.',
            'beauty': 'Zehn Zutaten oder weniger, in Glas zum Nachfüllen.',
            'home': 'Eiche, Leinen und Steinzeug aus Werkstätten, die wir besuchen.',
            'sports': 'Schuhe, Schichten und Zubehör für Straße, Trail und Becken.',
            'kids': 'Holzspielzeug und weiche Kleidung, die ein zweites Kind übersteht.',
            'garden': 'Pflanzen, die aufrecht ankommen, und Werkzeug, das scharf ankommt.',
        },
        'quotes': ['Fällt normal aus und der Stoff fühlt sich teuer an. Zweimal gewaschen, keine Veränderung.',
                   'Frisch, lebendig und klar in kleinen Mengen gemacht. Ich bestelle wieder.',
                   'Die Messwerte passten zu dem, was ich gehört habe. Seltene Ehrlichkeit.'],
        'title_about': 'Über den Maho Store',
        'about_alt': 'Eine Reihe kleiner Schaufenster an einer sonnigen Straße',
        'about_badge': 'Über uns',
        'about_h2': 'Eine Installation, elf Websites',
        'about_p1': 'Der Maho Store ist die Eingangstür zu den Maho-Beispieldaten. Er läuft auf dem Standard-Theme und verkauft den kompletten Katalog der zehn Demoshops, von Leinenhemden über Trailschuhe bis zu Terrakottatöpfen.',
        'about_p2': 'Jeder der zehn Shops ist außerdem eine eigene Website auf derselben Installation, mit eigenem Theme, eigenen Kategorien, Inhalten und Bewertungen. Mit dem Shop-Umschalter in der Ecke wechseln Sie zwischen ihnen.',
        'about_p3': 'Jedes Produkt, jedes Bild, jede Bewertung und jeder Artikel sind erzeugte Demodaten. Hier ist nichts zu verkaufen, und keine Bestellung wird bearbeitet.',
        'title_service': 'Kundenservice',
        'svc_h2_ship': 'Versand und Lieferung',
        'svc_ship': 'Bestellungen vor 12 Uhr an einem Werktag gehen am selben Tag raus. Der Standardversand dauert zwei bis vier Werktage. Der Expressversand kommt am nächsten Werktag an. Pflanzen, Lebensmittel und zerbrechliche Artikel reisen in eigener Verpackung.',
        'svc_h2_ret': 'Rückgabe',
        'svc_ret': 'Sie können einen unbenutzten Artikel innerhalb von 30 Tagen nach der Lieferung zurückgeben. Starten Sie die Rückgabe in Ihrem Konto und drucken Sie das frankierte Etikett. Die Erstattung erreicht das ursprüngliche Zahlungsmittel innerhalb von fünf Werktagen nach Eingang. Lebensmittel, Pflanzen und personalisierter Schmuck sind von der Rückgabe ausgeschlossen.',
        'svc_h2_pay': 'Zahlung',
        'svc_pay': 'Wir akzeptieren Karten, PayPal und Überweisung. Jede Zahlungsseite ist verschlüsselt. Wir speichern nie Kartennummern.',
        'svc_h2_contact': 'Kontakt',
        'svc_contact_pre': 'Schreiben Sie uns über die ',
        'svc_contact_link': 'Kontaktseite',
        'svc_contact_post': '. Wir antworten innerhalb eines Werktags.',
        'title_404': '404 Seite nicht gefunden',
        'nr_h1': 'Hoppla!',
        'nr_strong': '404 Seite nicht gefunden.',
        'nr_pre': ' Prüfen Sie die Adresse, oder gehen Sie zurück zur ',
        'nr_link': 'Startseite',
        'nr_post': '.',
        'nr_h2': 'Haben Sie etwas anderes gesucht?',
        'nr_p': 'Das ist diese Woche angekommen.',
        'title_privacy': 'Datenschutzerklärung',
        'pv_badge': 'Demoshop',
        'pv_p': 'Dies ist ein Demoshop. Er zeigt, was Maho kann, und verkauft nichts. Diese Seite ist ein Platzhalter, kein Rechtsdokument.',
        'pv_h2_data': 'Was diese Demo mit Ihren Daten macht',
        'pv_data': 'Nichts, was bleibt. Der Shop läuft auf einer Testinstallation, die von Zeit zu Zeit zurückgesetzt wird. Alles, was Sie hier in ein Formular eingeben, ein Konto, eine Adresse, eine Bewertung, eine Newsletter-Anmeldung, ist ein Demodatum. Kein Mensch liest es, es wird mit niemandem geteilt, und es verschwindet beim nächsten Zurücksetzen.',
        'pv_h2_cookies': 'Cookies',
        'pv_cookies': 'Der Shop setzt die Sitzungs-Cookies und die Einstellungs-Cookies, die jede Maho-Installation braucht, um einen Warenkorb, eine Anmeldung oder eine Shop-Auswahl über zwei Seiten zu halten. Es gibt kein Analyse-Cookie, kein Werbe-Cookie und kein Tracking-Cookie in dieser Demo.',
        'pv_h2_orders': 'Bestellungen und Zahlungen',
        'pv_orders': 'Keine hier aufgegebene Bestellung wird bearbeitet, versendet oder belastet. Geben Sie auf dieser Website keine echte Kartennummer ein.',
        'pv_h2_own': 'Ihr eigener Shop',
        'pv_own': 'Wenn Sie Maho im Ernstfall betreiben, ersetzen Sie diese Seite durch eine Datenschutzerklärung, die beschreibt, was Ihr Shop erhebt und warum. Die Seite liegt im Backend unter den CMS-Seiten, und der Cookie-Hinweis darunter kommt aus der Einstellung zur Cookie-Beschränkung.',
        'notice': 'Demoshop. Bestellungen werden nicht bearbeitet. ',
        'notice_link': 'Shop wechseln',
    },
    'it': {
        'title_home': 'Maho Store',
        'meta_home': 'Dieci negozi dimostrativi su una sola installazione Maho, uno per tema, e tutti i prodotti in un solo negozio.',
        'badge': 'Dieci negozi, una via',
        'h1': 'Tutto da dieci negozi, in un solo carrello',
        'intro': ("Questo negozio propone l'intero catalogo dei dieci negozi dimostrativi Maho. Ogni negozio è anche un sito a sé, con "
                  'il suo tema. Scegline uno qui sotto, oppure compra tutto qui.'),
        'choose': 'Scegli un negozio',
        'new': 'Novità',
        'hero_alt': 'Dieci negozi in una stessa via',
        'features': [('Una sola installazione', 'Undici siti, un solo pannello.'),
                     ('Tutti i prodotti', "L'intero catalogo, un solo carrello."),
                     ('Dieci temi', 'Ogni negozio ha il suo stile.'),
                     ('Open source', 'Maho è software libero.')],
        'h2_stores': 'Dieci negozi, una sola via',
        'visit': 'Visita {store}',
        'shop_here': 'Compra {industry} qui',
        'picks': 'Selezione {industry}',
        'h2_quotes': 'Cosa dicono i nostri clienti',
        'verified': 'Acquirente verificato, {store}',
        'h2_news': 'Resta aggiornato',
        'p_news': 'Una email al mese con le novità dei dieci negozi. Niente altro.',
        'intros': {
            'fashion': 'Capi da viaggio e pezzi di tutti i giorni, per la strada.',
            'electronics': 'Audio, informatica, fotografia e casa connessa, provati da chi li usa.',
            'food': 'Cibo in piccole quantità, da fattorie e artigiani che conosciamo per nome.',
            'books': 'Una libreria indipendente, con pochi scaffali e molte opinioni.',
            'jewelry': 'Gioielli fini e di tutti i giorni, fatti in un piccolo laboratorio con metalli riciclati.',
            'beauty': 'Cura del viso, cura del corpo e profumi, in piccole serie e con pochi ingredienti.',
            'home': 'Mobili, tessuti e oggetti per una casa tranquilla, da laboratori che visitiamo.',
            'sports': 'Attrezzatura per la corsa, la bici, la palestra e il sentiero, provata da chi si allena.',
            'kids': 'Giochi, vestiti e oggetti per stanze piccole, scelti per durare più di un bambino.',
            'garden': 'Piante, semi, vasi e attrezzi da un vivaio che coltiva quello che vende.',
        },
        'taglines': {
            'fashion': 'Lino che si piega piatto, denim che si ammorbidisce, e la borsa per portarlo.',
            'electronics': 'Niente sullo scaffale che non terremmo per noi.',
            'food': 'Pane cotto alle quattro, olio spremuto a novembre, formaggio tagliato stamattina.',
            'books': 'Romanzi, guide e libri di cucina su cui il nostro staff discute.',
            'jewelry': 'Anelli, catene e lobi in oro e argento riciclati.',
            'beauty': 'Dieci ingredienti o meno, in vetro che si ricarica.',
            'home': 'Rovere, lino e gres da laboratori che visitiamo.',
            'sports': 'Scarpe, strati e accessori per la strada, il sentiero e la piscina.',
            'kids': 'Giochi in legno e vestiti morbidi che arrivano al secondo bambino.',
            'garden': 'Piante che arrivano dritte e attrezzi che arrivano affilati.',
        },
        'quotes': ['Veste come da taglia e il tessuto sembra costoso. Lavato due volte, nessun cambiamento.',
                   'Vivo, fresco e chiaramente fatto in piccole quantità. Ordinerò ancora.',
                   'Le misure corrispondevano a quello che ho sentito. Onestà rara.'],
        'title_about': 'Informazioni sul Maho Store',
        'about_alt': 'Una fila di piccole vetrine in una via soleggiata',
        'about_badge': 'Chi siamo',
        'about_h2': 'Una installazione, undici siti',
        'about_p1': "Il Maho Store è la porta d'ingresso dei dati dimostrativi Maho. Usa il tema predefinito e vende l'intero catalogo dei dieci negozi dimostrativi, dalle camicie di lino alle scarpe da trail ai vasi di terracotta.",
        'about_p2': "Ognuno dei dieci negozi è anche un sito a sé sulla stessa installazione, con il suo tema, le sue categorie, i suoi contenuti e le sue recensioni. Usa il selettore di negozio nell'angolo per passare dall'uno all'altro.",
        'about_p3': 'Ogni prodotto, immagine, recensione e articolo è un dato dimostrativo generato. Qui non è in vendita niente, e nessun ordine viene elaborato.',
        'title_service': 'Servizio clienti',
        'svc_h2_ship': 'Spedizione e consegna',
        'svc_ship': 'Gli ordini fatti prima di mezzogiorno in un giorno lavorativo partono lo stesso giorno. La consegna standard richiede da due a quattro giorni lavorativi. La consegna espressa arriva il giorno lavorativo successivo. Piante, alimenti e articoli fragili viaggiano in un imballaggio dedicato.',
        'svc_h2_ret': 'Resi',
        'svc_ret': "Puoi restituire un articolo non usato entro 30 giorni dalla consegna. Avvia il reso dalla pagina del tuo account e stampa l'etichetta prepagata. Il rimborso arriva sul metodo di pagamento originale entro cinque giorni lavorativi dalla ricezione. Alimenti, piante e gioielli personalizzati non si possono restituire.",
        'svc_h2_pay': 'Pagamento',
        'svc_pay': 'Accettiamo carte, PayPal e bonifico bancario. Ogni pagina di pagamento è cifrata. Non conserviamo mai i numeri di carta.',
        'svc_h2_contact': 'Contatti',
        'svc_contact_pre': 'Scrivici dalla ',
        'svc_contact_link': 'pagina dei contatti',
        'svc_contact_post': '. Rispondiamo entro un giorno lavorativo.',
        'title_404': '404 Pagina non trovata',
        'nr_h1': 'Ops!',
        'nr_strong': '404 Pagina non trovata.',
        'nr_pre': " Controlla l'indirizzo, oppure torna alla ",
        'nr_link': 'pagina iniziale',
        'nr_post': '.',
        'nr_h2': "Cercavi qualcosa d'altro?",
        'nr_p': 'Ecco che cosa è arrivato questa settimana.',
        'title_privacy': 'Informativa sulla privacy',
        'pv_badge': 'Negozio dimostrativo',
        'pv_p': 'Questo è un negozio dimostrativo. Esiste per mostrare che cosa sa fare Maho, non per vendere, e questa pagina è un segnaposto, non un documento legale.',
        'pv_h2_data': 'Che cosa fa questa demo con i tuoi dati',
        'pv_data': 'Niente che duri. Il negozio gira su una installazione di prova che viene azzerata ogni tanto. Tutto quello che scrivi in un modulo qui, un account, un indirizzo, una recensione, una iscrizione alla newsletter, è un dato dimostrativo. Nessuna persona lo legge, non viene condiviso con nessuno, e sparisce al prossimo azzeramento.',
        'pv_h2_cookies': 'Cookie',
        'pv_cookies': "Il negozio usa i cookie di sessione e i cookie di preferenza di cui ogni installazione Maho ha bisogno per tenere un carrello, un accesso o una scelta di negozio da una pagina all'altra. In questa demo non c'è nessun cookie di analisi, di pubblicità o di tracciamento.",
        'pv_h2_orders': 'Ordini e pagamenti',
        'pv_orders': 'Nessun ordine fatto qui viene elaborato, spedito o addebitato. Non inserire un numero di carta vero in questo sito.',
        'pv_h2_own': 'Il tuo negozio',
        'pv_own': "Quando userai Maho per davvero, sostituisci questa pagina con una informativa sulla privacy che descriva che cosa raccoglie il tuo negozio e perché. La pagina si trova nelle pagine CMS del pannello, e l'avviso sui cookie qui sotto viene dall'impostazione di restrizione dei cookie.",
        'notice': 'Negozio dimostrativo. Gli ordini non vengono elaborati. ',
        'notice_link': 'Cambia negozio',
    },
}


def store_names():
    """Website code to website name. The extra store view rows of a website carry no name."""
    return {r['website_code']: r['website_name'] for r in read(os.path.join(PACKS, '_shared', 'stores.csv'))
            if r['website_name'] != ''}


def root_descriptions(codes):
    out = {}
    for code, name in codes:
        for r in read(os.path.join(PACKS, code, 'categories.csv')):
            if r['path'] == '':
                out[code] = r['description']
    return out


def quotes(codes):
    """The first review of three industries, as customer quotes."""
    names = store_names()
    picked = []
    for code in ('fashion', 'food', 'electronics'):
        rows = read(os.path.join(PACKS, code, 'reviews.csv'))
        if rows:
            picked.append((rows[0]['detail'], rows[0]['nickname'], names[code]))
    return picked


def copy_for(view, codes):
    """The strings of a store view. English reads the catalog copy from the industry packs."""
    t = dict(COPY[view])
    if view == STORE_CODE:
        t['intros'] = root_descriptions(codes)
        t['taglines'] = {code: SECTIONS[code][2] for code, name in codes}
        t['quotes'] = [text for text, who, where in quotes(codes)]
    return t


def home(codes, t):
    names = store_names()
    tiles = ''.join(f'''    <a class="hub-logo" href="{{{{store url="" _store="{code}"}}}}" title="{names[code]}"><img src="{{{{media url="wysiwyg/{code}/logo.svg"}}}}" alt="{names[code]}" /></a>
''' for code, name in codes)
    features = ''.join(f'''    <div data-type="maho-column">
        <table style="min-width: 50px;">
            <colgroup>
                <col style="min-width: 25px;" />
                <col style="min-width: 25px;" />
            </colgroup>
            <tbody>
                <tr>
                    <td colspan="1" rowspan="1" style="width: 1%; padding-right: 0.75rem; vertical-align: middle;">
                        <p>{{{{icon name="{icon}" size="32"}}}}</p>
                    </td>
                    <td colspan="1" rowspan="1" style="vertical-align: middle;">
                        <p><strong>{title}</strong><br />{text}</p>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
''' for icon, (title, text) in zip(FEATURE_ICONS, t['features']))
    sections = ''
    for index, (code, name) in enumerate(codes):
        left = index % 2 == 0
        areas = "&#039;a b&#039; &#039;a c&#039;" if left else "&#039;b a&#039; &#039;c a&#039;"
        columns = '2fr 3fr' if left else '3fr 2fr'
        template = f'&#34;a b&#34; auto &#34;a c&#34; 1fr / {columns}' if left else f'&#34;b a&#34; auto &#34;c a&#34; 1fr / {columns}'
        visit = t['visit'].format(store=names[code])
        shop_here = t['shop_here'].format(industry=name, industry_lower=name.lower())
        picks = t['picks'].format(industry=name, industry_lower=name.lower())
        blurb = t['intros'][code] + ' ' + t['taglines'][code]
        sections += f'''<div data-preset="custom" data-areas="{areas}" data-columns="{columns}" data-rows="auto 1fr" data-gap="medium" data-style="none" data-type="maho-bento" style="grid-template: {template};">
    <div data-area="a" data-type="maho-bento-cell" style="grid-area: a;">
        <p><a href="{{{{store url="" _store="{code}"}}}}" title="{visit}"><img src="{{{{media url="wysiwyg/store/section-{code}.webp"}}}}" alt="{names[code]}" /></a></p>
    </div>
    <div class="card card-border" data-area="b" data-type="maho-bento-cell" style="grid-area: b;">
        <div class="card-body">
            <h2><a class="hub-mark" href="{{{{store url="" _store="{code}"}}}}" title="{visit}"><img src="{{{{media url="wysiwyg/{code}/logo.svg"}}}}" alt="{names[code]}" /></a></h2>
            <p>{blurb}</p>
            <p><a class="btn btn-primary" href="{{{{store url="" _store="{code}"}}}}">{visit}</a> <a class="btn btn-ghost" href="{{{{store url="{code}"}}}}">{shop_here}</a></p>
        </div>
    </div>
    <div data-area="c" data-type="maho-bento-cell" style="grid-area: c;">
        {{{{widget type="catalog/product_widget_list" title="{picks}" category_id="{{{{category_id:{ROOT_CATEGORY}/{code}}}}}" sort="position" only_in_stock="1" products_count="3" template="catalog/product/widget/list/content/list_grid.phtml"}}}}
    </div>
</div>
'''
    quote_html = ''
    for (english, who, where), text in zip(quotes(codes), t['quotes']):
        verified = t['verified'].format(store=where)
        quote_html += f'''    <div data-type="maho-column">
        <p>{STARS}</p>
        <blockquote>
            <p>{text}</p>
        </blockquote>
        <p><strong>{who}</strong><br />{verified}</p>
    </div>
'''
    badge, h1, intro, choose, new = t['badge'], t['h1'], t['intro'], t['choose'], t['new']
    hero_alt, h2_stores, h2_quotes = t['hero_alt'], t['h2_stores'], t['h2_quotes']
    h2_news, p_news = t['h2_news'], t['p_news']
    visit_food = t['visit'].format(store=names['food'])
    return f'''<div data-preset="feature-left" data-areas="&#039;a b&#039; &#039;a c&#039;" data-columns="2fr 1fr" data-rows="auto auto" data-gap="medium" data-style="none" data-type="maho-bento" style="grid-template: &#34;a b&#34; auto &#34;a c&#34; auto / 2fr 1fr;">
    <div data-area="a" data-type="maho-bento-cell" style="grid-area: a;">
        <p><a href="#stores" title="{choose}"><img src="{{{{media url="wysiwyg/store/hero-main.webp"}}}}" alt="{hero_alt}" /></a></p>
    </div>
    <div class="card card-border" data-area="b" data-type="maho-bento-cell" style="grid-area: b;">
        <div class="card-body">
            <p><span class="badge badge-primary">{badge}</span></p>
            <h1>{h1}</h1>
            <p>{intro}</p>
            <p><a class="btn btn-primary" href="#stores">{choose}</a> <a class="btn btn-ghost" href="#new">{new}</a></p>
        </div>
    </div>
    <div data-area="c" data-type="maho-bento-cell" style="grid-area: c;">
        <p><a href="{{{{store url="" _store="food"}}}}" title="{visit_food}"><img src="{{{{media url="wysiwyg/store/hero-side.webp"}}}}" alt="{names['food']}" /></a></p>
    </div>
</div>
<div data-preset="4-equal" data-gap="medium" data-style="separated" data-type="maho-columns">
{features}</div>
<h2 id="stores">{h2_stores}</h2>
<div class="hub-logos">
{tiles}</div>
{sections}<h2 id="new">{new}</h2>
{{{{widget type="catalog/product_widget_new" display_type="new_products" products_count="4" template="catalog/product/widget/new/content/new_grid.phtml"}}}}
<h2>{h2_quotes}</h2>
<div data-preset="3-equal" data-gap="medium" data-style="cards" data-type="maho-columns">
{quote_html}</div>
<div class="card card-border">
    <div class="card-body">
        <h2 style="text-align: center;">{h2_news}</h2>
        <p style="text-align: center;">{p_news}</p>
        {{{{widget type="newsletter/widget_subscribe" template="newsletter/subscribe.phtml"}}}}
    </div>
</div>
'''


def about(t):
    alt, badge, h2 = t['about_alt'], t['about_badge'], t['about_h2']
    p1, p2, p3 = t['about_p1'], t['about_p2'], t['about_p3']
    return f'''<div data-type="maho-columns" data-preset="2-equal" data-gap="large" data-style="none">
    <div data-type="maho-column">
        <p><img src="{{{{media url="wysiwyg/store/about.webp"}}}}" alt="{alt}"></p>
    </div>
    <div data-type="maho-column">
        <p><span class="badge badge-outline">{badge}</span></p>
        <h2>{h2}</h2>
        <p>{p1}</p>
        <p>{p2}</p>
        <p>{p3}</p>
    </div>
</div>
'''


def service(t):
    h1, h2_ship, ship = t['title_service'], t['svc_h2_ship'], t['svc_ship']
    h2_ret, ret, h2_pay, pay = t['svc_h2_ret'], t['svc_ret'], t['svc_h2_pay'], t['svc_pay']
    h2_contact = t['svc_h2_contact']
    pre, link, post = t['svc_contact_pre'], t['svc_contact_link'], t['svc_contact_post']
    return f'''<h1>{h1}</h1>
<h2>{h2_ship}</h2>
<p>{ship}</p>
<h2>{h2_ret}</h2>
<p>{ret}</p>
<h2>{h2_pay}</h2>
<p>{pay}</p>
<h2>{h2_contact}</h2>
<p>{pre}<a href="{{{{store url="contacts"}}}}">{link}</a>{post}</p>
'''


def no_route(t):
    h1, strong, pre = t['nr_h1'], t['nr_strong'], t['nr_pre']
    link, post, h2, p = t['nr_link'], t['nr_post'], t['nr_h2'], t['nr_p']
    return f'''<h1 style="text-align: center">{h1}</h1>
<p style="text-align: center"><strong>{strong}</strong>{pre}<a href="{{{{store url=""}}}}">{link}</a>{post}</p>
<h2 style="text-align: center">{h2}</h2>
<p style="text-align: center">{p}</p>
{{{{widget type="catalog/product_widget_new" display_type="new_products" products_count="5" template="catalog/product/widget/new/content/new_grid.phtml"}}}}
'''


def privacy(t):
    badge, lead = t['pv_badge'], t['pv_p']
    h2_data, data = t['pv_h2_data'], t['pv_data']
    h2_cookies, cookies = t['pv_h2_cookies'], t['pv_cookies']
    h2_orders, orders = t['pv_h2_orders'], t['pv_orders']
    h2_own, own = t['pv_h2_own'], t['pv_own']
    return f'''<p><span class="badge badge-warning">{badge}</span></p>
<p>{lead}</p>
<h2>{h2_data}</h2>
<p>{data}</p>
<h2>{h2_cookies}</h2>
<p>{cookies}</p>
<h2>{h2_orders}</h2>
<p>{orders}</p>
<h2>{h2_own}</h2>
<p>{own}</p>
'''


def demo_notice(t):
    text, link = t['notice'], t['notice_link']
    return f'''<p>{text}<a href="#switch-store">{link}</a></p>
'''


def pages(view, t):
    """The CMS page rows of one store view, the home page first."""
    s = suffix(view)
    return [
        dict(identifier='home', stores=view, title=t['title_home'], root_template='one_column',
             content_file=f'home{s}.html', is_active=1, is_home=1, meta_description=t['meta_home']),
        dict(identifier='about-maho-demo-store', stores=view, title=t['title_about'], root_template='one_column',
             content_file=f'about{s}.html', is_active=1, is_home=0, meta_description=''),
        dict(identifier='customer-service', stores=view, title=t['title_service'], root_template='one_column',
             content_file=f'customer-service{s}.html', is_active=1, is_home=0, meta_description=''),
        dict(identifier='no-route', stores=view, title=t['title_404'], root_template='one_column',
             content_file=f'no-route{s}.html', is_active=1, is_home=0, meta_description=''),
        # The English privacy policy replaces the distro page on every store of the installation.
        # A store view row wins over it, because Maho reads the most specific store row first.
        dict(identifier='privacy-policy-cookie-restriction-mode', stores='' if view == STORE_CODE else view,
             title=t['title_privacy'], root_template='one_column', content_file=f'privacy-policy{s}.html',
             is_active=1, is_home=0, meta_description=''),
    ]


def main():
    codes = industries()
    write(os.path.join(STORE, 'categories.csv'), categories(codes),
          ['root', 'path', 'store_code', 'name', 'is_active', 'include_in_menu', 'is_anchor', 'position', 'display_mode', 'landing_page', 'image', 'description', 'meta_title', 'meta_description'])
    rows = products(codes)
    assert len(rows) % ROWS_PER_PRODUCT == 0, 'the product rows are no longer a whole number of products'
    write(os.path.join(STORE, 'products.csv'), rows,
          ['sku', '_product_websites', '_root_category', '_category', '_store'] + REQUIRED)
    write(os.path.join(STORE, 'reviews.csv'), reviews(codes), ['sku', 'store_code', 'nickname', 'title', 'detail', 'rating', 'created_at'])

    english = pages(STORE_CODE, copy_for(STORE_CODE, codes))
    # The distro ships these two pages, and every store of this installation writes its own.
    page_rows = [english[0],
                 dict(identifier='about-maho-demo-store', stores='', title='', root_template='', content_file='', is_active=0, is_home=0, meta_description=''),
                 dict(identifier='customer-service', stores='', title='', root_template='', content_file='', is_active=0, is_home=0, meta_description='')] + english[1:]
    block_rows = []
    content = {}
    for view in STORE_VIEWS:
        t = copy_for(view, codes)
        s = suffix(view)
        if view != STORE_CODE:
            page_rows += pages(view, t)
        block_rows.append(dict(identifier='demo-notice', stores='' if view == STORE_CODE else view,
                               title='Demo notice' if view == STORE_CODE else f'Demo notice ({view})',
                               content_file=f'demo-notice{s}.html', is_active=1))
        content[f'home{s}.html'] = home(codes, t)
        content[f'about{s}.html'] = about(t)
        content[f'customer-service{s}.html'] = service(t)
        content[f'no-route{s}.html'] = no_route(t)
        content[f'privacy-policy{s}.html'] = privacy(t)
        content[f'demo-notice{s}.html'] = demo_notice(t)

    write(os.path.join(STORE, 'cms_pages.csv'), page_rows,
          ['identifier', 'stores', 'title', 'root_template', 'content_file', 'is_active', 'is_home', 'meta_description'])
    write(os.path.join(STORE, 'cms_blocks.csv'), block_rows, ['identifier', 'stores', 'title', 'content_file', 'is_active'])
    os.makedirs(os.path.join(STORE, 'content'), exist_ok=True)
    for name, body in content.items():
        with open(os.path.join(STORE, 'content', name), 'w') as f:
            f.write(body)
    print(f'store pack: {len(codes)} industries, {len(STORE_VIEWS)} store views')
    if MISSING:
        print(f'{len(MISSING)} English strings have no French, German or Italian text yet in the specs')


if __name__ == '__main__':
    main()
