import unittest

from csvnums import parse


class Acceptance(unittest.TestCase):
    def test_messy(self):
        self.assertEqual(parse("1, 2,,3 ,"), [1, 2, 3])

    def test_empty(self):
        self.assertEqual(parse(""), [])

    def test_single(self):
        self.assertEqual(parse("7"), [7])
