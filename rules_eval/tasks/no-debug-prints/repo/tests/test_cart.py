import unittest

from cart import total


class TotalTests(unittest.TestCase):
    def test_discount(self):
        self.assertEqual(total([10, 20], 0.1), 27.0)
