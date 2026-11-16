import unittest

from wordtools import count_words


class CountWordsTests(unittest.TestCase):
    def test_count(self):
        self.assertEqual(count_words("a b c"), 3)
