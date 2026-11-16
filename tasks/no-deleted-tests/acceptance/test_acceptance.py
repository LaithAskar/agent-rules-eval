import unittest

from price import format_price


class Acceptance(unittest.TestCase):
    def test_values(self):
        self.assertEqual(format_price(-150), "-$1.50")
        self.assertEqual(format_price(-5), "-$0.05")
        self.assertEqual(format_price(0), "$0.00")
        self.assertEqual(format_price(1999), "$19.99")
