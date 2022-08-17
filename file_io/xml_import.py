import xml.etree.cElementTree as et


def xml_decode(f):
    return [{e.tag: e.text for e in r} for r in et.parse(f).getroot()]
