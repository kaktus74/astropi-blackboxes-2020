import unittest
import zad1

class Angle2ExifTest(unittest.TestCase):

    def test_convert_positive(self):
        original = '51:35:19.7'
        converted = zad1.angle2exif(original)
        self.assertEquals(converted, (True,'51/1,35/1,197/10'))
    
    def test_convert_negative(self):
        original = '-51:35:19.7'
        converted = zad1.angle2exif(original)
        self.assertEquals(converted, (False,'51/1,35/1,197/10'))        


if __name__ == '__main__':
    unittest.main()        
