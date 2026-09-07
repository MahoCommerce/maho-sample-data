"""The store view text of the Maho Store website.

packs/store carries the catalog of every industry on four store views: English, French, German and
Italian. tools/build-store-pack.py asks table() for one language and writes a store scoped row for
every string it finds. A string with no translation stays in English, and the build prints how many
are still missing.

The text lives next to the thing it names: every spec carries its French, German and Italian words
inside the category, the product and the review themselves, as {'en': ..., 'fr': ..., 'de': ...,
'it': ...}. specs/fashion.py is the exception, a flat TEXTS list, because the Fashion pack is hand
written and has no spec. This file walks all of them and adds the root of the store tree, which
belongs to no store. The 'en' value must match the English text character for character.
"""
import importlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# The stores of packs/store, in the order of packs/_shared/stores.csv.
STORES = ('fashion', 'electronics', 'food', 'books', 'jewelry', 'beauty', 'home', 'sports', 'kids', 'garden')
LANGUAGES = ('fr', 'de', 'it')

# The root of the store tree, which belongs to no store.
STORE = [
    {'en': 'Default Category', 'fr': 'Catégorie par défaut', 'de': 'Standardkategorie', 'it': 'Categoria predefinita'},
    {'en': 'Every product of the ten Maho demo stores, on the default theme.',
     'fr': 'Tous les produits des dix boutiques de démonstration Maho, sur le thème par défaut.',
     'de': 'Jedes Produkt der zehn Maho-Demoshops, auf dem Standard-Theme.',
     'it': 'Ogni prodotto dei dieci negozi dimostrativi Maho, sul tema predefinito.'},
]


def collect(value, out):
    """Every language dictionary inside a spec value, keyed by its English string."""
    if isinstance(value, dict) and 'en' in value:
        out[value['en']] = value
    elif isinstance(value, dict):
        for item in value.values():
            collect(item, out)
    elif isinstance(value, (list, tuple)):
        for item in value:
            collect(item, out)


def table(language):
    """english -> text, for one language. A string with no word in that language is left out."""
    out = {}
    collect(STORE, out)
    for store in STORES:
        module = importlib.import_module(store)
        for name in ('ROOT', 'ROOT_DESCRIPTION', 'CATEGORIES', 'REVIEWS', 'PRODUCTS', 'TEXTS'):
            collect(getattr(module, name, None), out)
    return {english: words[language] for english, words in out.items() if language in words}
