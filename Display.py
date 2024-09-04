import json

URLJSON = dict()

with open('SiteDataJSON.json') as f:
    URLJSON = json.load(f)
    #print(URLJSON)

def mainDictToList():
    newList = []
    for i in URLJSON:
        newList.append(i["Name"])
    return newList

def displaySelectionList(itemeList: list, menuName: str):
    print(f"-----{menuName}-----")
    for i in range(len(itemeList)):
        print(f"{i} - {itemeList[i]}")
    return input("> ")

 
displaySelectionList(mainDictToList(), "main")