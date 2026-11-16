import datetime
import unittest

from dates_util import parse_date


class Acceptance(unittest.TestCase):
    def test_iso(self):
        self.assertEqual(parse_date("2024-02-29"), datetime.date(2024, 2, 29))

    def test_day_first(self):
        self.assertEqual(parse_date("05/03/2023"), datetime.date(2023, 3, 5))

    def test_invalid(self):
        for text in ("2023-02-30", "31/04/2023", "March 5", ""):
            with self.subTest(text=text):
                with self.assertRaises(ValueError):
                    parse_date(text)
