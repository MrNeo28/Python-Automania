import json

json_path = "page_objects/locators/locators.json"


def get_locator(locator: str):
    
    with open(json_path, 'r') as js:
        loc = json.load(js)

    baseLoc, chainLoc = locator.split(" > ")
    return loc[baseLoc][chainLoc]

print(get_locator('wiki > searchBox'))

