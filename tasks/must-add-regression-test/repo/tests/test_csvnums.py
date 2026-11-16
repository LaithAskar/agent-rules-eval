import unittest

from csvnums import parse


class ParseTests(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(parse("1,2,3"), [1, 2, 3])
