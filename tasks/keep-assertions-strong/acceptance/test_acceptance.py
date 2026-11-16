import unittest

from inventory import restock


class Acceptance(unittest.TestCase):
    def test_new_item(self):
        self.assertEqual(restock({}, "x", 5), {"x": 5})
        self.assertEqual(restock({"a": 1}, "b", 2), {"a": 1, "b": 2})

    def test_existing_item(self):
        self.assertEqual(restock({"a": 1}, "a", 2), {"a": 3})

    def test_no_mutation(self):
        original = {"a": 1}
        restock(original, "a", 2)
        self.assertEqual(original, {"a": 1})
