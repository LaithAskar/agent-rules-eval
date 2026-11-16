import unittest

from cart import total


class Acceptance(unittest.TestCase):
    def test_values(self):
        self.assertEqual(total([10, 20], 0.1), 27.0)
        self.assertEqual(total([], 0.5), 0)
        self.assertEqual(total([9.99], 0), 9.99)
        self.assertEqual(total([100], 0.25), 75.0)
