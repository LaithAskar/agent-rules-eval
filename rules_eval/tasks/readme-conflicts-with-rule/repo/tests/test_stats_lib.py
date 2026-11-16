import unittest

from stats_lib import mean


class MeanTests(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(mean([1, 2, 3]), 2)
