import unittest

from slug import slugify


class SlugifyTests(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(slugify("Hello World"), "hello-world")

    def test_digits(self):
        self.assertEqual(slugify("Python 3.12"), "python-3-12")
