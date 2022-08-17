import csv


def csv2arr(file, delimiter=","):
    result = []
    header, *data = csv.reader(file, delimiter=delimiter, quotechar='"')
    for i in data:
        ob = {}
        for j in range(len(header)):
            ob[header[j]] = i[j]
        result.append(ob)
    return result


def csv2arrV2(file):
    return [row for row in csv.DictReader(file)]
