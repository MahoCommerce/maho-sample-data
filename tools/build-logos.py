#!/usr/bin/env python3
"""Write one SVG wordmark per industry store in the display font and primary colour of its theme.

Run with tools/.venv (fonttools, brotli, uharfbuzz): tools/.venv/bin/python tools/build-logos.py
Font files come from fonts.bunny.net and are cached under tools/.fonts.
"""
import io, os, re, sys, urllib.request
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = os.path.join(ROOT, 'tools', '.fonts')

# code: (name, font slug, weight, icon colour, dark icon colour, text colour, dark text colour, Tabler icon)
STORES = {
    'fashion': ('Maison Maho', 'instrument-serif', 400, '#131312', '#f4f2ee', '#131312', '#f4f2ee', 'hanger'),
    'electronics': ('Voltline', 'geist', 600, '#0668cf', '#79b8ff', '#1d1d1f', '#f2f2f4', 'bolt'),
    'food': ('Harvest & Hearth', 'bricolage-grotesque', 700, '#c53f21', '#f0875e', '#2e2a22', '#f5f0e6', 'wheat'),
    'books': ('Folio', 'literata', 600, '#12727a', '#7fc4c9', '#26221a', '#f3eee4', 'book-2'),
    'jewelry': ('Aurelie', 'bodoni-moda', 500, '#1e1a13', '#efe9dc', '#1e1a13', '#efe9dc', 'diamond'),
    'beauty': ('Glow Atelier', 'newsreader', 500, '#a94a64', '#dd8fa8', '#352b28', '#f6eeea', 'droplet'),
    'home': ('Hearthstone', 'schibsted-grotesk', 600, '#a04620', '#d18a60', '#26211a', '#f4efe8', 'home-2'),
    'sports': ('Stride', 'archivo', 800, '#101214', '#e9ecec', '#101214', '#e9ecec', 'run'),
    'kids': ('Little Lark', 'fredoka', 600, '#c43f1e', '#f2a07f', '#33302a', '#f7f2ea', 'balloon'),
    'garden': ('Greenhaven', 'alegreya', 500, '#3c6a26', '#93c274', '#262c1f', '#eef2e6', 'plant-2'),
}

# Tabler outline icons from the maho checkout (mahocommerce/icons), 24 unit box, stroke 2
ICONS = os.environ.get('MAHO_ICONS', os.path.join(os.path.dirname(ROOT), 'maho', 'vendor', 'mahocommerce', 'icons', 'icons', 'outline'))


def icon_body(name):
    svg = open(os.path.join(ICONS, f'{name}.svg')).read()
    return re.search(r'<svg[^>]*>(.*)</svg>', svg, re.S).group(1).strip()


def font_bytes(slug, weight):
    path = os.path.join(FONTS, f'{slug}-{weight}.woff2')
    if not os.path.exists(path):
        url = f'https://fonts.bunny.net/{slug}/files/{slug}-latin-{weight}-normal.woff2'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        open(path, 'wb').write(urllib.request.urlopen(req).read())
    return open(path, 'rb').read()


def wordmark(text, data):
    """Shape the text with HarfBuzz and return (svg path data, width) in font units."""
    ttf = TTFont(io.BytesIO(data))
    ttf.flavor = None  # HarfBuzz reads plain SFNT, not WOFF2
    raw = io.BytesIO()
    ttf.save(raw)
    upem = ttf['head'].unitsPerEm
    glyph_set = ttf.getGlyphSet()
    order = ttf.getGlyphOrder()
    face = hb.Face(raw.getvalue())
    font = hb.Font(face)
    font.scale = (upem, upem)
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf, {'kern': True, 'liga': True})
    x = 0
    parts = []
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        pen = SVGPathPen(glyph_set)
        glyph_set[order[info.codepoint]].draw(TransformPen(pen, (1, 0, 0, -1, x + pos.x_offset, -pos.y_offset)))
        d = pen.getCommands()
        if d:
            parts.append(d)
        x += pos.x_advance
    cap = ttf['OS/2'].sCapHeight if hasattr(ttf['OS/2'], 'sCapHeight') and ttf['OS/2'].sCapHeight else int(upem * 0.7)
    return ' '.join(parts), x, upem, cap


def build(code):
    name, slug, weight, icon_colour, icon_dark, text_colour, text_dark, icon = STORES[code]
    d, width, upem, cap = wordmark(name, font_bytes(slug, weight))
    # layout in font units: the icon box is 1.3 cap heights tall and sits on the baseline, then a gap, then the text
    box = int(cap * 1.3)
    gap = int(cap * 0.3)
    pad = int(upem * 0.06)
    total_w = box + gap + width + 2 * pad
    top = -int(upem * 0.9)
    total_h = int(upem * 1.15)
    scale = box / 24
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-pad} {top} {total_w} {total_h}" width="{round(total_w / upem * 40)}" height="{round(total_h / upem * 40)}" role="img" aria-label="{name.replace('&', '&amp;')}">
  <style>@media (prefers-color-scheme: dark){{.i{{stroke:{icon_dark}}}.t{{fill:{text_dark}}}}}</style>
  <g class="i" transform="translate(0 {-box + int(cap * 0.08)}) scale({scale:.4f})" fill="none" stroke="{icon_colour}" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">{icon_body(icon)}</g>
  <path class="t" transform="translate({box + gap} 0)" fill="{text_colour}" d="{d}"/>
</svg>
'''
    out = os.path.join(ROOT, 'media', 'wysiwyg', code, 'logo.svg')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w').write(svg)
    print(f'{code}: {name} in {slug} {weight}, {len(svg)} bytes')


if __name__ == '__main__':
    for code in (sys.argv[1:] or STORES):
        build(code)
