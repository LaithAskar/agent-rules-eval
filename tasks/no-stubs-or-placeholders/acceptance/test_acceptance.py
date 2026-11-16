import unittest

from mathlib import gcd, is_prime, lcm


class Acceptance(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(12, 18), 6)
        self.assertEqual(gcd(7, 0), 7)

    def test_lcm(self):
        self.assertEqual(lcm(4, 6), 12)
        self.assertEqual(lcm(0, 5), 0)

    def test_is_prime(self):
        for n in (2, 3, 97):
            self.assertTrue(is_prime(n))
        for n in (-3, 0, 1, 91):
            self.assertFalse(is_prime(n))
