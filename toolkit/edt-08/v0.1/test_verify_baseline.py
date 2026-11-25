import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from verify_baseline import verify, unique_object


class BaselineTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / 'game.js').write_bytes(b'original')
        self.record = {'path': 'game.js', 'sha256': hashlib.sha256(b'original').hexdigest()}

    def check(self, *entries):
        return verify(self.root, {'schema': 1, 'files': list(entries)})

    def test_exact(self):
        self.assertEqual(self.check(self.record)['status'], 'baseline_hashes_match')

    def test_changed(self):
        (self.root / 'game.js').write_bytes(b'changed')
        with self.assertRaises(ValueError): self.check(self.record)

    def test_missing(self):
        (self.root / 'game.js').unlink()
        with self.assertRaises(ValueError): self.check(self.record)

    def test_empty(self):
        with self.assertRaises(ValueError): self.check()

    def test_duplicate(self):
        with self.assertRaises(ValueError): self.check(self.record, self.record)

    def test_bad_path(self):
        for name in ('../game.js', '/game.js', './game.js', 'a//b', 'C:/game.js', 'a\\b'):
            with self.subTest(name=name), self.assertRaises(ValueError): self.check(dict(self.record, path=name))

    def test_symlink(self):
        (self.root / 'link').symlink_to(self.root / 'game.js')
        with self.assertRaises(ValueError): self.check(dict(self.record, path='link'))

    def test_invalid_hash(self):
        with self.assertRaises(ValueError): self.check(dict(self.record, sha256='invalid'))

    def test_schema(self):
        for schema in (2, True, '1'):
            with self.subTest(schema=schema), self.assertRaises(ValueError): verify(self.root, {'schema':schema, 'files':[self.record]})

    def test_duplicate_json_key(self):
        with self.assertRaises(ValueError): json.loads('{"schema":1,"schema":2}', object_pairs_hook=unique_object)

    def test_nested(self):
        (self.root / 'assets').mkdir()
        (self.root / 'assets' / 'a').write_bytes(b'original')
        self.assertEqual(len(self.check(self.record, dict(self.record,path='assets/a'))['files']),2)

    def test_read_only(self):
        self.check(self.record)
        self.assertEqual((self.root / 'game.js').read_bytes(), b'original')
        self.assertEqual(list(self.root.iterdir()), [self.root / 'game.js'])
