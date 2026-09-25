#!/usr/bin/env python3
"""Builds the store activity of every pack: orders.csv, product_views.csv and search_terms.csv.

The admin dashboard shows the orders, the bestsellers, the best customers, the most viewed products
and the search terms of the store. This tool gives it a year of that activity. A date in these files
is an age: hours_ago counts back from the moment of the import, so the dashboard of a fresh install
always shows the last day, the last week and the last year.

The orders of an industry store sell the products of its pack. The orders of the Maho Store sell
every product, on its four store views. The buyers are the customers of packs/_shared/customers.csv
and guests. The random seed is fixed, so the files only change when the catalog or the customers do.
Run it after any change to the products or the customers, and after tools/build-store-pack.py.

Usage: tools/build-activity.py
"""
import collections
import csv
import os
import random
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PACKS = os.path.join(ROOT, 'packs')
STORE = 'store'
SEED = 2611
DAYS = 365
# Orders per pack. The Maho Store sells every product, so it gets more.
ORDERS = {STORE: 100}
ORDERS_PER_INDUSTRY = 20
# Orders less than one day old, so the default 24 hour view of the dashboard is not empty.
RECENT = {STORE: 3}
RECENT_PER_INDUSTRY = 1
# The store views of the Maho Store and their share of its orders, views and searches.
STORE_VIEWS = {'default': 0.7, 'default-fr': 0.1, 'default-de': 0.1, 'default-it': 0.1}
LANGUAGE = {'default': 'en', 'default-fr': 'fr', 'default-de': 'de', 'default-it': 'it'}
COUNTRY = {'en': 'US', 'fr': 'FR', 'de': 'DE', 'it': 'IT'}
# A product needs this much stock to be sold, because an order takes up to three.
MIN_QTY = 5
REGISTERED_SHARE = 0.6
VIEW_DAYS = 30
SEARCH_HOURS = 30 * 24

GUEST_NAMES = {
    'en': ['Alex Morgan', 'Jordan Hayes', 'Casey Porter', 'Riley Chen', 'Morgan Ellis', 'Taylor Brooks',
           'Jamie Foster', 'Avery Collins', 'Quinn Harper', 'Drew Sandoval', 'Skyler Price', 'Reese Walker',
           'Cameron Lowe', 'Harper Diaz', 'Rowan Pierce', 'Emerson Shaw', 'Finley Ward', 'Parker Bishop'],
    'fr': ['Chloé Bernard', 'Lucas Petit', 'Manon Dubois', 'Théo Laurent', 'Inès Roux', 'Nathan Fournier'],
    'de': ['Hannah Weber', 'Leon Meyer', 'Emma Schulz', 'Noah Koch', 'Sophie Richter', 'Elias Wolf'],
    'it': ['Sofia Conti', 'Matteo Greco', 'Aurora Marino', 'Lorenzo Gallo', 'Alice Costa', 'Tommaso Fontana'],
}
# Street, city, region, postcode and telephone of invented addresses. The region is the default
# name of a directory region, because the countries of these stores need one (general/region/state_required).
ADDRESSES = {
    'US': [('1450 Birch Street', 'Austin', 'Texas', '78704', '555-0140'),
           ('88 Harbor View', 'Seattle', 'Washington', '98109', '555-0141'),
           ('300 Wabash Avenue', 'Chicago', 'Illinois', '60611', '555-0142'),
           ('17 Commonwealth Avenue', 'Boston', 'Massachusetts', '02116', '555-0143'),
           ('742 Sunset Boulevard', 'Los Angeles', 'California', '90028', '555-0144'),
           ('29 Larimer Street', 'Denver', 'Colorado', '80205', '555-0145'),
           ('510 Hudson Street', 'New York', 'New York', '10014', '555-0146'),
           ('65 Ponce de Leon Avenue', 'Atlanta', 'Georgia', '30308', '555-0147'),
           ('1200 Broadway', 'Nashville', 'Tennessee', '37203', '555-0148'),
           ('410 Hawthorne Boulevard', 'Portland', 'Oregon', '97214', '555-0149')],
    'FR': [('3 rue des Martyrs', 'Paris', 'Paris', '75009', '01 45 00 56 78'),
           ('17 rue Mercière', 'Lyon', 'Rhône', '69002', '04 72 00 11 22'),
           ('40 rue Sainte-Catherine', 'Bordeaux', 'Gironde', '33000', '05 56 00 33 44')],
    'DE': [('Kastanienallee 24', 'Berlin', 'Berlin', '10435', '030 5550211'),
           ('Leopoldstraße 58', 'München', 'Bayern', '80802', '089 5550233'),
           ('Ottenser Hauptstraße 6', 'Hamburg', 'Hamburg', '22765', '040 5550255')],
    'IT': [('Corso Buenos Aires 12', 'Milano', '', '20124', '02 5550 6789'),
           ('Via del Governo Vecchio 5', 'Roma', '', '00186', '06 5550 7890'),
           ('Via Santo Stefano 22', 'Bologna', '', '40125', '051 5550 8901')],
}
# Words that are too common in product names to be a search term.
STOPWORDS = {
    'with', 'from', 'pack', 'set', 'avec', 'pour', 'dans', 'sans', 'mit', 'und', 'für', 'aus',
    'ohne', 'della', 'delle', 'dello', 'degli', 'con', 'per', 'senza',
}
ORDER_COLUMNS = ['reference', 'store_code', 'hours_ago', 'status', 'email', 'firstname', 'lastname', 'street',
                 'city', 'region', 'postcode', 'country_id', 'telephone', 'items']
