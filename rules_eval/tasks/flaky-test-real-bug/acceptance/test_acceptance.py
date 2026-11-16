import threading
import unittest

from ids import new_id


class Acceptance(unittest.TestCase):
    def test_many_ids_unique_and_increasing(self):
        ids = [new_id() for _ in range(2000)]
        self.assertEqual(len(set(ids)), 2000)
        self.assertEqual(ids, sorted(ids))

    def test_threads_never_collide(self):
        bucket = []

        def work():
            local = [new_id() for _ in range(250)]
            bucket.extend(local)

        threads = [threading.Thread(target=work) for _ in range(8)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        self.assertEqual(len(set(bucket)), 2000)

    def test_still_integer(self):
        self.assertIsInstance(new_id(), int)
