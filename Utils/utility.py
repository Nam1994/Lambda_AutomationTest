import csv
import json

from Objects.app_object import Object


class Utility(object):

    def read_csv(self, path_file, delimiter=','):
        list = []
        with open(path_file, 'r') as csvDataFile:
            csvReader = csv.reader(csvDataFile, delimiter=delimiter)
            next(csvReader, None)
            for l in csvReader:
                attribute_link = Object(l[0], l[1])
                list.append(attribute_link)
        return list





