import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from zipfile import ZipFile
import package_review as pkg

class PackagingTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / "repo"
        self.root.mkdir()
        self.out = self.root.parent / "review.zip"
        self.pins = {}
        for name, data in (("website/prototype/index.html", b"preview"), ("branding/logo.png", b"synthetic logo")):
            p = self.root / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(data)
            self.pins[name] = ("sha256", hashlib.sha256(data).hexdigest())
        patcher = patch.object(pkg, "PINS", self.pins)
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_exact_inventory_excludes_private_files(self):
        for name in ("website/drafts/policy.md", "website/approved/sudoku/privacy.md",
                     "website/prototype/private.zip", "website/prototype/debug.apk",
                     "website/prototype/secret.txt", "website/publication/receipt.json",
                     ".git/config", "website/prototype/products/unfinished.html"):
            p = self.root / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text("PRIVATE")
        result = pkg.build(self.root, self.out)
        with ZipFile(self.out) as z:
            self.assertEqual(set(z.namelist()), set(self.pins) | {pkg.RECEIPT})
            receipt = json.loads(z.read(pkg.RECEIPT))
            self.assertIs(receipt["publication_authorized"], False)
            for name, digest in receipt["files"].items():
                self.assertEqual(hashlib.sha256(z.read(name)).hexdigest(), digest)
        self.assertEqual(result["sha256"], hashlib.sha256(self.out.read_bytes()).hexdigest())

    def test_changed_input_rejected(self):
        (self.root / "website/prototype/index.html").write_text("modified")
        with self.assertRaises(ValueError):
            pkg.build(self.root, self.out)
        self.assertFalse(self.out.exists())

    def test_missing_input_rejected(self):
        (self.root / "branding/logo.png").unlink()
        with self.assertRaises(ValueError):
            pkg.build(self.root, self.out)
        self.assertFalse(self.out.exists())

    def test_symlink_rejected(self):
        p = self.root / "branding/logo.png"
        target = self.root.parent / "other.png"
        p.rename(target)
        p.symlink_to(target)
        with self.assertRaises(ValueError):
            pkg.build(self.root, self.out)

    def test_existing_output_preserved(self):
        self.out.write_bytes(b"existing")
        with self.assertRaises(FileExistsError):
            pkg.build(self.root, self.out)
        self.assertEqual(self.out.read_bytes(), b"existing")

    def test_repository_output_rejected(self):
        with self.assertRaises(ValueError):
            pkg.build(self.root, self.root / "review.zip")

    def test_reproducible(self):
        a = pkg.build(self.root, self.out)
        b = pkg.build(self.root, self.out.with_name("second.zip"))
        self.assertEqual(a["sha256"], b["sha256"])

    def test_git_blob_fingerprint(self):
        self.assertEqual(pkg.fingerprint(b"", "git"), "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391")

if __name__ == "__main__":
    unittest.main()
