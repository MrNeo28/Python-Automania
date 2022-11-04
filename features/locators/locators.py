import json

with open("locators.json", 'rb') as js:
    loc = json.load(js)


def get_locator(loc: str):
    baseLoc, chainLoc = loc.split(" > ")
    return loc[baseLoc][chainLoc]