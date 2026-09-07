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
./maho sample-data:install --path "$HERE" --skip-reindex
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