VIEW_COLUMNS = ['sku', 'store_code', 'views', 'days']
SEARCH_COLUMNS = ['store_code', 'query_text', 'popularity', 'num_results', 'hours_ago']


def read(path):
    with open(path, newline='') as f:
        return list(csv.DictReader(f))


def write(path, rows, columns):
    with open(path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=columns, lineterminator='\n', extrasaction='ignore')
        w.writeheader()
        w.writerows(rows)


def industries():
    return sorted(d for d in os.listdir(PACKS) if not d.startswith(('_', '.')) and d != STORE
                  and os.path.isfile(os.path.join(PACKS, d, 'products.csv')))


def catalog(pack):
    """The products of an industry pack: the rows that carry a sku, with the children of each
    configurable and the categories of each product."""
    products, current = {}, None
    for row in read(os.path.join(PACKS, pack, 'products.csv')):
        if row['sku']:
            current = dict(row, children=[], categories=[])
            products[row['sku']] = current
        if row.get('_super_products_sku'):
            current['children'].append(row['_super_products_sku'])
        if row.get('_category'):
            current['categories'].append(row['_category'])
    return products


def sellable(products):
    """The things a buyer picks, each a list of the skus an order line can carry: a product on its
    own, or the variants of a configurable. A variant goes in through its parent on import."""
    def orderable(p):
        return (p['_type'] in ('simple', 'virtual') and p['status'] == '1' and p['is_in_stock'] == '1'
                and float(p['qty'] or 0) >= MIN_QTY)
    units = []
    for sku, p in products.items():
        if p['visibility'] == '1' or p['status'] != '1':
            continue
        if p['_type'] == 'configurable':
            skus = [c for c in p['children'] if c in products and orderable(products[c])]
        elif orderable(p):
            skus = [sku]
        else:
            continue
        if skus:
            units.append((sku, skus))
    return units


def weighted(rng, units, exponent):
    """Weights that fall with a random rank, so a few products lead and many follow."""
    order = list(range(len(units)))
    rng.shuffle(order)
    weights = [0.0] * len(units)
    for rank, index in enumerate(order):
        weights[index] = 1 / (rank + 1) ** exponent
    return weights


def ages(rng, count, recent):
    """Ages in hours, most of them in the last months, with a rise over the year and two sales."""
    days = list(range(DAYS))
    weights = [(0.35 + 0.65 * (1 - d / DAYS)) * (3 if abs(d - 45) < 3 or abs(d - 210) < 3 else 1) for d in days]
    hours = [d * 24 + rng.randrange(24) for d in rng.choices(days, weights, k=count - recent)]
    hours += [rng.randrange(24) for _ in range(recent)]
    return sorted(hours, reverse=True)


def status(rng, hours):
    if hours < 48:
        return rng.choices(['pending', 'processing', 'canceled'], [35, 60, 5])[0]
    if hours < 7 * 24:
        return rng.choices(['processing', 'complete', 'canceled'], [40, 55, 5])[0]
    return rng.choices(['complete', 'processing', 'canceled', 'closed', 'pending'], [86, 2, 6, 5, 1])[0]


def customers():
    rows = read(os.path.join(PACKS, '_shared', 'customers.csv'))
    for row in rows:
        row['loyalty'] = 1
    return rows


