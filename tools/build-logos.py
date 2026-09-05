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


def wordmark(text, data, tracking=0.0):
    """Shape the text with HarfBuzz and return (svg path data, width, units per em, cap height) in font units.
    tracking adds that fraction of an em after every glyph."""
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
    extra = int(upem * tracking)
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        pen = SVGPathPen(glyph_set)
        glyph_set[order[info.codepoint]].draw(TransformPen(pen, (1, 0, 0, -1, x + pos.x_offset, -pos.y_offset)))
        d = pen.getCommands()
        if d:
            parts.append(d)
        x += pos.x_advance + extra
    x -= extra
    cap = ttf['OS/2'].sCapHeight if getattr(ttf['OS/2'], 'sCapHeight', 0) else int(upem * 0.7)
    return ' '.join(parts), x, upem, cap


# typographic treatment per store: caps with tracking, or mixed case; the accent is a coloured glyph
TYPE = {
    'fashion': dict(caps=True, tracking=0.16),
    'jewelry': dict(caps=True, tracking=0.22),
    'beauty': dict(caps=False, tracking=0.02),
    'books': dict(caps=False, tracking=0.0),
    'garden': dict(caps=False, tracking=0.01),
    'electronics': dict(caps=True, tracking=0.06),
    'food': dict(caps=False, tracking=0.0, accent='&'),
    'home': dict(caps=False, tracking=0.0),
    'sports': dict(caps=True, tracking=0.04),
    'kids': dict(caps=False, tracking=0.0),
}
SHAPE = {'fashion': 'circle', 'jewelry': 'diamond', 'beauty': 'circle', 'books': 'square', 'garden': 'circle',
         'electronics': 'square', 'food': 'circle', 'home': 'square', 'sports': 'square', 'kids': 'circle'}
MONOGRAM = {'fashion': 'MM', 'electronics': 'V', 'food': 'H', 'books': 'F', 'jewelry': 'A', 'beauty': 'G', 'home': 'H', 'sports': 'S', 'kids': 'LL', 'garden': 'G'}


def shape_path(kind, size):
    r = size / 2
    if kind == 'circle':
        return f'<circle cx="{r:.0f}" cy="{r:.0f}" r="{r:.0f}"/>'
    if kind == 'diamond':
        return f'<path d="M{r:.0f} 0L{size:.0f} {r:.0f}L{r:.0f} {size:.0f}L0 {r:.0f}Z"/>'
    return f'<rect width="{size:.0f}" height="{size:.0f}" rx="{size * 0.22:.0f}"/>'


def text_parts(code, data):
    """Shape the store name; with an accent glyph the name is shaped in three pieces so the accent can take the icon colour."""
    name = STORES[code][0]
    t = TYPE[code]
    text = name.upper() if t['caps'] else name
    if not t.get('accent'):
        d, width, upem, cap = wordmark(text, data, t['tracking'])
        return d, width, upem, cap, None
    i = text.index(t['accent'])
    before, width_b, upem, cap = wordmark(text[:i], data, t['tracking'])
    a, width_a, _, _ = wordmark(t['accent'], data, t['tracking'])
    after, width_c, _, _ = wordmark(text[i + 1:], data, t['tracking'])
    gap = int(upem * t['tracking'])
    d = f'{before} {shift(after, width_b + gap + width_a + gap)}'
    return d, width_b + width_a + width_c + 2 * gap, upem, cap, (a, width_b + gap)


def shift(d, dx):
    """Move absolute SVG path data along x (fontTools writes absolute commands only)."""
    out = []
    for token in re.findall(r'[MLCQZHV]|-?\d+\.?\d*', d):
        out.append(token)
    result = []
    i = 0
    cmd = None
    while i < len(out):
        tok = out[i]
        if tok.isalpha():
            cmd = tok
            result.append(tok)
            i += 1
            continue
        if cmd == 'V':
            result.append(tok)
            i += 1
        elif cmd == 'H':
            result.append(str(round(float(tok) + dx)))
            i += 1
        else:
            result.append(str(round(float(tok) + dx)))
            result.append(out[i + 1])
            i += 2
    return ' '.join(result)


def build_svg(code, style):
    name, slug, weight, icon_colour, icon_dark, text_colour, text_dark, icon = STORES[code]
    data = font_bytes(slug, weight)
    d, width, upem, cap, accent = text_parts(code, data)
    pad = int(upem * 0.06)
    top = -int(upem * 0.9)
    total_h = int(upem * 1.15)
    mark = ''
    mark_w = 0
    if style in ('badge', 'monogram'):
        size = int(cap * 1.45)
        y = -int((size - cap) / 2) - cap
        if style == 'badge':
            sc = size * 0.62 / 24
            inner = ('<g transform="translate(%.0f %.0f) scale(%.4f)" fill="none" stroke="#ffffff" stroke-width="1.9" '
                     'stroke-linecap="round" stroke-linejoin="round">%s</g>') % (size * 0.19, size * 0.19, sc, icon_body(icon))
        else:
            m, mw, _, mcap = wordmark(MONOGRAM[code], data)
            ms = size * 0.5 / mcap if len(MONOGRAM[code]) == 1 else size * 0.72 / mw
            inner = '<path transform="translate(%.0f %.0f) scale(%.4f)" fill="#ffffff" d="%s"/>' % ((size - mw * ms) / 2, (size + mcap * ms) / 2, ms, m)
        mark = ('<g class="m" transform="translate(0 %d)" fill="%s">%s</g><g transform="translate(0 %d)">%s</g>'
                % (y, icon_colour, shape_path(SHAPE[code], size), y, inner))
        mark_w = size + int(cap * 0.38)
    accent_svg = ''
    if accent:
        a, offset = accent
        accent_svg = '<path class="m" transform="translate(%d 0)" fill="%s" d="%s"/>' % (mark_w + offset, icon_colour, a)
    total_w = mark_w + width + 2 * pad
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="%d %d %d %d" width="%d" height="%d" role="img" aria-label="%s">\n'
            '  <style>@media (prefers-color-scheme: dark){.m{fill:%s}.t{fill:%s}}</style>\n'
            '  %s\n'
            '  <path class="t" transform="translate(%d 0)" fill="%s" d="%s"/>\n'
            '  %s\n'
            '</svg>\n') % (-pad, top, total_w, total_h, round(total_w / upem * 40), round(total_h / upem * 40), name.replace('&', '&amp;'),
                           icon_dark, text_dark, mark, mark_w, text_colour, d, accent_svg)


STYLE = {code: 'type' for code in STORES}


def build(code, style=None, out=None):
    svg = build_svg(code, style or STYLE[code])
    out = out or os.path.join(ROOT, 'media', 'wysiwyg', code, 'logo.svg')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w').write(svg)
    print('%s: %s, %d bytes' % (code, style or STYLE[code], len(svg)))


if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == '--preview':
        for code in STORES:
            for style in ('badge', 'monogram', 'type'):
                build(code, style, os.path.join(sys.argv[2], '%s-%s.svg' % (code, style)))
    else:
        for code in (sys.argv[1:] or STORES):
            build(code)
