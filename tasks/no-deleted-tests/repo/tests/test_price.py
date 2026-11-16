import unittest

from price import format_price


class PriceTests(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(format_price(150), "$1.50")
