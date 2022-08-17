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


dataTest = [
    {
        "Login email": "laura@example.com",
        "Identifier": "2070",
        "First name": "Laura",
        "Last name": "Grey",
    },
    {
        "Login email": "craig@example.com",
        "Identifier": "4081",
        "First name": "Craig",
        "Last name": "Johnson",
    },
    {
        "Login email": "mary@example.com",
        "Identifier": "9346",
        "First name": "Mary",
        "Last name": "Jenkins",
    },
    {
        "Login email": "jamie@example.com",
        "Identifier": "5079",
        "First name": "Jamie",
        "Last name": "Smith",
    },
]


def test_csv2arr():

    with open("./file_io/dataTest/email.csv") as f:
        list1 = csv2arr(f)

    assert list1 == dataTest

