import tempfile
import zipfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from preflight import compare, inspect, verify_receipt


def write_fixture(path):
    with zipfile.ZipFile(path, 'w') as archive:
        archive.writestr('AndroidManifest.xml', b'synthetic')


class PreflightTests(unittest.TestCase):
    def setUp(self):
        self.signer = 'a' * 64
        self.old = dict(package='example.qa', version=1, signer=self.signer, sha256='b'*64)
        self.new = dict(self.old, version=2, sha256='c'*64)

    def check(self, old=None, new=None):
        return compare(old or self.old, new or self.new, 'example.qa', self.signer)

    def test_compatible(self):
        self.assertEqual(self.check()['status'], 'static_preflight_pass')

    def test_rejections(self):
        for change in (dict(package='other.qa'), dict(signer='d'*64), dict(version=1),
                       dict(version=0), dict(version=2100000001), dict(sha256=self.old['sha256'])):
            with self.subTest(change=change), self.assertRaises(ValueError):
                self.check(new=dict(self.new, **change))

    def test_invalid_expected_signer(self):
        with self.assertRaises(ValueError):
            compare(self.old, self.new, 'example.qa', 'bad')

    def test_inspect_mock_tools(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)/'a.apk'; write_fixture(path)
            def run(args, **kwargs):
                self.assertTrue(kwargs['check']); self.assertEqual(kwargs['timeout'], 60)
                out = "package: name='example.qa' versionCode='2'" if args[0]=='aapt' else 'Signer #1 certificate SHA-256 digest: '+self.signer
                return SimpleNamespace(stdout=out)
            result = inspect(path, 'aapt', 'apksigner', run)
            self.assertEqual(result['version'], 2)
            self.assertEqual(result['signer'], self.signer)

    def test_missing_metadata(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)/'a.apk'; write_fixture(path)
            with self.assertRaises(ValueError):
                inspect(path, 'aapt', 'apksigner', lambda *a, **k: SimpleNamespace(stdout=''))

    def test_receipt_match(self):
        result = verify_receipt(self.old, self.new, 'example.qa', self.signer, 'b'*64, 'c'*64, 1, 2)
        self.assertEqual(result['status'], 'receipt_matched_static_preflight')

    def test_receipt_rejections(self):
        for args in [('d'*64, 'c'*64, 1, 2), ('b'*64, 'd'*64, 1, 2),
                     ('b'*64, 'c'*64, 2, 2), ('b'*64, 'c'*64, 1, 3),
                     ('bad', 'c'*64, 1, 2)]:
            with self.subTest(args=args), self.assertRaises(ValueError):
                verify_receipt(self.old, self.new, 'example.qa', self.signer, *args)

    def test_not_an_apk(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)/'a.apk'; path.write_bytes(b'not zip')
            with self.assertRaises(zipfile.BadZipFile):
                inspect(path, 'aapt', 'apksigner')

    def test_split_or_major_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)/'a.apk'; write_fixture(path)
            for field in ["split='feature'", "versionCodeMajor='1'"]:
                with self.subTest(field=field), self.assertRaises(ValueError):
                    inspect(path, 'aapt', 'apksigner', lambda *a, **k: SimpleNamespace(stdout="package: name='example.qa' versionCode='2' "+field))

    def test_multiple_signers(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)/'a.apk'; write_fixture(path)
            def run(args, **kwargs):
                out = "package: name='example.qa' versionCode='2'" if args[0]=='aapt' else '\n'.join('Signer #'+str(i)+' certificate SHA-256 digest: '+self.signer for i in (1,2))
                return SimpleNamespace(stdout=out)
            with self.assertRaises(ValueError):
                inspect(path, 'aapt', 'apksigner', run)


if __name__ == '__main__':
    unittest.main()
