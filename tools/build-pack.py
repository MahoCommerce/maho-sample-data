#!/usr/bin/env python3
# Writes the CSV files, the HTML bodies and the picture manifest of one pack from a spec module.
# Usage: python3 tools/build-pack.py specs/food.py
# The CSV files are the source of truth once written; the spec is kept so a pack can be rebuilt.
import csv, json, os, random, re, sys, importlib.util

def slug(s):
    return re.sub(r'-+', '-', ''.join(c if c.isalnum() else '-' for c in s.lower())).strip('-')

def load_spec(path):
    spec = importlib.util.spec_from_file_location('spec', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def write_csv(path, rows, header):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=header, lineterminator='\n', extrasaction='ignore')
        w.writeheader(); w.writerows(rows)

def put(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w').write(text.rstrip() + '\n')

BANNER = ' A very wide, low banner: the subject spread across the whole width, nothing important near the top or bottom edge.'
STARS = ' '.join(['{{icon name="star" variant="filled" size="18"}}'] * 5)

def home_html(S):
    c = S.CODE; cats = S.CATEGORIES
    tiles = ''.join(f'''    <div data-type="maho-column">
        <p><a href="{{{{store url="{cat['path']}"}}}}" title="Shop {cat['name']}"><img src="{{{{media url="wysiwyg/{c}/tile-{slug(cat['path'])}.webp"}}}}" alt="{cat['name']}" /></a></p>
        <p style="text-align: center;">{{{{widget type="catalog/category_widget_link" id_path="category/{{{{category_id:{S.ROOT}/{cat['path']}}}}}" template="catalog/category/widget/link/link_block.phtml"}}}}</p>
    </div>
''' for cat in cats[:4])
    features = ''.join(f'''    <div data-type="maho-column">
        <p>{{{{icon name="{icon}" size="32"}}}}</p>
        <p><strong>{title}</strong><br />{text}</p>
    </div>
''' for icon, title, text in S.FEATURES)
    quotes = ''.join(f'''    <div data-type="maho-column">
        <p>{STARS}</p>
        <blockquote>
            <p>{text}</p>
        </blockquote>
        <p><strong>{who}</strong><br />Verified buyer, {where}</p>
    </div>
''' for text, who, where in S.TESTIMONIALS)
    return f'''<div data-preset="feature-left" data-areas="&#039;a b&#039; &#039;a c&#039;" data-columns="2fr 1fr" data-rows="1fr 1fr" data-gap="medium" data-style="none" data-type="maho-bento" style="grid-template: &#34;a b&#34; 1fr &#34;a c&#34; 1fr / 2fr 1fr;">
    <div data-area="a" data-type="maho-bento-cell" style="grid-area: a;">
        <p><a href="{{{{store url="{cats[0]['path']}"}}}}" title="{S.HERO['title']}"><img src="{{{{media url="wysiwyg/{c}/hero-main.webp"}}}}" alt="{S.HERO['title']}" /></a></p>
    </div>
    <div class="card card-border" data-area="b" data-type="maho-bento-cell" style="grid-area: b;">
        <div class="card-body">
            <p><span class="badge badge-primary">{S.HERO['badge']}</span></p>
            <h1>{S.HERO['title']}</h1>
            <p>{S.HERO['text']}</p>
            <p><a class="btn btn-primary" href="{{{{store url="{cats[0]['path']}"}}}}">Shop {cats[0]['name']}</a> <a class="btn btn-ghost" href="{{{{store url="{cats[1]['path']}"}}}}">Shop {cats[1]['name']}</a></p>
        </div>
    </div>
    <div data-area="c" data-type="maho-bento-cell" style="grid-area: c;">
        <p><a href="{{{{store url="{cats[2]['path']}"}}}}" title="Shop {cats[2]['name']}"><img src="{{{{media url="wysiwyg/{c}/hero-side.webp"}}}}" alt="Shop {cats[2]['name']}" /></a></p>
    </div>
</div>
<div data-preset="4-equal" data-gap="medium" data-style="separated" data-type="maho-columns">
{features}</div>
<h2>Shop by category</h2>
<div data-preset="4-equal" data-gap="small" data-style="none" data-type="maho-columns">
{tiles}</div>
{{{{widget type="catalog/product_widget_new" display_type="new_products" products_count="4" template="catalog/product/widget/new/content/new_grid.phtml"}}}}
<div data-preset="2-equal" data-gap="large" data-style="none" data-type="maho-columns">
    <div data-type="maho-column">
        <p><img src="{{{{media url="wysiwyg/{c}/editorial.webp"}}}}" alt="{S.STORY['title']}" /></p>
    </div>
    <div data-type="maho-column">
        <p><span class="badge badge-outline">Our story</span></p>
        <h2>{S.STORY['title']}</h2>
        <p>{S.STORY['text1']}</p>
        <p>{S.STORY['text2']}</p>
        <p><a class="btn btn-outline" href="{{{{store url="about"}}}}">Read our story</a></p>
    </div>
</div>
<div data-preset="sidebar-left" data-gap="large" data-style="none" data-type="maho-columns">
    <div data-type="maho-column">
        <div class="card card-border">
            <div class="card-body">
                <p><span class="badge badge-error">{S.PROMO['badge']}</span></p>
                <h2 class="card-title">{S.PROMO['title']}</h2>
                <p>{S.PROMO['text']}</p>
                <p><a class="btn btn-primary btn-wide" href="{{{{store url="{S.PROMO['path']}"}}}}">{S.PROMO['button']}</a></p>
            </div>
        </div>
    </div>
    <div data-type="maho-column">
        {{{{widget type="catalog/product_widget_list" title="{S.PROMO['list_title']}" category_id="{{{{category_id:{S.ROOT}/{S.PROMO['path']}}}}}" sort="position" only_in_stock="1" products_count="3" template="catalog/product/widget/list/content/list_grid.phtml"}}}}
    </div>
</div>
<h2>What our customers say</h2>
<div data-preset="3-equal" data-gap="medium" data-style="cards" data-type="maho-columns">
{quotes}</div>
<div data-preset="2-equal" data-gap="medium" data-style="none" data-type="maho-columns">
    <div data-type="maho-column">
        <p><a href="{{{{store url="{cats[4]['path']}"}}}}" title="Shop {cats[4]['name']}"><img src="{{{{media url="wysiwyg/{c}/banner-a.webp"}}}}" alt="Shop {cats[4]['name']}" /></a></p>
        <h3>{cats[4]['name']}</h3>
        <p>{cats[4]['description']}</p>
        <p><a class="btn btn-outline" href="{{{{store url="{cats[4]['path']}"}}}}">Shop {cats[4]['name']}</a></p>
    </div>
    <div data-type="maho-column">
        <p><a href="{{{{store url="{cats[5]['path']}"}}}}" title="Shop {cats[5]['name']}"><img src="{{{{media url="wysiwyg/{c}/banner-b.webp"}}}}" alt="Shop {cats[5]['name']}" /></a></p>
        <h3>{cats[5]['name']}</h3>
        <p>{cats[5]['description']}</p>
        <p><a class="btn btn-outline" href="{{{{store url="{cats[5]['path']}"}}}}">Shop {cats[5]['name']}</a></p>
    </div>
</div>
{{{{widget type="blog/widget_posts" title="From the journal" posts_count="3" template="blog/widget/posts.phtml"}}}}
<div class="card card-border">
    <div class="card-body">
        <h2 style="text-align: center;">{S.NEWSLETTER['title']}</h2>
        <p style="text-align: center;">{S.NEWSLETTER['text']}</p>
        {{{{widget type="newsletter/widget_subscribe" template="newsletter/subscribe.phtml"}}}}
    </div>
</div>
'''

def landing_html(S, cat):
    c = S.CODE
    return f'''<div data-preset="2-equal" data-gap="large" data-style="none" data-type="maho-columns">
    <div data-type="maho-column">
        <p><img src="{{{{media url="wysiwyg/{c}/tile-{slug(cat['path'])}.webp"}}}}" alt="{cat['name']}" /></p>
    </div>
    <div data-type="maho-column">
        <p><span class="badge badge-outline">{cat['name']}</span></p>
        <h2>{cat['landing_title']}</h2>
        <p>{cat['landing_text']}</p>
    </div>
</div>
'''

def about_html(S):
    return f'''<div data-type="maho-columns" data-preset="2-equal" data-gap="large" data-style="none">
    <div data-type="maho-column">
        <p><img src="{{{{media url="wysiwyg/{S.CODE}/about.webp"}}}}" alt="{S.STORE_NAME}"></p>
    </div>
    <div data-type="maho-column">
        <p><span class="badge badge-outline">Our story</span></p>
        <h2>{S.ABOUT['title']}</h2>
        {''.join(f'<p>{p}</p>' + chr(10) + '        ' for p in S.ABOUT['paragraphs']).rstrip()}
    </div>
</div>
'''

CUSTOMER_SERVICE = '''<h1>Customer Service</h1>
<h2>Shipping and delivery</h2>
<p>Orders placed before noon on a weekday ship the same day. Standard delivery takes two to four working days. Express delivery arrives the next working day.</p>
<h2>Returns</h2>
<p>You can return an unused item within 30 days of delivery. Start the return from your account page and print the prepaid label. Refunds reach the original payment method within five working days of receipt.</p>
<h2>Payment</h2>
<p>We accept cards, PayPal and bank transfer. Every payment page is encrypted. We never store card numbers.</p>
<h2>Contact</h2>
<p>Write to us through the <a href="{{store url="contacts"}}">contact page</a>. We answer within one working day.</p>
'''

def merge_shared(S):
    """Adds the industry attributes of the spec to the shared attribute files when they are missing."""
    shared = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'packs', '_shared')
    attributes = list(csv.DictReader(open(f'{shared}/attributes.csv')))
    header = list(attributes[0].keys())
    known = {a['code'] for a in attributes}
    for a in getattr(S, 'ATTRIBUTES', []):
        if a['code'] not in known:
            attributes.append(a); known.add(a['code'])
    write_csv(f'{shared}/attributes.csv', attributes, header)
    options = list(csv.DictReader(open(f'{shared}/attribute_options.csv')))
    known = {(o['attribute_code'], o['label']) for o in options}
    for code, labels in getattr(S, 'OPTIONS', {}).items():
        for i, label in enumerate(labels):
            if (code, label) not in known:
                options.append(dict(attribute_code=code, label=label, sort_order=(i + 1) * 10, swatch=''))
    write_csv(f'{shared}/attribute_options.csv', options, ['attribute_code', 'label', 'sort_order', 'swatch'])

