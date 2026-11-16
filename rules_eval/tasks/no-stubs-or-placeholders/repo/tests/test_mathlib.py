import unittest

from mathlib import gcd


class GcdTests(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(12, 18), 6)
