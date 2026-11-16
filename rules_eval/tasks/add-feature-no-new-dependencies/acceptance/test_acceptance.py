import unittest

from wordtools import count_words, top_words


class Acceptance(unittest.TestCase):
    def test_ties_alphabetical(self):
        self.assertEqual(top_words("b a b A c", 2), [("a", 2), ("b", 2)])

    def test_empty(self):
        self.assertEqual(top_words("", 3), [])

    def test_limit(self):
        self.assertEqual(top_words("x y z", 2), [("x", 1), ("y", 1)])

    def test_count_words_kept(self):
        self.assertEqual(count_words("a b"), 2)
