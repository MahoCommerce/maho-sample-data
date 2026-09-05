#!/usr/bin/env python3
"""Builds packs/store from the ten industry packs.

The store pack is the "Maho Store" website on the maho/default theme: every product of every
industry, one category tree with one branch per industry, every review, and the home page that
links to the ten industry stores. Run it after any industry pack changes.

Usage: tools/build-store-pack.py
"""
import csv
import os
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PACKS = os.path.join(ROOT, 'packs')
STORE = os.path.join(PACKS, 'store')
WEBSITE = 'base'
STORE_CODE = 'default'
ROOT_CATEGORY = 'Default Category'

INTRO = ('This is the sample data of Maho, the open source ecommerce platform. This store runs on the default theme and '
         'sells the full catalog of the ten shops below. Each shop is a website of the same installation, with its own '
         'industry theme, catalog and content. Choose one to see how Maho looks and works in that industry.')
NOTE = 'All products, pictures and content are generated demo data. Orders placed in these stores are not processed.'


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
    for position, (code, name) in enumerate(codes, 1):
        tile = os.path.join(ROOT, 'media', 'wysiwyg', 'store', f'tile-{code}.webp')
        image = ''
        if os.path.exists(tile):
            image = f'store-{code}.webp'
            os.makedirs(os.path.join(STORE, 'media', 'catalog', 'category'), exist_ok=True)
            shutil.copyfile(tile, os.path.join(STORE, 'media', 'catalog', 'category', image))
        rows.append(dict(root=ROOT_CATEGORY, path=code, name=name, is_active=1, include_in_menu=1, is_anchor=1,
                         position=position, display_mode='PRODUCTS', image=image))
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


def home(codes):
    tiles = ''.join(f'''    <a class="hub-card" href="{{{{store url="" _store="{code}"}}}}">
        <img src="{{{{media url="wysiwyg/store/tile-{code}.webp"}}}}" alt="" />
        <span class="hub-card-name">{name}</span>
    </a>
''' for code, name in codes)
    return f'''<div class="hub">
    <div class="hub-hero">
        <img src="{{{{media url="wysiwyg/store/hero.webp"}}}}" alt="" />
        <p>{INTRO}</p>
    </div>
    <div class="hub-grid">
{tiles}    </div>
    <p class="hub-note">{NOTE}</p>
</div>
'''


def main():
    codes = industries()
    write(os.path.join(STORE, 'categories.csv'), categories(codes),
          ['root', 'path', 'name', 'is_active', 'include_in_menu', 'is_anchor', 'position', 'display_mode', 'landing_page', 'image', 'description', 'meta_title', 'meta_description'])
    write(os.path.join(STORE, 'products.csv'), products(codes), ['sku', '_product_websites', '_root_category', '_category'])
    write(os.path.join(STORE, 'reviews.csv'), reviews(codes), ['sku', 'store_code', 'nickname', 'title', 'detail', 'rating', 'created_at'])
    write(os.path.join(STORE, 'cms_pages.csv'),
          [dict(identifier='home', stores=STORE_CODE, title='Maho Store', root_template='one_column', content_file='home.html', is_active=1, is_home=1,
                meta_description='Ten demo stores on one Maho installation, one per industry theme, and every product in one store.')],
          ['identifier', 'stores', 'title', 'root_template', 'content_file', 'is_active', 'is_home', 'meta_description'])
    os.makedirs(os.path.join(STORE, 'content'), exist_ok=True)
    with open(os.path.join(STORE, 'content', 'home.html'), 'w') as f:
        f.write(home(codes))
    print(f'store pack: {len(codes)} industries')


if __name__ == '__main__':
    main()
