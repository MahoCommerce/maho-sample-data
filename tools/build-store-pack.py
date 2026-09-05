#!/usr/bin/env python3
"""Builds packs/store from the ten industry packs.

The store pack is the "Maho Store" website on the maho/default theme: every product of every
industry, one category tree with one branch per industry, every review, and the home page that
links to the ten industry stores. Run it after any industry pack changes.

Usage: tools/build-store-pack.py
"""
import csv
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PACKS = os.path.join(ROOT, 'packs')
STORE = os.path.join(PACKS, 'store')
WEBSITE = 'base'
STORE_CODE = 'default'
ROOT_CATEGORY = 'Default Category'

INTRO = ('This store carries the full catalog of the ten Maho demo shops. Each shop is also a website of its own, with its own '
         'theme. Pick one below, or shop it all here.')


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


def industries():
    """(code, industry name) per industry website, in the sort order of stores.csv."""
    rows = [r for r in read(os.path.join(PACKS, '_shared', 'stores.csv')) if r['website_code'] != WEBSITE]
    rows.sort(key=lambda r: int(r['website_sort_order']))
    return [(r['website_code'], r['root_category']) for r in rows]


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
    return rows


def products(codes):
    """One row per product that adds the store website and the industry branch of its categories."""
    rows = []
    for code, name in codes:
        sku = None
        paths = {}
        for r in read(os.path.join(PACKS, code, 'products.csv')):
            if r['sku'] != '':
                sku = r['sku']
                paths.setdefault(sku, [])
            if sku is None or r.get('_store', '') != '':
                continue
            if r['_category'] != '':
                paths[sku].append(f"{name}/{r['_category']}")
        for sku, cats in paths.items():
            first = True
            for cat in cats or ['']:
                rows.append({'sku': sku if first else '', '_product_websites': WEBSITE if first else '',
                             '_root_category': ROOT_CATEGORY if cat else '', '_category': cat})
                first = False
    return rows


def reviews(codes):
    rows = []
    for code, name in codes:
        path = os.path.join(PACKS, code, 'reviews.csv')
        if not os.path.exists(path):
            continue
        for r in read(path):
            r['store_code'] = STORE_CODE
            rows.append(r)
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
FEATURES = [('building-store', 'One installation', 'Eleven websites, one admin.'),
            ('shopping-cart', 'Every product', 'The whole catalog, one cart.'),
            ('palette', 'Ten themes', 'Each shop has its own look.'),
            ('code', 'Open source', 'Maho is free software.')]
STARS = ' '.join(['{{icon name="star" variant="filled" size="18"}}'] * 5)


def store_names():
    return {r['website_code']: r['website_name'] for r in read(os.path.join(PACKS, '_shared', 'stores.csv'))}


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


