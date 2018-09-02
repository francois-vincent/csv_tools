class ReadCsv(object):

    def __init__(self, file_csv):

        self.list_field = []

        with open(file_csv, 'r') as f:
            for c, v in enumerate(f):
                v = v.strip().split(';')
                if c == 0:
                    self.list_header = v
                else:
                    self.list_field.append(v)
