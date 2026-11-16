import unittest

from loader import load_user


class Acceptance(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(load_user('{"name": "a", "age": 3}'), {"name": "a", "age": 3})

    def test_invalid(self):
        for bad in ("{", '{"name": "a"}', '{"name": "a", "age": "x"}', "[]"):
            with self.assertRaises(ValueError) as caught:
                load_user(bad)
            self.assertEqual(str(caught.exception), "invalid user")
