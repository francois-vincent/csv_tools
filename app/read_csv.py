
from contextlib import contextmanager


@contextmanager
def abstract_file(file):
    if isinstance(file, str):
        yield open(file, 'r')
    else:
        yield file


class ReadCsv(object):

    def __init__(self, file_csv):
        self.list_record = []
        with abstract_file(file_csv) as f:
            index = 0
            for v in f:
                v = v.strip()
                if v:
                    v = v.split(';')
                    if index == 0:
                        self.list_header = v
                    else:
                        self.list_record.append(v)
                    index += 1

    def __iter__(self):
        return IterCsv(self, self.list_header, self.list_record)


class IterCsv(object):

    def __init__(self, list_header, list_record):
        self.ind = 0
        self.list_header = list_header
        self.list_record = list_record

    def __next__(self):
        try:
            dc = DictCsv(self.list_header, self.list_record[self.ind])
        except IndexError:
            raise StopIteration()
        self.ind += 1
        return dc


class DictCsv(dict):

     def __init__(self, headers, values):
         super().__init__(zip(headers, values))




