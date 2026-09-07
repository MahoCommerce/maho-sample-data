#!/bin/bash
# Installs the packs of this checkout into a Maho checkout with a fresh SQLite database, twice, and reindexes.
# Usage: tools/validate.sh /path/to/maho
set -e
MAHO="${1:?path to a Maho checkout}"
HERE="$(cd "$(dirname "$0")/.." && pwd)"
cd "$MAHO"
if [ -f app/etc/local.xml ]; then
  mv app/etc/local.xml app/etc/local.xml.validate-backup
  trap 'mv "$MAHO/app/etc/local.xml.validate-backup" "$MAHO/app/etc/local.xml"' EXIT
fi
DB="$MAHO/var/db/sample-data-validate.sqlite"
rm -f "$DB"
./maho install --license_agreement_accepted yes --locale en_US --timezone UTC --default_currency USD \
  --db_engine sqlite --db_name "$DB" --url http://localhost:8901/ --secure_base_url http://localhost:8901/ \
  --use_secure 0 --use_secure_admin 0 --admin_lastname admin --admin_firstname admin --admin_email admin@example.com \
  --admin_username admin --admin_password validate123456 --sample_data "$HERE"
./maho import:sample-data --path "$HERE" --skip-reindex
./maho index:reindex:all
./maho cache:flush

# The store view rows of packs/store/products.csv carry no sku: they belong to the last sku the
# importer read, and _saveProducts forgets that sku at the start of every 100 row bunch. The build
# keeps every product to the same row count so a bunch never cuts one in half. If that ever breaks,
# products lose their translation silently, so count the gaps here instead.
echo "checking the store view rows of every product"
gaps=$(sqlite3 "$DB" "
  with name as (select attribute_id from eav_attribute where attribute_code='name'
    and entity_type_id=(select entity_type_id from eav_entity_type where entity_type_code='catalog_product')),
  view as (select store_id from core_store where code in ('fr','de','it'))
  select count(*) from catalog_product_entity e, view v
  where exists (select 1 from catalog_product_entity_varchar d
                where d.entity_id=e.entity_id and d.store_id=0 and d.attribute_id=(select attribute_id from name))
    and not exists (select 1 from catalog_product_entity_varchar s
                where s.entity_id=e.entity_id and s.store_id=v.store_id and s.attribute_id=(select attribute_id from name));")
if [ "$gaps" != "0" ]; then
  echo "FAILED: $gaps product and store view pairs have no store scoped name" >&2
  exit 1
fi
echo "every product has a name on every store view"

# A row that carries no sku belongs to the last sku the importer read, and the importer forgets
# that sku at the start of every 100 row bunch. tools/build-pack.py keeps each product inside one
# bunch, but if that ever breaks a configurable silently loses a variant, so count them here.
echo "checking the variants and the members of every product"
python3 - "$HERE" "$DB" <<'PY'
import csv, glob, os, sqlite3, sys

here, db = sys.argv[1], sys.argv[2]
VARIANT = 'select c.sku from catalog_product_super_link l' \
    ' join catalog_product_entity p on p.entity_id = l.parent_id' \
    ' join catalog_product_entity c on c.entity_id = l.product_id where p.sku = ?'
MEMBER = 'select c.sku from catalog_product_link k' \
    ' join catalog_product_entity p on p.entity_id = k.product_id' \
    ' join catalog_product_entity c on c.entity_id = k.linked_product_id' \
    ' where k.link_type_id = 3 and p.sku = ?'

wanted = {}
for path in sorted(glob.glob(os.path.join(here, 'packs', '*', 'products.csv'))):
    sku = None
    for row in csv.DictReader(open(path)):
        sku = row['sku'] or sku
        for column, query in (('_super_products_sku', VARIANT), ('_associated_sku', MEMBER)):
            if row.get(column):
                wanted.setdefault((sku, query), set()).add(row[column])

db = sqlite3.connect(db)
gaps = []
for (sku, query), children in sorted(wanted.items()):
    have = {r[0] for r in db.execute(query, (sku,))}
    if children - have:
        gaps.append(f'{sku} is missing {", ".join(sorted(children - have))}')
if gaps:
    print('FAILED: ' + '\n        '.join(gaps), file=sys.stderr)
    raise SystemExit(1)
print(f'every one of the {len(wanted)} configurable and grouped products kept all its children')
PY
