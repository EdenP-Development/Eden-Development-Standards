import hashlib
import tempfile
import unittest
import warnings
import zipfile
from pathlib import Path
from verify_drawables import verify


class DrawableTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.path = Path(tmp.name) / 'test.apk'
        self.name = 'res/drawable-nodpi-v4/logo.png'
        self.data = b'\x89PNG\r\n\x1a\nsynthetic'

    def fixture(self, entries):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', UserWarning)
            with zipfile.ZipFile(self.path, 'w') as z:
                z.writestr('AndroidManifest.xml', b'test')
                for name, data in entries:
                    z.writestr(name, data)
        return {'schema': 1, 'apk_sha256': hashlib.sha256(self.path.read_bytes()).hexdigest(), 'drawables': {self.name: hashlib.sha256(self.data).hexdigest()}}

    def test_exact(self):
        r = self.fixture([(self.name, self.data)])
        before = self.path.read_bytes()
        self.assertEqual(verify(self.path, r)['status'], 'mapped_drawable_bytes_match')
        self.assertEqual(before, self.path.read_bytes())

    def test_missing(self):
        with self.assertRaises(ValueError): verify(self.path, self.fixture([]))

    def test_changed(self):
        with self.assertRaises(ValueError): verify(self.path, self.fixture([(self.name, b'changed')]))

    def test_duplicate(self):
        with self.assertRaises(ValueError): verify(self.path, self.fixture([(self.name, self.data)] * 2))

    def test_wrong_apk(self):
        r = self.fixture([(self.name, self.data)]); r['apk_sha256'] = '0' * 64
        with self.assertRaises(ValueError): verify(self.path, r)

    def test_case_collision(self):
        with self.assertRaises(ValueError): verify(self.path, self.fixture([(self.name, self.data), (self.name.upper(), self.data)]))

    def test_unsupported_path(self):
        r = self.fixture([(self.name, self.data)]); r['drawables'] = {'res/../logo.png': '0'*64}
        with self.assertRaises(ValueError): verify(self.path, r)

    def test_non_png(self):
        self.data = b'not png'
        with self.assertRaises(ValueError): verify(self.path, self.fixture([(self.name, self.data)]))
