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
.promos { display: grid; gap: 20px; padding: 0; margin: 0 0 10px }
@media (min-width: 771px) { .promos { grid-template-columns: repeat(3, 1fr) } }
body .promos > li { list-style: none; margin: 0; user-select: none }
.promos img { width: 100% }
.promos a:hover { opacity: 0.8 }
.cms-index-index .products-grid :is(.ratings, .actions),
.cms-index-noroute .products-grid :is(.ratings, .actions) { display: none }
.cms-index-index h2.subtitle { padding: 6px 0; text-align: center; color: var(--maho-color-primary); font-weight: 600; border-block: 1px solid var(--maho-color-border) }
.cms-index-noroute h2.subtitle { display: none }
.catblocks { display: grid; gap: 10px; padding-bottom: 20px }
@media (min-width: 480px) { .catblocks { grid-template-columns: repeat(2, 1fr) } }
@media (min-width: 771px) { .catblocks { grid-template-columns: repeat(4, 1fr) } }
body .catblocks li { position: relative; list-style: none; margin: 0; border: 1px solid var(--maho-color-border) }
.catblocks li:hover { border-color: var(--maho-color-primary) }
.catblocks li img { width: 100%; display: block }
.catblocks li a span { position: absolute; inset: auto 0 0; padding: 5px 10px; background: var(--maho-color-background-dark); color: var(--maho-color-background); font-weight: bold; text-transform: uppercase; text-align: center }
.slideshow { max-height: 400px }
.slideshow ul li { width: 100%; height: 400px }
.slideshow ul li a { display: block; width: 100%; height: 100% }
</style>', NULL);

INSERT INTO `permission_block` (block_name, is_allowed)
VALUES
    ('cms/block', 1);