def build(spec_path):
    S = load_spec(spec_path)
    random.seed(S.CODE)
    root = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'packs', S.CODE)
    c = S.CODE
    # categories
    cats = [dict(root=S.ROOT, path='', name=S.ROOT, is_active=1, include_in_menu=1, is_anchor=1, description=S.ROOT_DESCRIPTION)]
    blocks = []
    for i, cat in enumerate(S.CATEGORIES):
        block = f'landing-{slug(cat["path"])}'
        cats.append(dict(root=S.ROOT, path=cat['path'], name=cat['name'], is_active=1, include_in_menu=1, is_anchor=1, position=i + 1,
                         display_mode='PRODUCTS_AND_PAGE', landing_page=block, image=f'{slug(cat["path"])}.webp', description=cat['description'],
                         meta_title=f"{cat['name']} | {S.STORE_NAME}", meta_description=cat['description']))
        for j, sub in enumerate(cat.get('children', [])):
            cats.append(dict(root=S.ROOT, path=f"{cat['path']}/{sub['path']}", name=sub['name'], is_active=1, include_in_menu=1, is_anchor=1, position=j + 1, description=sub.get('description', '')))
        blocks.append(dict(identifier=block, stores=c, title=f"Category landing: {cat['name']}", content_file=f'{block}.html', is_active=1))
        put(f'{root}/content/{block}.html', landing_html(S, cat))
    names = {c['path']: c['name'] for c in cats if c['path']}
    def named(path):
        parts = path.split('/')
        return '/'.join(names['/'.join(parts[:k + 1])] for k in range(len(parts)))
    write_csv(f'{root}/categories.csv', cats, ['root', 'path', 'name', 'is_active', 'include_in_menu', 'is_anchor', 'position', 'display_mode', 'landing_page', 'image', 'description', 'meta_title', 'meta_description'])
    write_csv(f'{root}/cms_blocks.csv', blocks, ['identifier', 'stores', 'title', 'content_file', 'is_active'])
    # pages
    put(f'{root}/content/home.html', home_html(S))
    put(f'{root}/content/about.html', about_html(S))
    put(f'{root}/content/customer-service.html', CUSTOMER_SERVICE)
    pages = [dict(identifier='home', stores=c, title=S.STORE_NAME, root_template='one_column', content_file='home.html', is_active=1, is_home=1, meta_description=S.META_DESCRIPTION),
             dict(identifier='about', stores=c, title=f'About {S.STORE_NAME}', root_template='two_columns_left', content_file='about.html', is_active=1, is_home=0),
             dict(identifier='customer-service', stores=c, title='Customer Service', root_template='two_columns_left', content_file='customer-service.html', is_active=1, is_home=0)]
    write_csv(f'{root}/cms_pages.csv', pages, ['identifier', 'stores', 'title', 'root_template', 'content_file', 'is_active', 'is_home', 'meta_description'])
    # products
    cols = ['sku', '_attribute_set', '_type', '_product_websites', '_root_category', '_category', 'name', 'price', 'special_price', 'status', 'visibility', 'tax_class_id', 'weight', 'description', 'short_description', 'qty', 'is_in_stock'] + S.ATTRIBUTE_COLUMNS + ['_media_image', 'image', 'small_image', 'thumbnail', 'url_key', '_super_products_sku', '_super_attribute_code', '_super_attribute_option', '_associated_sku', '_associated_default_qty', '_associated_position']
    rows, images, reviews = [], [], []
    def base(sku, name, price, vis, desc, short, attrs, img, urlkey, ptype='simple'):
        r = dict(sku=sku, _attribute_set=S.ATTRIBUTE_SET, _type=ptype, _product_websites=c, _root_category=S.ROOT, name=name, price=price, status=1, visibility=vis,
                 tax_class_id=2, weight=S.WEIGHT, description=desc, short_description=short, qty=random.randint(8, 60), is_in_stock=1, url_key=urlkey)
        r.update(attrs)
        if img:
            r.update(_media_image=img, image=img, small_image=img, thumbnail=img)
        return r
    for p in S.PRODUCTS:
        sku, name, cats_, price, axis, values, attrs, desc, prompt = p['sku'], p['name'], [named(c) for c in p['categories']], p['price'], p.get('axis'), p.get('values'), p.get('attributes', {}), p['description'], p['prompt']
        short = p.get('short') or desc.split('. ')[0].rstrip('.') + '.'
        desc = desc + ' ' + S.MORE[p['sku']]
        urlkey = slug(name)
        if p.get('grouped'):
            r = base(sku, name, price, 4, desc, short, attrs, f'{sku.lower()}.webp', urlkey, 'grouped'); r['_category'] = cats_[0]; r['qty'] = 0
            first = p['grouped'][0]
            r.update(_associated_sku=first, _associated_default_qty=1, _associated_position=1)
            rows.append(r)
            for k, asku in enumerate(p['grouped'][1:]):
                rows.append({'_associated_sku': asku, '_associated_default_qty': 1, '_associated_position': k + 2})
            for cat in cats_[1:]:
                rows.append({'_category': cat, '_root_category': S.ROOT})
            images.append({'file': sku.lower(), 'prompt': prompt})
            continue
        if not axis:
            r = base(sku, name, price, 4, desc, short, attrs, f'{sku.lower()}.webp', urlkey, p.get('type', 'simple')); r['_category'] = cats_[0]
            if p.get('special_price'): r['special_price'] = p['special_price']
            rows.append(r)
            for cat in cats_[1:]:
                rows.append({'_category': cat, '_root_category': S.ROOT})
            images.append({'file': sku.lower(), 'prompt': prompt})
            continue
        children = []
        for v in values:
            csku = f'{sku}-{slug(v).upper()}'
            a = dict(attrs); a[axis] = v
            img = f'{sku.lower()}-{slug(v)}.webp' if p.get('picture_per_value') else f'{sku.lower()}.webp'
            rows.append(base(csku, f'{name} {v}', price, 1, desc, short, a, img, slug(f'{name} {v}')))
            children.append((csku, v))
            if p.get('picture_per_value'):
                images.append({'file': img[:-5], 'prompt': prompt.replace('{value}', v.lower())})
        if not p.get('picture_per_value'):
            images.append({'file': sku.lower(), 'prompt': prompt.replace('{value}', values[0].lower())})
        parentimg = f'{sku.lower()}-{slug(values[0])}.webp' if p.get('picture_per_value') else f'{sku.lower()}.webp'
        r = base(sku, name, price, 4, desc, short, attrs, parentimg, urlkey, 'configurable'); r['_category'] = cats_[0]; r['qty'] = 0
        if p.get('special_price'): r['special_price'] = p['special_price']
        r.update(_super_products_sku=children[0][0], _super_attribute_code=axis, _super_attribute_option=children[0][1])
        rows.append(r)
        for csku, v in children[1:]:
            rows.append({'_super_products_sku': csku, '_super_attribute_code': axis, '_super_attribute_option': v})
        for cat in cats_[1:]:
            rows.append({'_category': cat, '_root_category': S.ROOT})
    write_csv(f'{root}/products.csv', rows, cols)
    names = ['Ada', 'Ben', 'Chloe', 'Dev', 'Elena', 'Femi', 'Greta', 'Hugo', 'Iris', 'Jonas', 'Kira', 'Leo', 'Maya', 'Noor', 'Oscar', 'Priya', 'Quinn', 'Rosa']
    k = 0
    for i, p in enumerate(S.PRODUCTS):
        if i % 3:
            continue
        for j in range(1 + i % 2):
            t = S.REVIEWS[k % len(S.REVIEWS)]
            k += 1
            reviews.append(dict(sku=p['sku'], store_code=c, nickname=names[(i + j) % len(names)], title=t[0], detail=t[1], rating=t[2], created_at=f'2026-0{1 + (i % 6)}-{10 + j:02d} 10:00:00'))
    write_csv(f'{root}/reviews.csv', reviews, ['sku', 'store_code', 'nickname', 'title', 'detail', 'rating', 'created_at'])
    # blog
    posts = []
    for i, (title, body, prompt) in enumerate(S.POSTS):
        key = slug(title)
        put(f'{root}/content/post-{key}.html', body)
        posts.append(dict(url_key=key, stores=c, title=title, is_active=1, publish_date=f'2026-0{1 + i}-1{i}', content_file=f'post-{key}.html', image=f'{c}/{key}.webp', meta_title=title, meta_description=body.split('</p>')[0].replace('<p>', '')[:150]))
    write_csv(f'{root}/blog_posts.csv', posts, ['url_key', 'stores', 'title', 'is_active', 'publish_date', 'content_file', 'image', 'meta_title', 'meta_description'])
    # manifest
    manifest = {'model': 'wavespeed-ai/krea-v2/turbo', 'output_dir': f'packs/{c}/media/import', 'style': S.PRODUCT_STYLE, 'images': [dict(i, size='1024x1024', ratio='1:1') for i in images]}
    scene = [
        {'file': 'hero-main', 'dir': f'media/wysiwyg/{c}', 'size': '2048x1152', 'ratio': '16:9', 'prompt': S.SCENES['hero-main']},
        {'file': 'hero-side', 'dir': f'media/wysiwyg/{c}', 'size': '1024x1024', 'ratio': '1:1', 'prompt': S.SCENES['hero-side']},
        {'file': 'editorial', 'dir': f'media/wysiwyg/{c}', 'size': '1024x1024', 'ratio': '1:1', 'prompt': S.SCENES['editorial']},
        {'file': 'about', 'dir': f'media/wysiwyg/{c}', 'size': '1024x1024', 'ratio': '1:1', 'prompt': S.SCENES['about']},
        {'file': 'banner-a', 'dir': f'media/wysiwyg/{c}', 'size': '1536x1024', 'ratio': '3:2', 'prompt': S.CATEGORIES[4]['scene']},
        {'file': 'banner-b', 'dir': f'media/wysiwyg/{c}', 'size': '1536x1024', 'ratio': '3:2', 'prompt': S.CATEGORIES[5]['scene']},
    ]
    for cat in S.CATEGORIES:
        scene.append({'file': f'tile-{slug(cat["path"])}', 'dir': f'media/wysiwyg/{c}', 'size': '1024x1024', 'ratio': '1:1', 'prompt': cat['scene']})
        scene.append({'file': slug(cat['path']), 'dir': f'packs/{c}/media/catalog/category', 'size': '1536x512', 'ratio': '3:1', 'model': 'ideogram-v3-turbo', 'prompt': cat['scene'] + BANNER})
    for title, body, prompt in S.POSTS:
        scene.append({'file': slug(title), 'dir': f'media/blog/{c}', 'size': '1536x1024', 'ratio': '3:2', 'prompt': prompt})
    for s in scene:
        s['prompt'] = s['prompt'] + ' ' + S.SCENE_STYLE
    manifest['images'] += scene
    json.dump(manifest, open(f'{root}/images.json', 'w'), indent=2)
    merge_shared(S)
    print(f"{c}: {len([r for r in rows if r.get('sku')])} product rows, {len(images)} product pictures, {len(scene)} scene pictures, {len(reviews)} reviews, {len(posts)} posts")

if __name__ == '__main__':
    build(sys.argv[1])
