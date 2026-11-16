import unittest

from prices import format_price


class PriceTests(unittest.TestCase):
    def test_whole(self):
        self.assertEqual(format_price(3), "$3.00")

    def test_float_edge(self):
        self.assertEqual(format_price(0.29), "$0.29")
