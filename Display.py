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

def isInputNumber(inputVal : str, reCall : bool = False, toCall = None):
    try:
        inputVal = int(inputVal)
    except:
        if reCall == True:
            f = toCall()
            return isInputNumber(f, reCall, toCall)
        else:
            return None
    else:
        return None
        

def displaySelectionList(itemeList: list, menuName: str):
    print(f"-----{menuName}-----")
    for i in range(len(itemeList)):
        print(f"{i} - {itemeList[i]}")
    return input("> ")

def mainMenu():
    displaySelectionList(["Random thing generation"])

#mainMenu()

def randomThingGenerator():
    isInputNumber(displaySelectionList(mainDictToList(), "random"))

randomThingGenerator()

#displaySelectionList(mainDictToList(), "main")