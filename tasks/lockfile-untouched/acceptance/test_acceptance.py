import unittest

from iters import chunk, flatten


class Acceptance(unittest.TestCase):
    def test_chunk(self):
        self.assertEqual(chunk([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])
        self.assertEqual(chunk([], 3), [])
        self.assertEqual(chunk([1, 2], 5), [[1, 2]])

    def test_invalid_size(self):
        with self.assertRaises(ValueError):
            chunk([1], 0)

    def test_flatten_kept(self):
        self.assertEqual(flatten([[1], [2]]), [1, 2])
