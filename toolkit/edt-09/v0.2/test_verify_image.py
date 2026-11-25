import hashlib
import io
import unittest
from PIL import Image
from verify_image import verify


def encode(im, fmt='PNG'):
    buf = io.BytesIO()
    im.save(buf, format=fmt)
    return buf.getvalue()


class ImageTests(unittest.TestCase):
    def setUp(self):
        self.im = Image.new('RGBA', (432,432))
        self.im.paste((255,200,20,255), (100,100,332,332))
        self.data = encode(self.im)

    def check(self, data=None, **kw):
        data = self.data if data is None else data
        args = dict(expected_hash=hashlib.sha256(data).hexdigest(), fmt='PNG', width=432, height=432, alpha='transparent', box=(100,100,332,332))
        args.update(kw)
        return verify(data, **args)

    def test_valid(self):
        self.assertEqual(self.check()['visible_bounds'], (100,100,332,332))

    def test_wrong_hash(self):
        with self.assertRaises(ValueError): self.check(expected_hash='0'*64)

    def test_wrong_dimensions(self):
        with self.assertRaises(ValueError): self.check(width=431)

    def test_wrong_encoding(self):
        with self.assertRaises(OSError): self.check(encode(self.im,'WEBP'))

    def test_webp(self):
        self.assertEqual(self.check(encode(self.im,'WEBP'),fmt='WEBP')['format'],'WEBP')

    def test_stray_pixel(self):
        self.im.putpixel((99,100),(0,0,0,1))
        with self.assertRaises(ValueError): self.check(encode(self.im))

    def test_blank(self):
        with self.assertRaises(ValueError): self.check(encode(Image.new('RGBA',(432,432))))

    def test_opaque_background(self):
        data = encode(Image.new('RGB',(432,432),(33,79,63)))
        self.assertEqual(self.check(data,alpha='opaque',box=None,color=(33,79,63))['status'],'image_contract_pass')

    def test_wrong_background(self):
        data = encode(Image.new('RGB',(432,432),(34,79,63)))
        with self.assertRaises(ValueError): self.check(data,alpha='opaque',box=None,color=(33,79,63))

    def test_invalid_box(self):
        with self.assertRaises(ValueError): self.check(box=(0,0,433,432))

    def test_animation(self):
        buf = io.BytesIO(); self.im.save(buf,format='PNG',save_all=True,append_images=[Image.new('RGBA',(432,432),(0,0,0,255))])
        with self.assertRaises(ValueError): self.check(buf.getvalue())

    def test_corrupt(self):
        with self.assertRaises((OSError,SyntaxError)): self.check(self.data[:50])
