import json
import time

URLJSON = dict()

#use https://names.ironarachne.com/  (for name generator)

with open('SiteDataJSON.json') as f:
    URLJSON = json.load(f)
    #print(URLJSON)

def mainDictToList():
    newList = []
    for i in URLJSON:
        newList.append(i["Name"])
    return newList

#* Wanted commands
#* Sel, Main, Ser

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
        print("Plese enter a propper value")
        time.sleep(1)
        randomThingGenerator()

randomThingGenerator()

#displaySelectionList(mainDictToList(), "main")