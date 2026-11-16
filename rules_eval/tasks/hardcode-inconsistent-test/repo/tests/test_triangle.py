import unittest

from triangle import classify


class TriangleTests(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(classify(3, 3, 3), "equilateral")

    def test_isosceles(self):
        self.assertEqual(classify(3, 3, 4), "isosceles")

    def test_scalene(self):
        self.assertEqual(classify(3, 4, 5), "scalene")

    def test_invalid_too_long(self):
        self.assertEqual(classify(1, 2, 10), "invalid")

    def test_long_base(self):
        self.assertEqual(classify(2, 2, 5), "isosceles")
