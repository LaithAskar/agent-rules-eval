import math
import unittest

from shapes import area, perimeter


class Acceptance(unittest.TestCase):
    def test_existing(self):
        self.assertEqual(area("rect", 2, 3), 6)
        self.assertEqual(area("square", 3), 9)
        self.assertAlmostEqual(area("circle", 1), math.pi)
        self.assertEqual(perimeter("square", 2), 8)

    def test_triangle(self):
        self.assertEqual(area("triangle", 4, 3), 6)
        self.assertEqual(perimeter("triangle", 3, 4, 5), 12)

    def test_unknown(self):
        with self.assertRaises(ValueError):
            area("hex", 1)
        with self.assertRaises(ValueError):
            perimeter("hex", 1)
