import csv
import json

from Objects.link_object import Object


class Utility(object):

    def read_csv(self, path_file, delimiter='|'):
        list = []
        with open(path_file, 'r') as csvDataFile:
            csvReader = csv.reader(csvDataFile, delimiter=delimiter)
            next(csvReader, None)
            for l in csvReader:
                object = Object(l[0], l[1], l[2])
                list.append(object)
                print(object)
        return list





