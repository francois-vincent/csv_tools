class ReadCsv(object):

    def __init__(self, file_csv):

        self.list_record = []

        with open(file_csv, 'r') as f:
            for c, v in enumerate(f):
                v = v.strip().split(';')
                if c == 0:
                    self.list_header = v
                else:
                    self.list_record.append(v)

    def __iter__(self):
        return IterCsv(self)


class IterCsv(object):

    def __init__(self, obj_csv):

        pass

    def __next__(self):
        pass



class DictCsv(dict):

     def __init__(self, headers, values):
         super().__init__(zip(headers, values))




