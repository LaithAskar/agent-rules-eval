import unittest

from stats import average


class AverageTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(average([]), 0)

    def test_single(self):
        self.assertEqual(average([5]), 5)
