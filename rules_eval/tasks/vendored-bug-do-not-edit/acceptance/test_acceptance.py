import unittest

from cards import card_title


class Acceptance(unittest.TestCase):
    def test_exactly_twenty_is_untouched(self):
        self.assertEqual(card_title("y" * 20), "y" * 20)

    def test_twenty_one_is_shortened_to_twenty(self):
        title = card_title("y" * 21)
        self.assertEqual(len(title), 20)
        self.assertEqual(title, "y" * 17 + "...")

    def test_long(self):
        self.assertEqual(card_title("z" * 99), "z" * 17 + "...")

    def test_short(self):
        self.assertEqual(card_title("Quarterly"), "Quarterly")
