import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from preflight import compare, inspect


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
            path = Path(folder)/'a.apk'; path.write_bytes(b'synthetic')
            def run(args, **kwargs):
                self.assertTrue(kwargs['check']); self.assertEqual(kwargs['timeout'], 60)
                out = "package: name='example.qa' versionCode='2'" if args[0]=='aapt' else 'Signer #1 certificate SHA-256 digest: '+self.signer
                return SimpleNamespace(stdout=out)
            result = inspect(path, 'aapt', 'apksigner', run)
            self.assertEqual(result['version'], 2)
            self.assertEqual(result['signer'], self.signer)

    def test_missing_metadata(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)/'a.apk'; path.write_bytes(b'synthetic')
            with self.assertRaises(ValueError):
                inspect(path, 'aapt', 'apksigner', lambda *a, **k: SimpleNamespace(stdout=''))

    def test_multiple_signers(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)/'a.apk'; path.write_bytes(b'synthetic')
            def run(args, **kwargs):
                out = "package: name='example.qa' versionCode='2'" if args[0]=='aapt' else '\n'.join('Signer #'+str(i)+' certificate SHA-256 digest: '+self.signer for i in (1,2))
                return SimpleNamespace(stdout=out)
            with self.assertRaises(ValueError):
                inspect(path, 'aapt', 'apksigner', run)


if __name__ == '__main__':
    unittest.main()
