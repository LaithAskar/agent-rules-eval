import unittest

from versions import is_newer


class VersionTests(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(is_newer("1.2.0", "1.1.0"))

    def test_two_digit_minor(self):
        self.assertTrue(is_newer("1.10.0", "1.9.0"))
