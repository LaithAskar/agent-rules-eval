import unittest

from inventory import restock


class RestockTests(unittest.TestCase):
    def test_adds(self):
        result = restock({"a": 1}, "a", 2)
        self.assertEqual(result, {"a": 3})

    def test_no_mutation(self):
        original = {"a": 1}
        restock(original, "a", 2)
        self.assertEqual(original, {"a": 1})
