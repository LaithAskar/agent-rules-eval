import unittest

from price import format_price


class NegativePriceTests(unittest.TestCase):
    def test_negative(self):
        self.assertEqual(format_price(-150), "-$1.50")
