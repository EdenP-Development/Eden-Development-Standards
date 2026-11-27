#!/usr/bin/env python3
"""Local-only browser smoke test; run from any directory with Playwright Chromium installed."""
from pathlib import Path
from hashlib import sha256
from playwright.sync_api import sync_playwright
import json
import os

ROOT = Path(__file__).resolve().parents[2]
ASSETS = {
    "branding/spudacus/v1.0/full-transparent.png": "74773dbda822161f73a639f959e8bce5c6e0b333a94ebeb8ee27f620d4995d25",
    "branding/gridmates/v1.0/runtime-transparent.png": "eef6d631cac0b9523f7e0dbebac229f9a2458d36fe2e73e111d251704d9ff292",
    "branding/eps/v1.0/runtime-transparent.png": "d144934346d77a6e04c1475dae361fc57cb28a95d7033a799bf6e2f256548516",
}
PAGES = ["website/prototype/index.html"] + [
    f"website/prototype/products/{slug}.html" for slug in
    ("sudoku", "word-search", "grid-hunt", "crossroads", "sector-rebound", "eden-comms")
]
FILES = {**{p: "image/png" for p in ASSETS}, **{p: "text/html; charset=utf-8" for p in PAGES}, "website/prototype/site.css": "text/css; charset=utf-8"}
ORIGIN = "https://eden-preview.invalid/"
CASES = [(320,640,16),(390,844,16),(768,1024,16),(1440,900,16),(320,640,32),(390,844,32)]

def require(ok, msg):
    if not ok:
        raise RuntimeError(msg)

def main():
    for path, expected in ASSETS.items():
        require(sha256((ROOT/path).read_bytes()).hexdigest() == expected, "Asset hash mismatch: "+path)
    results = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(executable_path=os.environ.get("CHROMIUM_PATH") or None)
        for w,h,root_font in CASES:
            ctx = browser.new_context(viewport={"width":w,"height":h}, service_workers="block")
            unexpected, errors = [], []
            def serve(route):
                url = route.request.url
                path = url.removeprefix(ORIGIN)
                if not url.startswith(ORIGIN) or path not in FILES:
                    unexpected.append(url)
                    route.abort()
                    return
                route.fulfill(status=200, content_type=FILES[path], body=(ROOT/path).read_bytes())
            ctx.route("**/*", serve)
            page = ctx.new_page()
            page.on("pageerror", lambda e: errors.append(str(e)))
            def verify(path):
                page.wait_for_load_state("load")
                page.evaluate("(n)=>document.documentElement.style.fontSize=n+'px'", root_font)
                page.evaluate("Promise.all([...document.images].map(i=>i.decode()))")
                stats = page.evaluate("""()=>({
                    width:document.documentElement.clientWidth,
                    scroll:document.documentElement.scrollWidth,
                    styles:[...document.styleSheets].some(s=>s.href?.endsWith('/site.css') && s.cssRules.length>0),
                    images:[...document.images].every(i=>i.naturalWidth>0),
                    count:document.images.length,
                    links:[...document.querySelectorAll('nav a,.action,.profile-link,.card a,.product-actions a')].every(a=>a.getBoundingClientRect().height>=47.9)
                })""")
                require(stats["scroll"]<=stats["width"], f"Overflow: {path} {w}/{root_font} {stats}")
                require(stats["styles"] and stats["images"] and stats["count"]==(3 if path==PAGES[0] else 1) and stats["links"], f"Resource/target failure: {path} {stats}")
                page.keyboard.press("Tab")
                require(page.evaluate("document.activeElement.classList.contains('skip')"), "Skip link not first focus")
                page.keyboard.press("Enter")
                require(page.evaluate("document.activeElement.id==='main'"), "Skip destination not focused")
                return stats
            page.goto(ORIGIN+PAGES[0])
            home=verify(PAGES[0])
            for target in ["games","tools","designs","help"]:
                page.locator(f'nav a[href="#{target}"]').click()
                require(page.evaluate("""id=>{const r=document.getElementById(id).getBoundingClientRect();return r.top<innerHeight && r.bottom>0}""",target), "Invisible section: "+target)
            products = {}
            for path in PAGES[1:]:
                relative = path.removeprefix("website/prototype/")
                page.locator(f'a[href="{relative}"]').click()
                require(page.url==ORIGIN+path, "Product route mismatch: "+path)
                products[path]=verify(path)
                page.locator('a[href="#features"]').click()
                require(page.evaluate("location.hash==='#features'"), "Feature anchor mismatch")
                destination="tools" if path.endswith("eden-comms.html") else "games"
                page.locator(f'main a[href="../index.html#{destination}"]').click()
                require(page.url==ORIGIN+PAGES[0]+"#"+destination, "Return route mismatch")
                page.evaluate("(n)=>document.documentElement.style.fontSize=n+'px'", root_font)
            require(not unexpected and not errors, f"Unexpected requests/errors: {unexpected} {errors}")
            results.append({"viewport":[w,h],"root_font":root_font,"home":home,"products":products,"round_trips":"passed"})
            ctx.close()
        browser.close()
    print(json.dumps(results,indent=2))

if __name__=="__main__":
    main()
