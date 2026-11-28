import tempfile
import unittest
from pathlib import Path
from audit_public import audit, BASE

def page():
    metas = {"description":"Example", "viewport":"width=device-width", "og:title":"Example", "og:description":"Example", "og:site_name":"Eden Practical", "og:type":"website", "twitter:card":"summary", "og:url":BASE+"/", "robots":"noindex,nofollow"}
    return '<html><head><title>Example</title><link rel="canonical" href="'+BASE+'/">'+''.join(f'<meta name="{k}" content="{v}">' for k,v in metas.items())+'</head><body><main id="main"><a href="#main">Home</a><img src="icon.png" alt="Example"></main></body></html>'

class IntegrityTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)/"public"
        self.root.mkdir()
        self.index = self.root/"index.html"
        self.index.write_text(page(), encoding="utf-8")
        (self.root/"icon.png").write_bytes(b"fixture")
        self.sitemap = self.root.parent/"sitemap.xml"
        self.sitemap.write_text('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>'+BASE+'/</loc></url></urlset>', encoding="utf-8")

    def errors(self):
        return audit(self.root, self.sitemap)[0]

    def change(self, old, new, expected):
        self.assertIn(old, page())
        self.index.write_text(page().replace(old,new,1), encoding="utf-8")
        self.assertTrue(any(expected in e for e in self.errors()), self.errors())

    def test_valid(self): self.assertEqual(self.errors(), [])
    def test_missing_asset(self):
        (self.root/"icon.png").unlink()
        self.assertTrue(any("missing reference" in e for e in self.errors()))
    def test_anchor(self): self.change('href="#main"', 'href="#gone"', "missing anchor")
    def test_alt(self): self.change(' alt="Example"', '', "missing image alt")
    def test_canonical(self): self.change('rel="canonical" href="'+BASE+'/"', 'rel="canonical" href="'+BASE+'/bad"', "incorrect canonical")
    def test_robots(self): self.change('noindex,nofollow', 'index,follow', "robots directive changed")
    def test_description(self): self.change('name="description"', 'name="unused"', "missing or duplicate description")
    def test_duplicate_id(self): self.change('<a href=', '<a id="main" href=', "duplicate ID")
    def test_escape(self): self.change('src="icon.png"', 'src="../icon.png"', "escaping reference")
    def test_sitemap(self):
        self.sitemap.write_text('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"/>', encoding="utf-8")
        self.assertIn("Staged sitemap does not match canonical routes", self.errors())
    def test_public_sitemap(self):
        (self.root/"sitemap.xml").write_text("fixture")
        self.assertIn("Prelaunch sitemap unexpectedly public", self.errors())

if __name__ == "__main__":
    unittest.main()
