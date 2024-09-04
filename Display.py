import json

URLJSON = dict()

with open('SiteDataJSON.json') as f:
    URLJSON = json.load(f)
    #print(URLJSON)

t = {"v":1, "b": 2}

print(t["v"])
def displaySelectionList(itemeList: list, menuName: str):
    print(f"-----{menuName}-----")
    for i in range(len(itemeList)):
        print(f"{i} - {itemeList[i]['Name']}")

displaySelectionList(URLJSON, "main")