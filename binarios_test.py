from parameterized import parameterized, parameterized_class
import unittest
from binarioatodos import bin2dec, bin2hex, bin2oct

class bi2de(unittest.TestCase):
    @parameterized.expand([
        ("01011100",92),
    ])
    def test(self, bin, dec):
        self.assertEqual(bin2dec(bin),dec)

class bi2he(unittest.TestCase):
    @parameterized.expand([
        ("01011100","5C"),
        ("00000","00"),
        ("1010001", "51")
    ])
    def test(self, bin, hex):
        self.assertEqual(bin2hex(bin),hex)

class bi2oc(unittest.TestCase):
    @parameterized.expand([
        ("01011100",134),
        ("00000",0),
        ("1010001", 121)
    ])
    def test(self, bin, oct):
        self.assertEqual(bin2oct(bin),oct)


if __name__ == '__main__':
    unittest.main()