class ReadCsv(object):

    def __init__(self):

        liste_entete = []
        liste_field = []
        meteo_csv = 'synop.2018090209.csv'

        f = open(meteo_csv, 'r')

        for i in enumerate(f):
            if i.count(0):
                liste_entete.append(i[1])
            liste_field.append([i[1]])
        f.close()
