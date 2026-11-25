import hashlib
import tempfile
import unittest
import warnings
import zipfile
from pathlib import Path
from verify_package import verify


def sha(data):
    return hashlib.sha256(data).hexdigest()


class PackageTests(unittest.TestCase):
    def setUp(self):
        tmp=tempfile.TemporaryDirectory(); self.addCleanup(tmp.cleanup)
        self.path=Path(tmp.name)/'fixture.apk'
        self.name='assets/branding/logo.png'

    def fixture(self, entries, manifest=True):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore',UserWarning)
            with zipfile.ZipFile(self.path,'w') as z:
                if manifest: z.writestr('AndroidManifest.xml',b'synthetic')
                for name,data in entries: z.writestr(name,data)
        return {'schema':1,'apk_sha256':sha(self.path.read_bytes()),'required':{self.name:sha(b'logo')},'exclusive_prefixes':['assets/branding/']}

    def test_valid(self):
        r=self.fixture([(self.name,b'logo'),('assets/other.txt',b'other')]); before=self.path.read_bytes()
        self.assertEqual(verify(self.path,r)['status'],'packaged_asset_bytes_match')
        self.assertEqual(self.path.read_bytes(),before)

    def test_wrong_package_hash(self):
        r=self.fixture([(self.name,b'logo')]); r['apk_sha256']='0'*64
        with self.assertRaises(ValueError): verify(self.path,r)

    def test_wrong_asset(self):
        with self.assertRaises(ValueError): verify(self.path,self.fixture([(self.name,b'changed')]))

    def test_missing(self):
        with self.assertRaises(ValueError): verify(self.path,self.fixture([]))

    def test_preview_leak(self):
        with self.assertRaises(ValueError): verify(self.path,self.fixture([(self.name,b'logo'),('assets/branding/preview.png',b'preview')]))

    def test_duplicate(self):
        with self.assertRaises(ValueError): verify(self.path,self.fixture([(self.name,b'logo'),(self.name,b'logo')]))

    def test_case_collision(self):
        with self.assertRaises(ValueError): verify(self.path,self.fixture([(self.name,b'logo'),(self.name.upper().replace('ASSETS/','assets/'),b'logo')]))

    def test_missing_manifest(self):
        with self.assertRaises(ValueError): verify(self.path,self.fixture([(self.name,b'logo')],False))

    def test_compiled_resource_rejected(self):
        r=self.fixture([(self.name,b'logo')]); r['required']={'res/drawable/icon.png':sha(b'logo')}
        with self.assertRaises(ValueError): verify(self.path,r)

    def test_traversal_receipt(self):
        r=self.fixture([(self.name,b'logo')]); r['required']={'assets/../logo.png':sha(b'logo')}
        with self.assertRaises(ValueError): verify(self.path,r)
