import unittest

from pricing import apply_discount


class PricingTests(unittest.TestCase):
    def test_ten_percent_off(self):
        self.assertEqual(apply_discount(100, 10), 85)

    def test_zero_percent(self):
        self.assertEqual(apply_discount(80, 0), 80)
