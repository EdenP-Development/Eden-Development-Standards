"""Blocked-egress browser observation for trusted, unpacked QA fixtures.
Not a sandbox, packet capture, hosted embed audit or privacy certification.
"""
import argparse
import json
import threading
from collections import Counter
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

from playwright.sync_api import sync_playwright


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_):
        pass


def destination(url):
    """Never retain paths, userinfo, query strings, fragments or payloads."""
    try:
        p = urlsplit(url)
        if p.scheme not in ("http", "https", "ws", "wss") or not p.hostname:
            return "other"
        host = p.hostname
        if ":" in host:
            host = "[" + host + "]"
        return p.scheme + "://" + host + (":" + str(p.port) if p.port else "")
    except ValueError:
        return "invalid"


def snapshot(page):
    return page.evaluate("""async () => {
      const count = f => {try {return f()} catch (_) {return null}};
      const asyncCount = async f => {try {return await f()} catch (_) {return null}};
      return {
        localStorageEntries: count(() => localStorage.length),
        sessionStorageEntries: count(() => sessionStorage.length),
        visibleCookieCount: count(() => document.cookie ? document.cookie.split(';').length : 0),
        indexedDBCount: await asyncCount(async () => (await indexedDB.databases()).length),
        cacheCount: await asyncCount(async () => (await caches.keys()).length)
      };
    }""")


def observe(root, entry="index.html", scenario=None):
    root = Path(root).resolve()
    if not root.is_dir() or any(p.is_symlink() for p in root.rglob("*")):
        raise ValueError("Use a trusted unpacked directory without symlinks")
    if not (root / entry).is_file() or Path(entry).is_absolute() or ".." in Path(entry).parts:
        raise ValueError("Invalid entry")
    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(root)))
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    origin = f"http://127.0.0.1:{server.server_port}"
    attempts = Counter()
    local_failures = 0
    errors = 0
    report = {"scope": "trusted-local-blocked-egress", "snapshots": {},
              "limitations": ["Not packet capture or an OS network sandbox",
              "Service workers blocked; WebRTC, DNS and browser-level traffic not measured",
              "Storage counts only; top-level page only; no hosted embed or online audit"]}
    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch()
            report["browser"] = browser.version
            context = browser.new_context(service_workers="block")
            def route_request(route):
                dest = destination(route.request.url)
                if dest == origin:
                    route.continue_()
                else:
                    attempts[dest] += 1
                    route.abort()
            context.route("**/*", route_request)
            def route_socket(ws):
                attempts[destination(ws.url)] += 1
                ws.close()
            context.route_web_socket("**/*", route_socket)
            def failed(req):
                nonlocal local_failures
                if destination(req.url) == origin:
                    local_failures += 1
            context.on("requestfailed", failed)
            def attach(page):
                def error(_):
                    nonlocal errors
                    errors += 1
                page.on("pageerror", error)
            context.on("page", attach)
            page = context.new_page()
            try:
                response = page.goto(origin + "/" + entry, wait_until="load", timeout=15000)
                if not response or not response.ok:
                    raise RuntimeError("Entry load failed")
                report["snapshots"]["load"] = snapshot(page)
                if scenario:
                    scenario(page, report["snapshots"])
                page.reload(wait_until="load", timeout=15000)
                report["snapshots"]["reload"] = snapshot(page)
                report["status"] = "observed"
            except Exception:
                report["status"] = "failed"
            finally:
                context.close()
                browser.close()
    finally:
        server.shutdown()
        server.server_close()
        thread.join()
    report["blocked_destinations"] = dict(sorted(attempts.items()))
    report["local_request_failures"] = local_failures
    report["page_errors"] = errors
    if errors or local_failures:
        report["status"] = "failed"
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root")
    parser.add_argument("--entry", default="index.html")
    args = parser.parse_args()
    result = observe(args.root, args.entry)
    print(json.dumps(result, indent=2))
    raise SystemExit(result["status"] != "observed")
