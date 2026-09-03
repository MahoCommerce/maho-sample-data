INSERT INTO `core_config_data` (`scope`, `scope_id`, `path`, `value`, `updated_at`)
VALUES
    ('default', '0', 'configswatches/general/product_list_attribute', '94', NULL),
    ('default', '0', 'configswatches/general/swatch_attributes', '195,94,191,210,187,181', NULL),
    ('default', '0', 'configswatches/general/enabled', '1', NULL),
    ('default', '0', 'catalog/frontend/grid_per_page', '12', NULL),
    ('default', '0', 'catalog/frontend/grid_per_page_values', '12', NULL),
    ('default', '0', 'catalog/frontend/list_mode', 'grid', NULL),
    ('default', '0', 'catalog/advanced_search/enabled', '0', NULL),
    ('default', '0', 'catalog/recently_products/enabled_product_compare', '0', NULL),
    ('default', '0', 'catalog/recently_products/enabled_recently_viewed', '0', NULL),
    ('default', '0', 'catalog/frontend/enable_addtocart_in_product_listings', '0', NULL),
    ('default', '0', 'design/head/demonotice', '1', NULL),
    ('default', '0', 'design/head/includes', '<style>
body.cms-home .main-container { padding-top: 0 }
.cms-index-index .products-grid :is(.ratings, .actions),
.cms-index-noroute .products-grid :is(.ratings, .actions) { display: none }
.catblocks { display: grid; gap: 10px; padding-bottom: 20px }
@media (min-width: 480px) { .catblocks { grid-template-columns: repeat(2, 1fr) } }
@media (min-width: 771px) { .catblocks { grid-template-columns: repeat(4, 1fr) } }
body .catblocks li { position: relative; list-style: none; margin: 0; border: 1px solid var(--maho-color-border) }
.catblocks li:hover { border-color: var(--maho-color-primary) }
.catblocks li img { width: 100%; display: block }
.catblocks li a span { position: absolute; inset: auto 0 0; padding: 5px 10px; background: var(--maho-color-background-dark); color: var(--maho-color-background); font-weight: bold; text-transform: uppercase; text-align: center }
/* Brand marquee on the home page (see SECTIONS.md, recipe 11) */
.marquee { margin: 2.5rem 0; overflow: hidden; mask-image: linear-gradient(to right, transparent, black 8%, black 92%, transparent) }
.marquee-track { display: flex; width: max-content; align-items: center; animation: marquee 45s linear infinite }
.marquee-track > * { margin: 0; flex-shrink: 0 }
.marquee:hover .marquee-track { animation-play-state: paused }
@media (prefers-reduced-motion: reduce) { .marquee-track { animation: none } }
@keyframes marquee { to { transform: translateX(-50%) } }
</style>', NULL),
    ('default', '0', 'revocation/general/enabled', '1', NULL),
    ('stores', '2', 'general/locale/code', 'fr_FR', NULL),
    ('stores', '3', 'general/locale/code', 'de_DE', NULL);

INSERT INTO `core_config_data` (`scope`, `scope_id`, `path`, `value`, `updated_at`)
VALUES
    ('default', '0', 'general/store_information/name', 'Maison Maho', NULL),
    ('default', '0', 'design/head/default_title', 'Maison Maho', NULL),
    ('default', '0', 'design/header/logo_alt', 'Maison Maho', NULL),
    ('default', '0', 'design/footer/copyright', '&copy; Maison Maho. All rights reserved.', NULL),
    ('default', '0', 'trans_email/ident_general/name', 'Maison Maho', NULL),
    ('default', '0', 'trans_email/ident_sales/name', 'Maison Maho', NULL),
    ('default', '0', 'trans_email/ident_support/name', 'Maison Maho', NULL);

INSERT INTO `permission_block` (block_name, is_allowed)
VALUES
    ('cms/block', 1);