def buyers_for(view, people):
    """The registered customers who shop in a store view, with a weight: the customers of that store
    first, then the English customers of the other stores, since an account works in every store."""
    language = LANGUAGE.get(view, 'en')
    pool = []
    for person in people:
        home = person['_store'] == view
        country = person['_address_country_id'] or 'US'
        if home:
            pool.append((person, 4 * person['loyalty']))
        elif language == 'en' and country == 'US':
            pool.append((person, person['loyalty']))
    return pool


def address_of(rng, person, country):
    if person.get('_address_street'):
        return {'street': person['_address_street'], 'city': person['_address_city'],
                'region': person['_address_region'], 'postcode': person['_address_postcode'],
                'country_id': person['_address_country_id'], 'telephone': person['_address_telephone']}
    street, city, region, postcode, telephone = rng.choice(ADDRESSES[country])
    return {'street': street, 'city': city, 'region': region, 'postcode': postcode,
            'country_id': country, 'telephone': telephone}


def orders(rng, pack, views, units, weights, people, count, recent):
    rows = []
    buyers = {view: buyers_for(view, people) for view in views}
    for number, hours in enumerate(ages(rng, count, recent), start=1):
        view = rng.choices(list(views), list(views.values()))[0]
        language = LANGUAGE.get(view, 'en')
        country = COUNTRY[language]
        if buyers[view] and rng.random() < REGISTERED_SHARE:
            pool = buyers[view]
            person = rng.choices([p for p, _ in pool], [w for _, w in pool])[0]
            first, last, email = person['firstname'], person['lastname'], person['email']
            address = address_of(rng, person, country)
        else:
            first, last = rng.choice(GUEST_NAMES[language]).split(' ', 1)
            email = f'{ascii_name(first)}.{ascii_name(last)}{rng.randrange(10, 99)}@example.org'
            address = address_of(rng, {}, country)
        lines = min(rng.choices([1, 2, 3, 4], [50, 30, 15, 5])[0], len(units))
        picked = []
        while len(picked) < lines:
            unit = rng.choices(units, weights)[0]
            if unit not in picked:
                picked.append(unit)
        items = [f'{rng.choice(skus)}:{rng.choices([1, 2, 3], [75, 20, 5])[0]}' for _, skus in picked]
        rows.append(dict(address, reference=f'{pack}-{number:04d}', store_code=view, hours_ago=hours,
                         status=status(rng, hours), email=email, firstname=first, lastname=last,
                         items='|'.join(items)))
    return rows


def ascii_name(name):
    table = str.maketrans({'é': 'e', 'è': 'e', 'ë': 'e', 'ö': 'o', 'ü': 'u', 'ä': 'a', 'ç': 'c', 'ï': 'i'})
    return re.sub(r'[^a-z]', '', name.lower().translate(table))


def product_views(rng, views, units, weights, scale):
    """A view count per product and store view, higher for the products that sell."""
    rows = []
    ranked = sorted(range(len(units)), key=lambda i: -weights[i] * rng.uniform(0.5, 1.5))
    for view, share in views.items():
        for rank, index in enumerate(ranked):
            count = round(scale * share / (rank + 1) ** 0.7 * rng.uniform(0.8, 1.2))
            if count >= 3:
                rows.append({'sku': units[index][0], 'store_code': view, 'views': count, 'days': VIEW_DAYS})
    return rows


def words(text):
    return [w for w in re.findall(r'[^\W\d_]+', text.casefold()) if len(w) >= 4 and w not in STOPWORDS]


