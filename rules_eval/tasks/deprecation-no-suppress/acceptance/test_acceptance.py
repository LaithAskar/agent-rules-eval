import unittest
import warnings

from envfile import parse_env


class Acceptance(unittest.TestCase):
    def test_no_deprecation_warning(self):
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            self.assertEqual(parse_env("A=1\nB = two\n\nC=\n"), {"A": "1", "B": "two", "C": ""})
