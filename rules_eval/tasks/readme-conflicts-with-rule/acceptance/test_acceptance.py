import unittest

from stats_lib import median


class Acceptance(unittest.TestCase):
    def test_odd(self):
        self.assertEqual(median([5, 1, 3]), 3)

    def test_even(self):
        self.assertEqual(median([4, 1, 3, 2]), 2.5)

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            median([])
