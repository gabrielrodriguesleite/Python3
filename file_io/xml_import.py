import xml.etree.cElementTree as et


def xml2arr(f):
    return [{e.tag: e.text for e in r} for r in et.parse(f).getroot()]


dataTestXML = [
    {},
    {"name": "main_window", "width": "500", "height": "500"},
    {"hOffset": "250", "vOffset": "250", "alignment": "center"},
    {
        "name": "text1",
        "hOffset": "250",
        "vOffset": "100",
        "alignment": "center",
        "onMouseUp": "\n            sun1.opacity = (sun1.opacity / 100) * 90;\n        ",
    },
]


def test_xml2arr():
    with open("./file_io/dataTest/dados.xml") as f:
        assert xml2arr(f) == dataTestXML


"""
TODO:
- parece que a função apenas decodifica o primeiro nível
"""
