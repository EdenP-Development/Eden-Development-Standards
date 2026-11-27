"""Private review catalog: normalize/expand shell pages, preserving V8 markup."""
import json
import re
import sys
from pathlib import Path
from html import escape, unescape

GROUPS = {'gridmates.html': 'gridmates', 'spudacus.html': 'spudacus', 'solutions.html': 'eps'}
CARD = re.compile(r'<article class="(?P<css>[^"]+)">(?P<image><img [^>]+>)?(?:<p>(?P<status>.*?)</p>)?<h3>(?P<title>.*?)</h3><p>(?P<description>.*?)</p><a class="action" href="(?P<route>[a-z-]+\.html)">(?P<action>.*?)</a></article>')
SLOT = '<!-- product-catalog -->'
COUNT = '<!-- gridmates-count -->'

def render_card(record):
    c = record['card']
    e = lambda s: escape(s, quote=False)
    status = '<p>' + e(c['status']) + '</p>' if c['status'] is not None else ''
    return ('<article class="' + escape(c['css'], quote=True) + '">' + (c['image'] or '') + status + '<h3>' + e(c['title']) + '</h3><p>' + e(c['description']) + '</p><a class="action" href="' + escape(record['route'], quote=True) + '">' + e(c['action']) + '</a></article>')

def normalize(pages):
    hubs = dict(pages)
    products = []
    for route, group in GROUPS.items():
        body = pages[route]['main']
        matches = [m for m in CARD.finditer(body) if m['route'] not in GROUPS]
        if not matches or any(a.end() != b.start() for a, b in zip(matches, matches[1:])):
            raise ValueError('Unsupported listing layout: ' + route)
        for m in matches:
            fields = m.groupdict()
            target = fields.pop('route')
            card = {k: unescape(v) if v is not None and k != 'image' else v for k, v in fields.items()}
            record = {'route': target, 'group': group, 'card': card, 'page': hubs.pop(target)}
            if render_card(record) != m[0]:
                raise ValueError('Card parity failed: ' + target)
            products.append(record)
        body = body[:matches[0].start()] + SLOT + body[matches[-1].end():]
        if group == 'spudacus':
            body = body.replace('Four illustrated puzzle and adventure projects.', COUNT)
        hubs[route] = {**pages[route], 'main': body}
    return {'hubs': hubs, 'products': products}

def expand(model):
    pages = dict(model['hubs'])
    products = model['products']
    for record in products:
        route = record['route']
        if not re.fullmatch(r'[a-z-]+\.html', route) or route in pages or record['group'] not in GROUPS.values():
            raise ValueError('Invalid or duplicate product route: ' + route)
        pages[route] = record['page']
    count = sum(p['group'] == 'gridmates' for p in products)
    count_text = 'Four' if count == 4 else str(count)
    for route, group in GROUPS.items():
        body = pages[route]['main']
        if body.count(SLOT) != 1:
            raise ValueError('Expected one catalog slot: ' + route)
        body = body.replace(SLOT, ''.join(render_card(p) for p in products if p['group'] == group))
        body = body.replace(COUNT, count_text + ' illustrated puzzle and adventure projects.')
        pages[route] = {**pages[route], 'main': body}
    return pages

if __name__ == '__main__':
    mode, src, dst = sys.argv[1:]
    data = json.loads(Path(src).read_text(encoding='utf-8'))
    result = {'normalize': normalize, 'expand': expand}[mode](data)
    with Path(dst).open('x', encoding='utf-8') as out:
        json.dump(result, out, ensure_ascii=False, indent=2)
        out.write('\n')
