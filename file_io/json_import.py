import json


def json2arr(file):
    return json.load(file)


dataTestJson = [
    {
        "widget": {
            "debug": "on",
            "window": {
                "title": "Sample Konfabulator Widget",
                "name": "main_window",
                "width": 500,
                "height": 500,
            },
            "image": {
                "src": "Images/Sun.png",
                "name": "sun1",
                "hOffset": 250,
                "vOffset": 250,
                "alignment": "center",
            },
            "text": {
                "data": "Click Here",
                "size": 36,
                "style": "bold",
                "name": "text1",
                "hOffset": 250,
                "vOffset": 100,
                "alignment": "center",
                "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;",
            },
        }
    }
]


def test_json2arr():
    with open("./file_io/dataTest/dados.json") as f:
        assert json2arr(f) == dataTestJson
