class ReadCsv(object):

    def __init__(self, file_csv):

        self.list_header, self.list_field = [], []

        f = open(file_csv, 'r')

        for c, v in enumerate(f):
            if c == 0:
                self.list_header.append(v)
            else:
                self.list_field.append(v)
           # print(self.list_header)
        #print(self.list_field)


        # for i in enumerate(f):
        #
        #     if i.count(0):
        #         self.list_header.append(i[1])
        #     else:
        #         self.list_field.append([i[1]])
        #
        #     print(self.list_header)
        # print(self.list_field)
       # [ for i in enumerate(f) if i.count(0)  self.list_header.append(i[1])]
        f.close()
