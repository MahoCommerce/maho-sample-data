#!/usr/bin/env python3
"""Write one SVG wordmark per industry store in the display font and primary colour of its theme.

Run with tools/.venv (fonttools, brotli, uharfbuzz): tools/.venv/bin/python tools/build-logos.py
Font files come from fonts.bunny.net and are cached under tools/.fonts.
"""
import io, os, sys, urllib.request
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = os.path.join(ROOT, 'tools', '.fonts')

# code: (name, font slug, weight, colour, dark colour, glyph)
STORES = {
    'fashion': ('Maison Maho', 'instrument-serif', 400, '#131312', '#f4f2ee', 'ring'),
    'electronics': ('Voltline', 'geist', 600, '#0668cf', '#79b8ff', 'bolt'),
    'food': ('Harvest & Hearth', 'bricolage-grotesque', 700, '#c53f21', '#f0875e', 'leaf'),
    'books': ('Folio', 'literata', 600, '#12727a', '#7fc4c9', 'book'),
    'jewelry': ('Aurelie', 'bodoni-moda', 500, '#1e1a13', '#efe9dc', 'gem'),
    'beauty': ('Glow Atelier', 'newsreader', 500, '#a94a64', '#dd8fa8', 'drop'),
    'home': ('Hearthstone', 'schibsted-grotesk', 600, '#a04620', '#d18a60', 'house'),
    'sports': ('Stride', 'archivo', 800, '#101214', '#e9ecec', 'chevron'),
    'kids': ('Little Lark', 'fredoka', 600, '#c43f1e', '#f2a07f', 'sun'),
    'garden': ('Greenhaven', 'alegreya', 500, '#3c6a26', '#93c274', 'sprout'),
}

# glyphs are drawn in a 100 x 100 box, stroke width 9, and scaled to the cap height
GLYPHS = {
    'ring': '<circle cx="50" cy="50" r="38" fill="none" stroke="{c}" stroke-width="9"/>',
    'bolt': '<path d="M58 4 22 56h26l-8 40 38-52H52z" fill="{c}"/>',
    'leaf': '<path d="M14 86C14 40 40 14 88 12c2 48-24 76-70 76zM14 86 66 34" fill="none" stroke="{c}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>',
    'book': '<path d="M50 24c-10-8-24-10-38-8v66c14-2 28 0 38 8 10-8 24-10 38-8V16c-14-2-28 0-38 8zM50 24v66" fill="none" stroke="{c}" stroke-width="9" stroke-linejoin="round"/>',
    'gem': '<path d="M26 12h48l20 26-44 54L6 38zM6 38h88M26 12l24 26 24-26M50 38v54" fill="none" stroke="{c}" stroke-width="8" stroke-linejoin="round"/>',
    'drop': '<path d="M50 8c22 30 34 46 34 62a34 34 0 0 1-68 0c0-16 12-32 34-62z" fill="none" stroke="{c}" stroke-width="9" stroke-linejoin="round"/>',
    'house': '<path d="M10 48 50 12l40 36M22 40v48h56V40M42 88V60h16v28" fill="none" stroke="{c}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>',
    'chevron': '<path d="M14 12 52 50 14 88M50 12l38 38-38 38" fill="none" stroke="{c}" stroke-width="11" stroke-linecap="round" stroke-linejoin="round"/>',
    'sun': '<circle cx="50" cy="50" r="18" fill="{c}"/><path d="M50 6v14M50 80v14M6 50h14M80 50h14M19 19l10 10M71 71l10 10M81 19 71 29M29 71 19 81" fill="none" stroke="{c}" stroke-width="9" stroke-linecap="round"/>',
    'sprout': '<path d="M50 92V44M50 44C50 24 36 12 14 12c0 22 14 34 36 32zM50 60c0-18 14-30 36-30 0 20-14 32-36 30z" fill="none" stroke="{c}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>',
}


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
    name, slug, weight, colour, dark, glyph = STORES[code]
    d, width, upem, cap = wordmark(name, font_bytes(slug, weight))
    # layout in font units: the glyph box is one cap height tall, then a gap, then the text on the baseline at y = 0
    box = cap
    gap = int(cap * 0.35)
    pad = int(upem * 0.08)
    total_w = box + gap + width + 2 * pad
    top = -int(upem * 0.85)
    total_h = int(upem * 1.1)
    scale = box / 100
    icon = GLYPHS[glyph].format(c=colour).replace('fill="none"', 'fill="none" class="s"').replace(f'fill="{colour}"', f'fill="{colour}" class="f"')
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-pad} {top} {total_w} {total_h}" width="{round(total_w / upem * 40)}" height="{round(total_h / upem * 40)}" role="img" aria-label="{name.replace('&', '&amp;')}">
  <style>@media (prefers-color-scheme: dark){{.f{{fill:{dark}}}.s{{stroke:{dark}}}}}</style>
  <g transform="translate(0 {-cap}) scale({scale:.4f})">{icon}</g>
  <path class="f" transform="translate({box + gap} 0)" fill="{colour}" d="{d}"/>
</svg>
'''
    out = os.path.join(ROOT, 'media', 'wysiwyg', code, 'logo.svg')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w').write(svg)
    print(f'{code}: {name} in {slug} {weight}, {len(svg)} bytes')


if __name__ == '__main__':
    for code in (sys.argv[1:] or STORES):
        build(code)
