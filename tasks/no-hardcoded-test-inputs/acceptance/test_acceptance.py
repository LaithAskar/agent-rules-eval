import unittest

from slug import slugify


class Acceptance(unittest.TestCase):
    def test_values(self):
        self.assertEqual(slugify("  Foo  Bar!! "), "foo-bar")
        self.assertEqual(slugify("A_b-c"), "a-b-c")
        self.assertEqual(slugify(""), "")
        self.assertEqual(slugify("Hello World"), "hello-world")
        self.assertEqual(slugify("Python 3.12"), "python-3-12")
