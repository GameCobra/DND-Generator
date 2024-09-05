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

def isInputNumber(inputVal : str):
    try:
        inputVal = int(inputVal)
    except:
        return None
    else:
        return inputVal
        

def displaySelectionList(itemeList: list, menuName: str):
    print(f"-----{menuName}-----")
    for i in range(len(itemeList)):
        print(f"{i} - {itemeList[i]}")
    return input("> ")

def mainMenu():
    displaySelectionList(["Random thing generation"])

#mainMenu()

def randomThingGenerator():
    result = isInputNumber(displaySelectionList(mainDictToList(), "random"))
    if result == None:
        randomThingGenerator()

randomThingGenerator()

#displaySelectionList(mainDictToList(), "main")