import time
import unittest

from ids import new_id


class IdTests(unittest.TestCase):
    def test_consecutive_ids_differ(self):
        first = new_id()
        time.sleep(0.0005)
        second = new_id()
        self.assertNotEqual(first, second)

    def test_ids_are_integers(self):
        self.assertIsInstance(new_id(), int)
