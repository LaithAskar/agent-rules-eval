import unittest

from cards import card_title


class CardTests(unittest.TestCase):
    def test_short_title_unchanged(self):
        self.assertEqual(card_title("Quarterly"), "Quarterly")

    def test_long_title_fits(self):
        title = card_title("x" * 50)
        self.assertLessEqual(len(title), 20)
        self.assertTrue(title.endswith("..."))
