import unittest

from envfile import parse_env


class EnvTests(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(parse_env("A=1\nB=two\n"), {"A": "1", "B": "two"})
