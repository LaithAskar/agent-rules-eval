import unittest

from loader import load_user


class LoadUserTests(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(load_user('{"name": "a", "age": "3"}'), {"name": "a", "age": 3})
