# Maho Sample Data

Demo content for [Maho](https://mahocommerce.com): one hub website plus ten industry stores, one per storefront theme, on a single installation. Every entity is a CSV file, with page bodies in HTML files and pictures next to them.

`./maho install --sample_data 1` downloads the branch that matches the Maho version and imports it. `./maho sample-data:install --path /path/to/this/checkout` imports a local checkout, and `--pack fashion,food` limits the run to some packs. Every import is idempotent: run it again and it updates instead of duplicating.

## Layout

```
packs/_shared/   stores.csv, attribute_sets.csv, attributes.csv, attribute_options.csv, config.csv, customers.csv
packs/hub/       the landing website that lists every store, at /hub/: cms_pages.csv, content/, images.json
packs/<store>/   categories.csv, products.csv, reviews.csv, cms_blocks.csv, cms_pages.csv, blog_posts.csv,
                 content/*.html, media/import/ (product pictures), media/catalog/category/, images.json
media/           wysiwyg/<store>/, wysiwyg/swatches/, blog/<store>/ (copied to public/media as is)
tools/           generate-images.mjs, cutout.sh, validate.sh
```

The install order is fixed: shared stores, attribute sets, attributes with options, config, media copy, then each pack (blocks, categories, products, reviews, pages, blog posts), then customers, reindex and cache flush.

## CSV contracts

The column lists live in the Maho importers under `lib/Maho/Import/Importer/`. Products and customers use the Import/Export layout with two rules: `_root_category` is required on every product row that sets `_category`, and `_media_attribute_id` must not be present. Picture paths in `products.csv` are relative to the pack's `media/import/` folder.

## Pictures

`tools/generate-images.mjs --manifest packs/<store>/images.json` generates the pictures of a manifest through the NanoGPT API (`NANOGPT_API_KEY`), then `tools/cutout.sh packs/<store>/media/import` removes the backgrounds with a local rembg. Existing files are skipped, so a manifest can grow.

## Check a change

`tools/validate.sh /path/to/maho` installs a fresh SQLite Maho with this checkout, runs the import a second time, and reindexes.
