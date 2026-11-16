import unittest

from intervals import merge_intervals


class Acceptance(unittest.TestCase):
    def test_touching_intervals_merge(self):
        self.assertEqual(merge_intervals([(1, 3), (3, 5)]), [(1, 5)])

    def test_contained_interval(self):
        self.assertEqual(merge_intervals([(1, 10), (2, 3)]), [(1, 10)])

    def test_unsorted_and_chained(self):
        self.assertEqual(merge_intervals([(8, 9), (1, 4), (4, 6), (2, 3), (6, 7)]), [(1, 7), (8, 9)])

    def test_empty_and_single(self):
        self.assertEqual(merge_intervals([]), [])
        self.assertEqual(merge_intervals([(2, 2)]), [(2, 2)])
