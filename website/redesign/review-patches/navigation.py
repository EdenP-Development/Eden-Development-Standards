"""Normalize V8 page shell records; preserve exact rendered HTML."""
import json
import re
import sys
from pathlib import Path
from html import escape, unescape

HEADER = re.compile(r'<header><a class="brand" href="([^"]+)">(.*?)</a><nav aria-label="Main navigation">(.*?)</nav></header>', re.S)
LINK = re.compile(r'<a href="([^"]+)">(.*?)</a>', re.S)
LEGAL = '<a href="index.html">Eden Practical</a> · <a href="index.html#about">About</a> · <a href="index.html#help">Help and privacy</a><p>Website concept. No claim of incorporated status.</p>'
SUFFIX = ' · Private artwork pilot'

def link(href, label):
    return f'<a href="{escape(href, quote=True)}">{escape(label, quote=False)}</a>'

def render_header(record, brands):
    href, label = brands[record['brand']]
    return f'<header><a class="brand" href="{escape(href, quote=True)}">{escape(label, quote=False)}</a><nav aria-label="Main navigation">' + ''.join(link(*pair) for pair in record['links']) + '</nav></header>'

def render_footer(record):
    kind = record['kind']
    if kind == 'legal':
        body = LEGAL
    elif kind == 'linked':
        body = link(*record['credit']) + SUFFIX
    elif kind == 'text':
        body = escape(record['credit'], quote=False) + SUFFIX
    else:
        raise ValueError('Unknown footer kind')
    return '<footer>' + body + '</footer>'

def normalize(pages):
    brands, records = {}, {}
    for name, fields in pages.items():
        match = HEADER.fullmatch(fields['header'])
        if not match:
            raise ValueError(name + ': unsupported header')
        href, label, nav = match.groups()
        brand = unescape(label)
        pair = [unescape(href), brand]
        if brand in brands and brands[brand] != pair:
            raise ValueError(name + ': conflicting brand destination')
        brands[brand] = pair
        header = {'brand': brand, 'links': [[unescape(a), unescape(b)] for a,b in LINK.findall(nav)]}
        body = fields['footer'].removeprefix('<footer>').removesuffix('</footer>')
        if body == LEGAL:
            footer = {'kind': 'legal'}
        elif body.endswith(SUFFIX):
            credit = body[:-len(SUFFIX)]
            m = LINK.fullmatch(credit)
            footer = {'kind': 'linked', 'credit': [unescape(x) for x in m.groups()]} if m else {'kind': 'text', 'credit': unescape(credit)}
        else:
            raise ValueError(name + ': unsupported footer')
        if render_header(header, brands) != fields['header'] or render_footer(footer) != fields['footer']:
            raise ValueError(name + ': exact parity failed')
        records[name] = {**{k:v for k,v in fields.items() if k not in ('header','footer')}, 'navigation': header, 'credit': footer}
    return {'brands': brands, 'pages': records}

def expand(model):
    return {name: {**{k:v for k,v in row.items() if k not in ('navigation','credit')}, 'header': render_header(row['navigation'], model['brands']), 'footer': render_footer(row['credit'])} for name,row in model['pages'].items()}

if __name__ == '__main__':
    mode, src, dst = sys.argv[1:]
    data = json.loads(Path(src).read_text(encoding='utf-8'))
    result = {'normalize': normalize, 'expand': expand}[mode](data)
    with Path(dst).open('x', encoding='utf-8') as out:
        json.dump(result, out, ensure_ascii=False, indent=2)
        out.write('\n')
