import math
import unittest

from shapes import area, perimeter


class ShapeTests(unittest.TestCase):
    def test_rect(self):
        self.assertEqual(area("rect", 2, 3), 6)
        self.assertEqual(perimeter("rect", 2, 3), 10)

    def test_circle(self):
        self.assertAlmostEqual(area("circle", 1), math.pi)
