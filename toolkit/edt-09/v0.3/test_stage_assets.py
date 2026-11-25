import hashlib
import io
import tempfile
import unittest
from pathlib import Path
import zipfile
from PIL import Image
from stage_assets import stage


class StageTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory(); self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name); self.archive = self.root/'art.zip'; self.dest = self.root/'staged'
        buf = io.BytesIO(); Image.new('RGB',(8,8),(33,79,63)).save(buf,format='PNG'); self.data = buf.getvalue()
        with zipfile.ZipFile(self.archive,'w') as z:
            z.writestr('art/a.png',self.data); z.writestr('art/b.png',self.data)
        sha = lambda data: hashlib.sha256(data).hexdigest()
        self.receipt = {'schema':1,'archive_sha256':sha(self.archive.read_bytes()),'files':[{'path':n,'sha256':sha(self.data)} for n in ('art/a.png','art/b.png')]}
        self.item = dict(source='art/a.png',name='selected.png',format='PNG',width=8,height=8,alpha='opaque',box=None,color=[33,79,63])

    def run_stage(self,*items):
        return stage(self.archive,self.receipt,{'schema':1,'images':list(items)},self.dest)

    def reject(self,*items):
        with self.assertRaises(ValueError): self.run_stage(*items)
        self.assertFalse(self.dest.exists())

    def test_selected_only(self):
        before=self.archive.read_bytes(); r=self.run_stage(self.item)
        self.assertEqual(r['status'],'staged_not_release_approved')
        self.assertEqual({p.name for p in self.dest.iterdir()},{'selected.png','manifest.json'})
        self.assertEqual((self.dest/'selected.png').read_bytes(),self.data)
        self.assertEqual(self.archive.read_bytes(),before)

    def test_existing(self):
        self.dest.mkdir(); (self.dest/'keep').write_text('safe')
        with self.assertRaises(ValueError): self.run_stage(self.item)
        self.assertEqual((self.dest/'keep').read_text(),'safe')

    def test_wrong_hash(self):
        self.receipt['archive_sha256']='0'*64; self.reject(self.item)

    def test_wrong_dimensions(self): self.reject(dict(self.item,width=9))
    def test_unknown_source(self): self.reject(dict(self.item,source='unknown.png'))
    def test_unsafe_name(self): self.reject(dict(self.item,name='../out.png'))
    def test_wrong_extension(self): self.reject(dict(self.item,name='out.webp'))
    def test_duplicate_source(self): self.reject(self.item,dict(self.item,name='other.png'))
    def test_duplicate_name(self): self.reject(self.item,dict(self.item,source='art/b.png',name='SELECTED.PNG'))
    def test_all_validate_before_write(self): self.reject(self.item,dict(self.item,source='art/b.png',name='b.png',width=9))
    def test_empty(self): self.reject()
    def test_symlink_destination(self):
        self.dest.symlink_to(self.root/'missing')
        with self.assertRaises(ValueError): self.run_stage(self.item)
        self.assertTrue(self.dest.is_symlink())
