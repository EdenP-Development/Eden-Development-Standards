"""Read-only HTTPS route audit for the public portfolio."""
import urllib.request
import urllib.error
from urllib.parse import urlsplit
from html.parser import HTMLParser
from pathlib import Path
import xml.etree.ElementTree as ET
import sys

BASE = "https://eden-practical.pages.dev"

class Metadata(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.canonical = []
        self.robots = []
        self.feed(html)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "link" and a.get("rel") == "canonical":
            self.canonical.append(a.get("href"))
        if tag == "meta" and a.get("name") == "robots":
            self.robots.append(a.get("content"))

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent":"EdenPractical-WebsiteQA/1.0"})
    with urllib.request.urlopen(req, timeout=20) as r:
        data = r.read(2_000_001)
        if len(data) > 2_000_000: raise ValueError("oversize HTML")
        return r.status, r.geturl(), r.headers.get_content_type(), Metadata(data.decode("utf-8"))

def main():
    sitemap = Path(__file__).resolve().parents[1] / "drafts/sitemap.xml"
    ns = {"s":"http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = [x.text for x in ET.parse(sitemap).findall("s:url/s:loc", ns)]
    failures = []
    for url in urls:
        if not url or urlsplit(url).netloc != urlsplit(BASE).netloc or not url.startswith(BASE+"/"):
            failures.append("Unexpected sitemap host")
            continue
        alias = BASE + "/index.html" if url == BASE+"/" else url+".html"
        for requested in (url, alias):
            try:
                status, final, mime, meta = get(requested)
                assert status == 200 and final == url, f"status={status}, final={final}"
                assert mime == "text/html", f"content type={mime}"
                assert meta.canonical == [url], f"canonical={meta.canonical}"
                assert meta.robots == ["noindex,nofollow"], f"robots={meta.robots}"
                print("PASS", requested, "->", final)
            except Exception as e:
                failures.append(f"{requested}: {e}")
    for f in failures: print("FAIL", f)
    print(f"{len(urls)*2} planned route checks; {len(failures)} failures")
    return bool(failures)

if __name__ == "__main__":
    sys.exit(main())