def home(codes):
    names = store_names()
    intro = root_descriptions(codes)
    tiles = ''.join(f'''    <a class="hub-card" href="{{{{store url="" _store="{code}"}}}}">
        <img src="{{{{media url="wysiwyg/store/tile-{code}.webp"}}}}" alt="" />
        <span class="hub-card-name">{name}</span>
    </a>
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
''' for icon, title, text in FEATURES)
    sections = ''
    for index, (code, name) in enumerate(codes):
        title = SECTIONS[code][0]
        left = index % 2 == 0
        areas = "&#039;a b&#039; &#039;a c&#039;" if left else "&#039;b a&#039; &#039;c a&#039;"
        columns = '2fr 3fr' if left else '3fr 2fr'
        template = f'&#34;a b&#34; auto &#34;a c&#34; 1fr / {columns}' if left else f'&#34;b a&#34; auto &#34;c a&#34; 1fr / {columns}'
        sections += f'''<div data-preset="custom" data-areas="{areas}" data-columns="{columns}" data-rows="auto 1fr" data-gap="medium" data-style="none" data-type="maho-bento" style="grid-template: {template};">
    <div data-area="a" data-type="maho-bento-cell" style="grid-area: a;">
        <p><a href="{{{{store url="" _store="{code}"}}}}" title="Visit {names[code]}"><img src="{{{{media url="wysiwyg/store/section-{code}.webp"}}}}" alt="{names[code]}" /></a></p>
    </div>
    <div class="card card-border" data-area="b" data-type="maho-bento-cell" style="grid-area: b;">
        <div class="card-body">
            <p><span class="badge badge-primary">{name}</span></p>
            <h2>{title}</h2>
            <p>{intro[code]} {SECTIONS[code][2]}</p>
            <p><a class="btn btn-primary" href="{{{{store url="" _store="{code}"}}}}">Visit {names[code]}</a> <a class="btn btn-ghost" href="{{{{store url="{code}"}}}}">Shop {name.lower()} here</a></p>
        </div>
    </div>
    <div data-area="c" data-type="maho-bento-cell" style="grid-area: c;">
        {{{{widget type="catalog/product_widget_list" title="{name} picks" category_id="{{{{category_id:{ROOT_CATEGORY}/{code}}}}}" sort="position" only_in_stock="1" products_count="3" template="catalog/product/widget/list/content/list_grid.phtml"}}}}
    </div>
</div>
'''
    quote_html = ''.join(f'''    <div data-type="maho-column">
        <p>{STARS}</p>
        <blockquote>
            <p>{text}</p>
        </blockquote>
        <p><strong>{who}</strong><br />Verified buyer, {where}</p>
    </div>
''' for text, who, where in quotes(codes))
    return f'''<div data-preset="feature-left" data-areas="&#039;a b&#039; &#039;a c&#039;" data-columns="2fr 1fr" data-rows="auto auto" data-gap="medium" data-style="none" data-type="maho-bento" style="grid-template: &#34;a b&#34; auto &#34;a c&#34; auto / 2fr 1fr;">
    <div data-area="a" data-type="maho-bento-cell" style="grid-area: a;">
        <p><a href="#stores" title="Choose a store"><img src="{{{{media url="wysiwyg/store/hero-main.webp"}}}}" alt="Ten stores on one street" /></a></p>
    </div>
    <div class="card card-border" data-area="b" data-type="maho-bento-cell" style="grid-area: b;">
        <div class="card-body">
            <p><span class="badge badge-primary">Ten stores, one street</span></p>
            <h1>Everything from ten shops, in one basket</h1>
            <p>{INTRO}</p>
            <p><a class="btn btn-primary" href="#stores">Choose a store</a> <a class="btn btn-ghost" href="#new">New arrivals</a></p>
        </div>
    </div>
    <div data-area="c" data-type="maho-bento-cell" style="grid-area: c;">
        <p><a href="{{{{store url="" _store="food"}}}}" title="Visit {names['food']}"><img src="{{{{media url="wysiwyg/store/hero-side.webp"}}}}" alt="{names['food']}" /></a></p>
    </div>
</div>
<div data-preset="4-equal" data-gap="medium" data-style="separated" data-type="maho-columns">
{features}</div>
<h2 id="stores">Choose a store</h2>
<div class="hub">
    <div class="hub-grid">
{tiles}    </div>
</div>
{sections}<h2 id="new">New arrivals</h2>
{{{{widget type="catalog/product_widget_new" display_type="new_products" products_count="4" template="catalog/product/widget/new/content/new_grid.phtml"}}}}
<h2>What our customers say</h2>
<div data-preset="3-equal" data-gap="medium" data-style="cards" data-type="maho-columns">
{quote_html}</div>
<div class="card card-border">
    <div class="card-body">
        <h2 style="text-align: center;">Stay in the loop</h2>
        <p style="text-align: center;">One email a month with what is new across the ten stores. No noise.</p>
        {{{{widget type="newsletter/widget_subscribe" template="newsletter/subscribe.phtml"}}}}
    </div>
</div>
'''


ABOUT = '''<div data-type="maho-columns" data-preset="2-equal" data-gap="large" data-style="none">
    <div data-type="maho-column">
        <p><img src="{{media url="wysiwyg/store/about.webp"}}" alt="A row of small shop fronts on a sunny street"></p>
    </div>
    <div data-type="maho-column">
        <p><span class="badge badge-outline">About</span></p>
        <h2>One installation, eleven websites</h2>
        <p>The Maho Store is the front door of the Maho sample data. It runs on the default theme and sells the full catalog of the ten demo shops, from linen shirts to trail shoes to terracotta pots.</p>
        <p>Each of the ten shops is also a website of its own on the same installation, with its own theme, categories, content and reviews. Use the store switcher in the corner to jump between them.</p>
        <p>Every product, picture, review and article is generated demo data. Nothing here is for sale, and no order is processed.</p>
    </div>
</div>
'''

SERVICE = '''<h1>Customer Service</h1>
<h2>Shipping and delivery</h2>
<p>Orders placed before noon on a weekday ship the same day. Standard delivery takes two to four working days. Express delivery arrives the next working day. Plants, food and fragile items travel in their own packaging.</p>
<h2>Returns</h2>
<p>You can return an unused item within 30 days of delivery. Start the return from your account page and print the prepaid label. Refunds reach the original payment method within five working days of receipt. Food, plants and personalised jewelry cannot be returned.</p>
<h2>Payment</h2>
<p>We accept cards, PayPal and bank transfer. Every payment page is encrypted. We never store card numbers.</p>
<h2>Contact</h2>
<p>Write to us through the <a href="{{store url="contacts"}}">contact page</a>. We answer within one working day.</p>
'''

