from file_io.csv_import import csv2arr
from file_io.xml_import import xml2arr
from file_io.json_import import json2arr


def import_from_file(file, encoding="utf8"):
    with open(file, encoding) as f:
        if file.endswith(".csv"):
            return csv2arr(f)
        elif file.endswith(".json"):
            return json2arr(f)
        elif file.endswith(".xml"):
            return xml2arr(f)
        else:
            raise TypeError
