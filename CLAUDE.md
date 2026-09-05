# CLAUDE.md

Sample data for Maho: eleven websites (a hub plus ten industry stores) on one installation, everything as CSV packs under `packs/`. Read `README.md` for the layout and the install order.

## Rules

- Every entity is CSV. Page and block bodies are HTML files under `packs/<store>/content/`. No SQL.
- Store, website, group and root category codes take the industry key (`fashion`, `food`, ...). The fashion website is the default website and serves the root URL. The hub website lists every store at /hub/.
- Products use the Maho Import/Export layout. `_root_category` on every product row. Children before the configurable parent. One axis per configurable.
- Scope everything by code, never by id. Config macros: `{{attribute_id:code}}`, `{{attribute_ids:a,b}}`, `{{category_id:Root/url-key}}`, `{{cms_block_id:identifier}}`, `{{store_id:code}}`.
- Pictures: `wavespeed-ai/krea-v2/turbo` on NanoGPT (0.010 USD per picture) for every tier, chosen in a bake-off against flux-2-klein-9b, z-image-turbo and microsoft/mai-image-2.5. Fallback: `flux-2-klein-9b`. Never `gpt-image-2`.
- Product pictures are cutouts on a transparent ground (`tools/cutout.sh`); the theme paints the tile.
- No real brands. Invented brand marks only.
- Never use em dashes in copy. Simple sentences.

## Check

`tools/validate.sh /path/to/maho` before a pull request. It must pass twice in a row (the second run is an update).
