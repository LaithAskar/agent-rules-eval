import unittest

from iters import flatten


class FlattenTests(unittest.TestCase):
    def test_flatten(self):
        self.assertEqual(flatten([[1], [2, 3]]), [1, 2, 3])
