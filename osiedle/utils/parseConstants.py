import json


def parseConstants():
    with open("./settings.json", "r") as f:
        return json.load(f)
