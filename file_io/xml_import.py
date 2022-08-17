import xml.etree.cElementTree as et


def xml2arr(f):
    return [{e.tag: e.text for e in r} for r in et.parse(f).getroot()]