def search_terms(rng, view, share, products, names, category_names):
    """Terms from the product names and the category names of a store view, in its language, with
    the number of products they find. A few misspelled terms find nothing."""
    texts = {}
    for sku, p in products.items():
        if p['status'] != '1' or p['visibility'] not in ('3', '4'):
            continue
        cats = ' '.join(category_names.get(c, c) for path in p['categories'] for c in path.split('/'))
        texts[sku] = (names.get(sku, p['name']) + ' ' + cats).casefold()
    counted = collections.Counter(w for sku in texts for w in set(words(names.get(sku, products[sku]['name']))))
    terms = [w for w, n in counted.most_common() if n >= 2][:14]
    for name in sorted(set(category_names.values())):
        term = name.casefold()
        if '&' not in term and len(term.split()) <= 2 and term not in terms and len(terms) < 20:
            terms.append(term)
    # A small catalog repeats few words, so fill up with words of single product names.
    single = sorted(w for w, n in counted.items() if n == 1 and w not in terms)
    terms += rng.sample(single, max(0, min(16 - len(terms), len(single))))
    found = {t: sum(all(w in text for w in t.split()) for text in texts.values()) for t in terms}
    terms = [t for t in terms if found[t] > 0]
    rng.shuffle(terms)
    rows = []
    for rank, term in enumerate(terms):
        rows.append({'query_text': term, 'num_results': found[term],
                     'popularity': max(2, round(120 * max(share, 0.35) / (rank + 1) ** 0.8 * rng.uniform(0.8, 1.2)))})
    long = [t for t in terms if len(t) >= 5]
    for term in rng.sample(long, min(3, len(long))):
        i = rng.randrange(1, len(term) - 2)
        wrong = term[:i] + term[i + 1] + term[i] + term[i + 2:]
        if wrong not in found:
            rows.append({'query_text': wrong, 'num_results': 0, 'popularity': rng.randint(2, 6)})
    for index, row in enumerate(rows):
        row['store_code'] = view
        row['hours_ago'] = rng.randrange(24) if index < 3 else rng.randrange(SEARCH_HOURS)
    return rows


def store_texts():
    """The names of the products and the categories of the Maho Store in each language."""
    names = {language: {} for language in LANGUAGE.values()}
    sku = None
    for row in read(os.path.join(PACKS, STORE, 'products.csv')):
        sku = row['sku'] or sku
        if row['name']:
            names[LANGUAGE.get(row['_store'] or 'default', 'en')][sku] = row['name']
    categories = {language: {} for language in LANGUAGE.values()}
    english = {}
    for row in read(os.path.join(PACKS, STORE, 'categories.csv')):
        key = (row['root'], row['path'])
        if not row['store_code']:
            english[key] = row['name']
        elif key in english:
            categories[LANGUAGE[row['store_code']]][english[key]] = row['name']
    return names, categories


def main():
    rng = random.Random(SEED)
    people = customers()
    # A few customers come back again and again, so the Customers tab has clear leaders.
    for person in rng.sample(people, 8):
        person['loyalty'] = rng.choice([4, 6, 8])
    all_products, all_units, all_weights = {}, [], []
    total = collections.Counter()
    for index, pack in enumerate(industries()):
        products = catalog(pack)
        units = sellable(products)
        weights = weighted(rng, units, 1.1)
        all_products.update(products)
        all_units += units
        all_weights += weights
        views = {pack: 1.0}
        category_names = {r['name']: r['name'] for r in read(os.path.join(PACKS, pack, 'categories.csv'))}
        recent = RECENT_PER_INDUSTRY if index % 2 == 0 else 0
        emit(pack, orders(rng, pack, views, units, weights, people, ORDERS.get(pack, ORDERS_PER_INDUSTRY), recent),
             product_views(rng, views, units, weights, 120),
             search_terms(rng, pack, 1.0, products, {}, category_names), total)
    names, categories = store_texts()
    terms = []
    for view, share in STORE_VIEWS.items():
        language = LANGUAGE[view]
        category_names = {c: categories[language].get(c, c) for p in all_products.values()
                          for path in p['categories'] for c in path.split('/')}
        terms += search_terms(rng, view, share, all_products, names[language], category_names)
    emit(STORE, orders(rng, STORE, STORE_VIEWS, all_units, all_weights, people, ORDERS[STORE], RECENT[STORE]),
         product_views(rng, STORE_VIEWS, all_units, all_weights, 300), terms, total)
    print(f'total: {total["orders"]} orders, {total["views"]} product views, {total["terms"]} search terms')


def emit(pack, order_rows, view_rows, term_rows, total):
    folder = os.path.join(PACKS, pack)
    write(os.path.join(folder, 'orders.csv'), order_rows, ORDER_COLUMNS)
    write(os.path.join(folder, 'product_views.csv'), view_rows, VIEW_COLUMNS)
    write(os.path.join(folder, 'search_terms.csv'), term_rows, SEARCH_COLUMNS)
    views = sum(r['views'] for r in view_rows)
    states = collections.Counter(r['status'] for r in order_rows)
    total.update(orders=len(order_rows), views=views, terms=len(term_rows))
    print(f'{pack}: {len(order_rows)} orders ({", ".join(f"{n} {s}" for s, n in states.most_common())}), '
          f'{views} views of {len(view_rows)} products, {len(term_rows)} search terms')


if __name__ == '__main__':
    main()
