def csv_decode(file):
    result = []
    header, *data = csv.reader(file, delimiter=",", quotechar='"')
    for i in data:
        ob = {}
        for j in range(len(header)):
            ob[header[j]] = i[j]
        result.append(ob)
    return result