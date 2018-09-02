from unittest import TestCase
from read_csv import DictCsv


class TestsCsv(TestCase):

    def test_dict(self):
        header = ['A', 'B', 'C']
        records = ['D', 'E', 'F']
        dc = DictCsv(header, records)
        self.assertEqual(dc, dict(zip(header, records)))


