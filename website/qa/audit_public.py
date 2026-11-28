"""Offline public-site integrity gate; no network requests or deployment."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import xml.etree.ElementTree as ET
import sys

BASE = "https://eden-practical.pages.dev"
class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.refs = []
        self.meta = {}
        self.canonical = []
        self.title = ""
        self.in_title = False
        self.images_missing_alt = 0
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a: self.ids.append(a["id"])
        for k in ("href", "src"):
            if a.get(k): self.refs.append(a[k])
        if tag == "meta":
            k = a.get("name") or a.get("property")
            if k: self.meta.setdefault(k, []).append(a.get("content", ""))
        if tag == "link" and a.get("rel") == "canonical":
            self.canonical.append(a.get("href", ""))
        if tag == "title": self.in_title = True
        if tag == "img" and "alt" not in a: self.images_missing_alt += 1
    def handle_endtag(self, tag):
        if tag == "title": self.in_title = False
    def handle_data(self, data):
        if self.in_title: self.title += data

def audit(root, sitemap):
    root = root.resolve()
    pages = {p.relative_to(root).as_posix(): Page(p.read_text(encoding="utf-8")) for p in root.rglob("*.html")}
    errors, titles, expected = [], set(), set()
    refs = 0
    if "index.html" not in pages: errors.append("Missing index.html")
    for name, p in sorted(pages.items()):
        def require(ok, msg):
            if not ok: errors.append(f"{name}: {msg}")
        url = BASE + ("/" if name == "index.html" else "/" + name.removesuffix(".html"))
        expected.add(url)
        require(bool(p.title.strip()) and p.title not in titles, "missing or duplicate title")
        titles.add(p.title)
        require(len(p.ids) == len(set(p.ids)), "duplicate ID")
        require("main" in p.ids, "missing main anchor")
        require(p.images_missing_alt == 0, "missing image alt attribute")
        require(p.canonical == [url], "incorrect canonical")
        for key in ("description", "viewport", "og:title", "og:description", "og:site_name", "og:type", "twitter:card"):
            values = p.meta.get(key, [])
            require(len(values) == 1 and bool(values[0].strip()), f"missing or duplicate {key}")
        require(p.meta.get("og:url") == [url], "incorrect og:url")
        require(p.meta.get("robots") == ["noindex,nofollow"], "prelaunch robots directive changed")
        for ref in p.refs:
            u = urlsplit(ref)
            if u.scheme or u.netloc: continue
            refs += 1
            path = unquote(u.path)
            target = (root / path.lstrip("/") if path.startswith("/") else root / Path(name).parent / path if path else root / name).resolve()
            if not target.is_relative_to(root):
                require(False, f"escaping reference {ref}")
                continue
            if target.is_dir(): target = target / "index.html"
            if not target.is_file() and not target.suffix: target = target.with_suffix(".html")
            require(target.is_file(), f"missing reference {ref}")
            if u.fragment:
                key = target.relative_to(root).as_posix()
                require(key in pages and unquote(u.fragment) in pages[key].ids, f"missing anchor {ref}")
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = [x.text for x in ET.parse(sitemap).findall("s:url/s:loc", ns)]
    if len(urls) != len(set(urls)) or set(urls) != expected: errors.append("Staged sitemap does not match canonical routes")
    if (root / "sitemap.xml").exists(): errors.append("Prelaunch sitemap unexpectedly public")
    return errors, len(pages), refs

if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    errors, pages, refs = audit(root / "public", root / "drafts/sitemap.xml")
    print(f"{pages} pages, {refs} local references, {len(errors)} errors")
    for error in errors: print(error)
    sys.exit(bool(errors))
