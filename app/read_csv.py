class ReadCsv(object):

    def __init__(self, file_csv):

        self.list_field = []

        f = open(file_csv, 'r')

        for c, v in enumerate(f):
            if c == 0:
                self.list_header = v.strip().split(';')
            else:
                self.list_field.append(v.strip().split(';'))

        f.close()
