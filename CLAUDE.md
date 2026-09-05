# CLAUDE.md

Sample data for Maho: eleven websites on one installation, everything as CSV packs under `packs/`. Website 1 is the Maho Store on the maho/default theme, with every product of every industry, and serves the root URL. The ten industry stores follow, one per storefront theme. Read `README.md` for the layout and the install order.

## Rules

- Reviews carry one vote on the single rating `Rating` (`packs/_shared/ratings.csv` hides the distro ratings Quality, Value and Price from every store). The product list shows no per-page selector: `catalog/frontend/grid_per_page_values` holds one value.
- Every storefront carries the demo store button (a `details` element in `design/footer/absolute_footer`, styled by `design/tokens/custom_css`, both at default scope). Its links use the `{{store_url:code}}` macro.
- Every entity is CSV. Page and block bodies are HTML files under `packs/<store>/content/`. No SQL.
- Website 1 keeps the distro codes (`base`, `default`, root `Default Category`). The industry stores take the industry key for the website, group, store and root category (`fashion`, `food`, ...).
- `packs/store` is generated: `tools/build-store-pack.py` reads the ten industry packs and writes the category tree (one branch per industry), the website and category rows of every product, every review, and the home page that links to the ten stores. Run it after any industry pack change. Only `images.json` in it is hand written.
- Products use the Maho Import/Export layout. `_root_category` on every product row. Children before the configurable parent. One axis per configurable.
- Scope everything by code, never by id. Config macros: `{{attribute_id:code}}`, `{{attribute_ids:a,b}}`, `{{category_id:Root/url-key}}`, `{{cms_block_id:identifier}}`, `{{store_id:code}}`.
- Pictures: product cutouts use `wavespeed-ai/krea-v2/turbo` on NanoGPT (0.010 USD per picture), chosen in a bake-off against flux-2-klein-9b, z-image-turbo and microsoft/mai-image-2.5. Fallback: `flux-2-klein-9b`. Every home page picture (hero, editorial, gallery, banners, tiles, about, blog) and the store pack use `gpt-image-2` (0.05 to 0.07 USD per picture). Category banners use `ideogram-v3-turbo` at 1536x512 for a true 3:1.
- A manifest entry carries its own `style` for scene pictures (`SCENE_STYLE` from the spec). The manifest `style` is the product studio style and must never reach a scene prompt: the model then renders a scene and a cutout side by side.
- gpt-image-2 renders 1:1, 3:2, 16:9 and their portrait forms. Ask for one of those sizes and set `ratio` to the shape you need. The generator crops to the ratio from the centre.
- Every industry home page follows the Fashion page: hero bento, feature strip, category tiles, new arrivals, story, promo, three quotes, a five picture gallery bento (`GALLERY` in the spec), blog posts, newsletter, the brand marquee (`BRANDS` in the spec, text logos written as SVG by the builder) and two category banners.
- Product pictures are cutouts on a transparent ground (`tools/cutout.sh`); the theme paints the tile.
- No real brands. Invented brand marks only.
- Never use em dashes in copy. Simple sentences.

## Check

`tools/validate.sh /path/to/maho` before a pull request. It must pass twice in a row (the second run is an update).
- Each industry store has its own SVG wordmark in `media/wysiwyg/<code>/logo.svg`, written by `tools/build-logos.py` (run it with `tools/.venv/bin/python`, a venv with fonttools, brotli and uharfbuzz). The mark uses the display font and the primary colour of the theme, with the text shaped by HarfBuzz and converted to paths, so no font loads at runtime. `design/header/logo_src` points at it per website; the Maho Store keeps the Maho logo.
