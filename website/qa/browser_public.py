"""Render the current public checkout locally; never navigate to external stores."""
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from threading import Thread
from playwright.sync_api import sync_playwright
import json
import sys

ROOT = Path(__file__).resolve().parents[1] / "public"
CASES = [(320,640,16),(390,844,16),(768,1024,16),(1440,900,16),(320,640,32),(390,844,32)]
def main():
    server = ThreadingHTTPServer(("127.0.0.1",0), partial(SimpleHTTPRequestHandler,directory=str(ROOT)))
    Thread(target=server.serve_forever,daemon=True).start()
    origin = f"http://127.0.0.1:{server.server_port}/"
    results = []
    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch()
            for w,h,font in CASES:
                context = browser.new_context(viewport={"width":w,"height":h},service_workers="block")
                context.route("**/*", lambda r: r.continue_() if r.request.url.startswith(origin) else r.abort())
                for path in sorted(ROOT.glob("*.html")):
                    page = context.new_page()
                    errors = []
                    page.on("pageerror",lambda e: errors.append(str(e)))
                    try:
                        response = page.goto(origin+path.name,wait_until="load",timeout=15000)
                        assert response and response.ok, "HTML request failed"
                        page.evaluate("(n)=>document.documentElement.style.fontSize=n+'px'",font)
                        page.evaluate("Promise.all([...document.images].map(i=>i.decode()))")
                        stats = page.evaluate("""()=>({
                          width:document.documentElement.clientWidth,
                          scroll:document.documentElement.scrollWidth,
                          css:[...document.styleSheets].some(s=>s.href?.endsWith('/style.css') && s.cssRules.length>0),
                          images:[...document.images].every(i=>i.naturalWidth>0),
                          imageCount:document.images.length,
                          main:!!document.querySelector('main#main'),
                          smallTargets:[...document.querySelectorAll('nav a,.action')].filter(a=>a.getBoundingClientRect().height<44).length
                        })""")
                        assert stats["scroll"]<=stats["width"]+1, f"Horizontal overflow: {stats}"
                        assert stats["css"] and stats["images"] and stats["main"], f"Resource failure: {stats}"
                        page.keyboard.press("Tab")
                        assert page.evaluate("document.activeElement.classList.contains('skip')"), "Skip link not first focus"
                        page.keyboard.press("Enter")
                        assert page.evaluate("document.activeElement.id==='main'"), "Skip target not focused"
                        assert not errors, str(errors)
                        results.append({"page":path.name,"viewport":[w,h],"root_font":font,"status":"pass",**stats})
                    except Exception as e:
                        results.append({"page":path.name,"viewport":[w,h],"root_font":font,"status":"fail","error":str(e)})
                    finally:
                        page.close()
                context.close()
            browser.close()
    finally:
        server.shutdown()
        server.server_close()
    failures = [r for r in results if r["status"]=="fail"]
    print(json.dumps({"cases":len(results),"failures":len(failures),"results":results},indent=2))
    return bool(failures)
if __name__ == "__main__":
    sys.exit(main())
