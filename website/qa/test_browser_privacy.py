import json
import tempfile
import unittest
from pathlib import Path
from browser_privacy import destination, observe, snapshot


class PrivacyFixtures(unittest.TestCase):
    def test_sanitize(self):
        self.assertEqual(destination("https://user:secret@example.invalid:8443/private?token=secret#secret"), "https://example.invalid:8443")
        self.assertEqual(destination("data:text/plain,secret"), "other")

    def test_runtime(self):
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "index.html").write_text("""<!doctype html><script>
            if (!sessionStorage.getItem('started')) {
              localStorage.setItem('private-key','private-value');
              sessionStorage.setItem('started','private-value');
              document.cookie='fixture=private-value';
            }
            fetch('https://example.invalid/private?token=private-value').catch(()=>{});
            const ws=new WebSocket('wss://example.invalid/private?token=private-value');
            ws.onerror=()=>{};
            </script>""", encoding="utf-8")
            def scenario(page, snapshots):
                page.wait_for_timeout(300)
                snapshots["before_delete"] = snapshot(page)
                page.evaluate("localStorage.clear()")
                snapshots["after_delete"] = snapshot(page)
            result = observe(tmp, scenario=scenario)
            self.assertEqual(result["status"], "observed")
            self.assertEqual(result["snapshots"]["before_delete"]["localStorageEntries"], 1)
            self.assertEqual(result["snapshots"]["after_delete"]["localStorageEntries"], 0)
            self.assertEqual(result["snapshots"]["reload"]["localStorageEntries"], 0)
            self.assertGreaterEqual(result["blocked_destinations"].get("https://example.invalid", 0), 1)
            self.assertGreaterEqual(result["blocked_destinations"].get("wss://example.invalid", 0), 1)
            for secret in ("private-key", "private-value", "/private", "token="):
                self.assertNotIn(secret, json.dumps(result))

    def test_invalid_entry(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                observe(tmp, "../index.html")

    def test_page_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "index.html").write_text("<script>throw Error('private-value')</script>")
            result = observe(tmp)
            self.assertEqual(result["status"], "failed")
            self.assertGreater(result["page_errors"], 0)
            self.assertNotIn("private-value", json.dumps(result))


if __name__ == "__main__":
    unittest.main()
