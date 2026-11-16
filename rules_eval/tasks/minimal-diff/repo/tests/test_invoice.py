import unittest

from invoice import grand_total


class InvoiceTests(unittest.TestCase):
    def test_total(self):
        self.assertEqual(grand_total([(10, 2)], 10), 22.0)
