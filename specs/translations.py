"""The store view translations of the Maho Store website, keyed by the English string.

The Maho Store website (packs/store) carries four store views: English, French, German and
Italian. tools/build-store-pack.py looks every English string up here and writes a store scoped
row for each language it finds. A string that is missing stays in English, and the build prints
how many are still missing, so the file can be filled a pack at a time.

The catalog itself lives in the industry packs, so the keys are the English strings of those
packs: category names and descriptions, product names and descriptions, review titles and bodies.
The attribute option labels are not here: they are shared by several industries and live in
packs/_shared/attribute_options.csv, next to the labels they translate.

The keys must match the English text character for character.
"""

# Category names and descriptions of the store tree.
CATEGORIES = {
    'Default Category': ('Catégorie par défaut', 'Standardkategorie', 'Categoria predefinita'),
    'Every product of the ten Maho demo stores, on the default theme.': (
        'Tous les produits des dix boutiques de démonstration Maho, sur le thème par défaut.',
        'Jedes Produkt der zehn Maho-Demoshops, auf dem Standard-Theme.',
        'Ogni prodotto dei dieci negozi dimostrativi Maho, sul tema predefinito.'),

    # Fashion
    'Fashion': ('Mode', 'Mode', 'Moda'),
    'Travel-wear and lifestyle pieces for the journey.': (
        'Des vêtements de voyage et des pièces du quotidien, pour la route.',
        'Reisekleidung und Lieblingsstücke für unterwegs.',
        'Capi da viaggio e pezzi di tutti i giorni, per la strada.'),
    'Women': ('Femme', 'Damen', 'Donna'),
    'New Arrivals': ('Nouveautés', 'Neuheiten', 'Novità'),
    'Tops & Blouses': ('Hauts et chemisiers', 'Tops und Blusen', 'Top e camicette'),
    'Pants & Denim': ('Pantalons et jeans', 'Hosen und Jeans', 'Pantaloni e jeans'),
    'Dresses & Skirts': ('Robes et jupes', 'Kleider und Röcke', 'Abiti e gonne'),
    'Men': ('Homme', 'Herren', 'Uomo'),
    'Shirts': ('Chemises', 'Hemden', 'Camicie'),
    'Tees, Knits and Polos': ('T-shirts, mailles et polos', 'Shirts, Strick und Polos', 'T-shirt, maglieria e polo'),
    'Blazers': ('Vestes', 'Sakkos', 'Giacche'),
    'Accessories': ('Accessoires', 'Accessoires', 'Accessori'),
    'Eyewear': ('Lunettes', 'Brillen', 'Occhiali'),
    'Shoes': ('Chaussures', 'Schuhe', 'Scarpe'),
    'Bags & Luggage': ('Sacs et bagages', 'Taschen und Gepäck', 'Borse e valigie'),
    'Sale': ('Soldes', 'Sale', 'Saldi'),

    # Electronics
    'Electronics': ('Électronique', 'Elektronik', 'Elettronica'),
    'Audio, computing, cameras and smart home gear, tested by people who use it.': (
        "Audio, informatique, photo et maison connectée, testés par ceux qui s'en servent.",
        'Audio, Computer, Kameras und Smart Home, getestet von Menschen, die es benutzen.',
        'Audio, informatica, fotografia e casa connessa, provati da chi li usa.'),
    'Audio': ('Audio', 'Audio', 'Audio'),
    'Computing': ('Informatique', 'Computer', 'Informatica'),
    'Cameras': ('Photo', 'Kameras', 'Fotografia'),
    'Smart Home': ('Maison connectée', 'Smart Home', 'Casa connessa'),
    'Wearables': ('Objets connectés', 'Wearables', 'Indossabili'),

    # Food
    'Food': ('Épicerie', 'Lebensmittel', 'Alimentari'),
    'Small-batch food from farms and makers we know by name.': (
        "Des produits en petites quantités, de fermes et d'artisans que nous connaissons par leur nom.",
        'Lebensmittel in kleinen Mengen, von Höfen und Herstellern, die wir beim Namen kennen.',
        'Cibo in piccole quantità, da fattorie e artigiani che conosciamo per nome.'),
    'Pantry': ('Garde-manger', 'Vorrat', 'Dispensa'),
    'Bakery': ('Boulangerie', 'Bäckerei', 'Panetteria'),
    'Cheese & Charcuterie': ('Fromages et charcuterie', 'Käse und Wurst', 'Formaggi e salumi'),
    'Coffee & Tea': ('Café et thé', 'Kaffee und Tee', 'Caffè e tè'),
    'Drinks': ('Boissons', 'Getränke', 'Bevande'),
    'Gift Boxes': ('Coffrets cadeaux', 'Geschenkboxen', 'Confezioni regalo'),

    # Books
    'Books': ('Livres', 'Bücher', 'Libri'),
    'An independent bookshop with a short shelf and long opinions.': (
        "Une librairie indépendante, peu de rayons et beaucoup d'avis.",
        'Eine unabhängige Buchhandlung mit kurzem Regal und langen Meinungen.',
        'Una libreria indipendente, con pochi scaffali e molte opinioni.'),
    'Fiction': ('Romans', 'Belletristik', 'Narrativa'),
    'Crime & Thrillers': ('Policiers et thrillers', 'Krimis und Thriller', 'Gialli e thriller'),
    'Science & Nature': ('Science et nature', 'Wissenschaft und Natur', 'Scienza e natura'),
    'History': ('Histoire', 'Geschichte', 'Storia'),
    'Cooking': ('Cuisine', 'Kochen', 'Cucina'),
    'Children': ('Enfants', 'Kinder', 'Bambini'),

    # Jewelry
    'Jewelry': ('Bijoux', 'Schmuck', 'Gioielli'),
    'Fine and everyday jewelry, made in a small workshop from recycled metals.': (
        'Des bijoux fins et de tous les jours, faits dans un petit atelier avec des métaux recyclés.',
        'Feiner und alltäglicher Schmuck, in einer kleinen Werkstatt aus recycelten Metallen gefertigt.',
        'Gioielli fini e di tutti i giorni, fatti in un piccolo laboratorio con metalli riciclati.'),
    'Rings': ('Bagues', 'Ringe', 'Anelli'),
    'Necklaces': ('Colliers', 'Ketten', 'Collane'),
    'Earrings': ("Boucles d'oreilles", 'Ohrringe', 'Orecchini'),
    'Bracelets': ('Bracelets', 'Armbänder', 'Bracciali'),
    'Engagement': ('Fiançailles', 'Verlobung', 'Fidanzamento'),
    'Gifts': ('Cadeaux', 'Geschenke', 'Regali'),

    # Beauty
    'Beauty': ('Beauté', 'Beauty', 'Bellezza'),
    'Skincare, body care and fragrance made in small batches with short ingredient lists.': (
        "Soins du visage, soins du corps et parfums, en petites séries et avec peu d'ingrédients.",
        'Gesichtspflege, Körperpflege und Duft, in kleinen Mengen und mit kurzen Zutatenlisten.',
        'Cura del viso, cura del corpo e profumi, in piccole serie e con pochi ingredienti.'),
    'Cleansers': ('Nettoyants', 'Reinigung', 'Detergenti'),
    'Serums': ('Sérums', 'Seren', 'Sieri'),
    'Moisturisers': ('Hydratants', 'Feuchtigkeitspflege', 'Idratanti'),
    'Body': ('Corps', 'Körper', 'Corpo'),
    'Fragrance': ('Parfums', 'Duft', 'Profumi'),
    'Sets': ('Coffrets', 'Sets', 'Cofanetti'),

    # Home
    'Home': ('Maison', 'Wohnen', 'Casa'),
    'Furniture, textiles and objects for a calm home, made by workshops we visit.': (
        'Meubles, textiles et objets pour une maison calme, faits par des ateliers que nous visitons.',
        'Möbel, Textilien und Objekte für ein ruhiges Zuhause, aus Werkstätten, die wir besuchen.',
        'Mobili, tessuti e oggetti per una casa tranquilla, da laboratori che visitiamo.'),
    'Furniture': ('Meubles', 'Möbel', 'Mobili'),
    'Seating': ('Assises', 'Sitzmöbel', 'Sedute'),
    'Bedding': ('Linge de lit', 'Bettwaren', 'Biancheria da letto'),
    'Kitchen & Dining': ('Cuisine et table', 'Küche und Esszimmer', 'Cucina e tavola'),
    'Lighting': ('Luminaires', 'Leuchten', 'Illuminazione'),
    'Decor': ('Décoration', 'Deko', 'Decorazioni'),

    # Sports
    'Sports': ('Sport', 'Sport', 'Sport'),
    'Gear for running, cycling, the gym and the trail, tested by people who train.': (
        "De l'équipement pour la course, le vélo, la salle et le sentier, testé par ceux qui s'entraînent.",
        'Ausrüstung für Laufen, Radfahren, Studio und Trail, getestet von Menschen, die trainieren.',
        'Attrezzatura per la corsa, la bici, la palestra e il sentiero, provata da chi si allena.'),
    'Running': ('Course', 'Laufen', 'Corsa'),
    'Cycling': ('Vélo', 'Radfahren', 'Ciclismo'),
    'Gym & Training': ('Salle et entraînement', 'Studio und Training', 'Palestra e allenamento'),
    'Yoga & Recovery': ('Yoga et récupération', 'Yoga und Regeneration', 'Yoga e recupero'),
    'Hiking': ('Randonnée', 'Wandern', 'Escursionismo'),
    'Swimming': ('Natation', 'Schwimmen', 'Nuoto'),

    # Kids
    'Kids': ('Enfants', 'Kinder', 'Bambini'),
    'Toys, clothes and things for small rooms, chosen to last more than one child.': (
        "Jouets, vêtements et objets pour petites chambres, choisis pour durer plus d'un enfant.",
        'Spielzeug, Kleidung und Dinge für kleine Zimmer, gewählt für mehr als ein Kind.',
        'Giochi, vestiti e oggetti per stanze piccole, scelti per durare più di un bambino.'),
    'Toys': ('Jouets', 'Spielzeug', 'Giochi'),
    'Clothing': ('Vêtements', 'Kleidung', 'Abbigliamento'),
    'Nursery': ('Chambre de bébé', 'Kinderzimmer', 'Cameretta'),
    'Outdoor': ('Plein air', 'Draußen', "All'aperto"),

    # Garden
    'Garden': ('Jardin', 'Garten', 'Giardino'),
    'Plants, seeds, pots and tools from a nursery that grows what it sells.': (
        "Plantes, graines, pots et outils d'une pépinière qui cultive ce qu'elle vend.",
        'Pflanzen, Samen, Töpfe und Werkzeug aus einer Gärtnerei, die anbaut, was sie verkauft.',
        'Piante, semi, vasi e attrezzi da un vivaio che coltiva quello che vende.'),
    'Houseplants': ("Plantes d'intérieur", 'Zimmerpflanzen', 'Piante da interno'),
    'Outdoor Plants': ("Plantes d'extérieur", 'Gartenpflanzen', 'Piante da esterno'),
    'Seeds & Bulbs': ('Graines et bulbes', 'Samen und Zwiebeln', 'Semi e bulbi'),
    'Pots & Planters': ('Pots et jardinières', 'Töpfe und Kübel', 'Vasi e fioriere'),
    'Tools': ('Outils', 'Werkzeug', 'Attrezzi'),
    'Outdoor Furniture': ('Mobilier de jardin', 'Gartenmöbel', 'Mobili da giardino'),
}

# Review titles and bodies. Filled pack by pack.
REVIEWS = {}

# Product names and descriptions. Filled pack by pack.
PRODUCTS = {}

# Every table is keyed the same way, so the builder reads one merged map per language.
LANGUAGES = ('fr', 'de', 'it')


def table(language):
    """English string to translation, for one store view code."""
    index = LANGUAGES.index(language)
    merged = {}
    for source in (CATEGORIES, REVIEWS, PRODUCTS):
        for english, values in source.items():
            merged[english] = values[index]
    return merged
