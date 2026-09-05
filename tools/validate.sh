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
