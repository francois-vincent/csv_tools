from unittest import TestCase
from io import StringIO

from read_csv import DictCsv, IterCsv, ReadCsv


class TestsCsv(TestCase):

    def test_dict(self):
        header = ['A', 'B', 'C']
        records = ['D', 'E', 'F']
        dc = DictCsv(header, records)
        self.assertEqual(dc, dict(zip(header, records)))

    def test_iterator(self):
        header = ['A', 'B', 'C']
        records = [['D', 'E', 'F']]
        it = IterCsv(header, records)
        self.assertEqual(next(it), dict(zip(header, records[0])))
        self.assertRaises(StopIteration, next, it)

    def test_iterable(self):
        file = StringIO("\nA;B;C\n\nD;E;F\n\n")
        rc = ReadCsv(file)
        self.assertEqual(rc.list_header, ['A', 'B', 'C'])
        self.assertEqual(rc.list_record, [['D', 'E', 'F']])
