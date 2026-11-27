import copy
import hashlib
import tempfile
import unittest
from pathlib import Path
from validate_publication import validate, CHECKS

class GateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.record = dict(schema=1, product="fixture", channel="synthetic",
            version="1", source_revision="a"*40, apk_sha256="b"*64,
            publisher="Synthetic publisher", contact="qa@fixture.example",
            private_reporting_contact="security@fixture.example",
            effective_date="2026-11-27", checks=dict.fromkeys(CHECKS, True),
            publication_authorized=True)
        for kind in ("privacy", "support"):
            name = f"website/approved/fixture/{kind}.md"
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            data = ("Publisher: Synthetic publisher\nContact: qa@fixture.example\nEffective date: 2026-11-27\nCanonical URL: https://fixture.example/"+kind+"\n"+("Private reporting contact: security@fixture.example\n" if kind=="support" else "")+"Synthetic test content only.\n").encode()
            path.write_bytes(data)
            self.record.update({kind+"_file":name, kind+"_sha256":hashlib.sha256(data).hexdigest(),
                                kind+"_url":"https://fixture.example/"+kind})

    def test_complete_synthetic_receipt(self):
        self.assertEqual(validate(self.record,self.root,fixture=True), [])
    def test_fixture_rejected_by_production(self):
        self.assertTrue(validate(self.record,self.root))
    def test_fixture_cannot_use_real_product(self):
        self.record["product"]="sudoku"
        self.assertTrue(validate(self.record,self.root,fixture=True))
    def test_content_metadata_mismatch(self):
        self.record["publisher"]="Different publisher"
        self.assertTrue(validate(self.record,self.root,fixture=True))
    def test_duplicate_metadata(self):
        p=self.root/self.record["privacy_file"]
        data=p.read_bytes()+b"Publisher: Different publisher\n"
        p.write_bytes(data)
        self.record["privacy_sha256"]=hashlib.sha256(data).hexdigest()
        self.assertTrue(validate(self.record,self.root,fixture=True))
    def test_production_host_rejections(self):
        from validate_publication import valid_host
        for h in ("fixture.example","sub.example.com","127.0.0.1","localhost","a.local","a.internal","-bad.com","bad_.com","good.com."):
            with self.subTest(host=h):
                self.assertFalse(valid_host(h))
        self.assertTrue(valid_host("publisher.examplebusiness.com"))
    def test_empty(self):
        self.assertTrue(validate({},self.root))
    def test_missing_approval(self):
        self.record["publication_authorized"]=False
        self.assertTrue(validate(self.record,self.root,fixture=True))
    def test_each_check_required(self):
        for key in CHECKS:
            with self.subTest(key=key):
                r=copy.deepcopy(self.record)
                r["checks"][key]="true"
                self.assertTrue(validate(r,self.root,fixture=True))
    def test_draft_path(self):
        self.record["privacy_file"]="website/drafts/sudoku-privacy.md"
        self.assertTrue(validate(self.record,self.root,fixture=True))
    def test_changed_bytes(self):
        (self.root/self.record["privacy_file"]).write_text("Changed")
        self.assertTrue(validate(self.record,self.root,fixture=True))
    def test_draft_even_with_matching_hash(self):
        data=b"PREPUBLICATION DRAFT"
        (self.root/self.record["privacy_file"]).write_bytes(data)
        self.record["privacy_sha256"]=hashlib.sha256(data).hexdigest()
        self.assertTrue(validate(self.record,self.root,fixture=True))
    def test_unsafe_url(self):
        for url in ("http://fixture.example/privacy","https://example.com/privacy","https://user@fixture.example/privacy","https://fixture.example/privacy?token=x"):
            with self.subTest(url=url):
                r=dict(self.record,privacy_url=url)
                self.assertTrue(validate(r,self.root,fixture=True))
    def test_placeholder_contact(self):
        self.record["contact"]="support@example.com"
        self.assertTrue(validate(self.record,self.root,fixture=True))
    def test_symlink(self):
        p=self.root/self.record["privacy_file"]
        target=self.root/"elsewhere.md"
        p.rename(target)
        p.symlink_to(target)
        self.assertTrue(validate(self.record,self.root,fixture=True))
    def test_invalid_date(self):
        self.record["effective_date"]="2026-02-30"
        self.assertTrue(validate(self.record,self.root,fixture=True))

if __name__ == "__main__":
    unittest.main()
