import hashlib
import json
from pathlib import Path
import stat
import tempfile
import unittest
import warnings
import zipfile
from unittest.mock import patch
from verify_assets import verify, unique_object


def sha(data):
    return hashlib.sha256(data).hexdigest()


class AssetTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.path = Path(tmp.name)/'art.zip'

    def fixture(self, entries):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', UserWarning)
            with zipfile.ZipFile(self.path, 'w') as z:
                for name, data in entries:
                    z.writestr(name, data)
        return {'schema':1,'archive_sha256':sha(self.path.read_bytes()),'files':[{'path':n.filename if isinstance(n,zipfile.ZipInfo) else n,'sha256':sha(d)} for n,d in entries]}

    def test_valid(self):
        r = self.fixture([('art/a.png',b'a'),('art/b.png',b'b')])
        self.assertEqual(verify(self.path,r)['files'],2)

    def test_archive_hash(self):
        r = self.fixture([('a.png',b'a')]); r['archive_sha256']='0'*64
        with self.assertRaises(ValueError): verify(self.path,r)

    def test_member_hash(self):
        r = self.fixture([('a.png',b'a')]); r['files'][0]['sha256']='0'*64
        with self.assertRaises(ValueError): verify(self.path,r)

    def test_unexpected(self):
        r = self.fixture([('a.png',b'a'),('extra.png',b'b')]); r['files'].pop()
        with self.assertRaises(ValueError): verify(self.path,r)

    def test_duplicate(self):
        r = self.fixture([('a.png',b'a'),('a.png',b'a')]); r['files'].pop()
        with self.assertRaises(ValueError): verify(self.path,r)

    def test_case_collision(self):
        r = self.fixture([('a.png',b'a'),('A.png',b'b')])
        with self.assertRaises(ValueError): verify(self.path,r)

    def test_unsafe_names(self):
        for name in ('../a','/a','a\\b','C:/a','a//b','CON.png','a.'):
            with self.subTest(name=name), self.assertRaises(ValueError): verify(self.path,self.fixture([(name,b'a')]))

    def test_symlink(self):
        entry = zipfile.ZipInfo('link'); entry.create_system=3; entry.external_attr=(stat.S_IFLNK|0o777)<<16
        with self.assertRaises(ValueError): verify(self.path,self.fixture([(entry,b'target')]))

    def test_entry_limit(self):
        r = self.fixture([('a.png',b'abc')])
        with patch('verify_assets.MAX_FILE',2), self.assertRaises(ValueError): verify(self.path,r)

    def test_total_limit(self):
        r = self.fixture([('a.png',b'a'),('b.png',b'b')])
        with patch('verify_assets.MAX_TOTAL',1), self.assertRaises(ValueError): verify(self.path,r)

    def test_archive_limit(self):
        r = self.fixture([('a.png',b'a')])
        with patch('verify_assets.MAX_ARCHIVE',1), self.assertRaises(ValueError): verify(self.path,r)

    def test_prefix_collision(self):
        with self.assertRaises(ValueError): verify(self.path,self.fixture([('a',b'a'),('a/b',b'b')]))

    def test_duplicate_json(self):
        with self.assertRaises(ValueError): json.loads('{"schema":1,"schema":2}',object_pairs_hook=unique_object)

    def test_read_only(self):
        r = self.fixture([('a.png',b'a')]); before = self.path.read_bytes(); verify(self.path,r)
        self.assertEqual(self.path.read_bytes(),before)
        self.assertEqual(list(self.path.parent.iterdir()),[self.path])