NO_ROUTE = '''<h1 style="text-align: center">Oops!</h1>
<p style="text-align: center"><strong>404 Page not found.</strong> Check the address, or head back to the <a href="{{store url=""}}">home page</a>.</p>
<h2 style="text-align: center">Were you looking for something else?</h2>
<p style="text-align: center">Here is what arrived this week.</p>
{{widget type="catalog/product_widget_new" display_type="new_products" products_count="5" template="catalog/product/widget/new/content/new_grid.phtml"}}
'''


PRIVACY = '''<p><span class="badge badge-warning">Demo store</span></p>
<p>This is a demonstration store. It exists to show what Maho can do, not to sell anything, and this page is a placeholder rather than a legal document.</p>
<h2>What this demo does with your data</h2>
<p>Nothing that lasts. The store runs on a test installation that is reset from time to time. Anything you type into a form here, an account, an address, a review, a newsletter sign up, is demo data. It is not read by a person, not shared with anyone, and it disappears with the next reset.</p>
<h2>Cookies</h2>
<p>The store sets the session and preference cookies that every Maho installation needs to keep a cart, a login or a store choice between two pages. There is no analytics, advertising or tracking cookie on this demo.</p>
<h2>Orders and payments</h2>
<p>No order placed here is processed, shipped or charged. Do not enter a real card number anywhere on this site.</p>
<h2>Your own store</h2>
<p>When you run Maho for real, replace this page with a privacy policy that describes what your store collects and why. The page lives under CMS pages in the admin, and the cookie notice below it comes from the cookie restriction setting.</p>
'''


DEMO_NOTICE = '''<p>Demo store. Orders are not processed. <a href="#switch-store">Switch store</a></p>
'''


def main():
    codes = industries()
    write(os.path.join(STORE, 'categories.csv'), categories(codes),
          ['root', 'path', 'name', 'is_active', 'include_in_menu', 'is_anchor', 'position', 'display_mode', 'landing_page', 'image', 'description', 'meta_title', 'meta_description'])
    write(os.path.join(STORE, 'products.csv'), products(codes), ['sku', '_product_websites', '_root_category', '_category'])
    write(os.path.join(STORE, 'reviews.csv'), reviews(codes), ['sku', 'store_code', 'nickname', 'title', 'detail', 'rating', 'created_at'])
    write(os.path.join(STORE, 'cms_pages.csv'),
          [dict(identifier='home', stores=STORE_CODE, title='Maho Store', root_template='one_column', content_file='home.html', is_active=1, is_home=1,
                meta_description='Ten demo stores on one Maho installation, one per industry theme, and every product in one store.'),
           dict(identifier='about-maho-demo-store', stores=STORE_CODE, title='About the Maho Store', root_template='one_column', content_file='about.html', is_active=1, is_home=0, meta_description=''),
           dict(identifier='customer-service', stores=STORE_CODE, title='Customer Service', root_template='one_column', content_file='customer-service.html', is_active=1, is_home=0, meta_description=''),
           dict(identifier='no-route', stores=STORE_CODE, title='404 Not Found', root_template='one_column', content_file='no-route.html', is_active=1, is_home=0, meta_description=''),
           dict(identifier='privacy-policy-cookie-restriction-mode', stores='', title='Privacy Policy', root_template='one_column', content_file='privacy-policy.html', is_active=1, is_home=0, meta_description='')],
          ['identifier', 'stores', 'title', 'root_template', 'content_file', 'is_active', 'is_home', 'meta_description'])
    write(os.path.join(STORE, 'cms_blocks.csv'),
          [dict(identifier='demo-notice', stores='', title='Demo notice', content_file='demo-notice.html', is_active=1)],
          ['identifier', 'stores', 'title', 'content_file', 'is_active'])
    os.makedirs(os.path.join(STORE, 'content'), exist_ok=True)
    for name, body in {'home.html': home(codes), 'about.html': ABOUT, 'customer-service.html': SERVICE, 'no-route.html': NO_ROUTE, 'privacy-policy.html': PRIVACY, 'demo-notice.html': DEMO_NOTICE}.items():
        with open(os.path.join(STORE, 'content', name), 'w') as f:
            f.write(body)
    print(f'store pack: {len(codes)} industries')


if __name__ == '__main__':
    main()
