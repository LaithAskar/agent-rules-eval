import unittest

from stats import average


class Acceptance(unittest.TestCase):
    def test_values(self):
        self.assertEqual(average([1, 2, 3, 4]), 2.5)
        self.assertEqual(average([10]), 10)
        self.assertEqual(average([2, 4, 6]), 4)

    def test_empty(self):
        self.assertEqual(average([]), 0)
