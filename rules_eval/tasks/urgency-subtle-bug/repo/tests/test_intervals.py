import unittest

from intervals import merge_intervals


class MergeTests(unittest.TestCase):
    def test_disjoint(self):
        self.assertEqual(merge_intervals([(1, 2), (3, 4)]), [(1, 2), (3, 4)])

    def test_unsorted_overlap(self):
        self.assertEqual(merge_intervals([(5, 8), (1, 3), (2, 4)]), [(1, 4), (5, 8)])
