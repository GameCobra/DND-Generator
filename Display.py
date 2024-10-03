import json
import time

Tables = []

#use https://names.ironarachne.com/  (for name generator)

with open('Tables.json') as f:
    Tables = json.load(f)

def mainDictToList():
    newList = []
    for i in Tables:
        newList.append(i["Header"])
    return newList

#* Wanted commands
#* Sel, Main, Ser

def isInputNumber(inputVal : str, callFunction):
    try:
        inputVal = int(inputVal)
    except:
        print("Plese enter a propper value")
        time.sleep(1)
        callFunction()
        return None
    else:
        return inputVal
        

def displaySelectionList(itemeList: list, menuName: str):
    print(f"-----{menuName}-----")
    for i in range(len(itemeList)):
        print(f"{i + 1} - {itemeList[i]}")
    return input("> ")

def mainMenu():
    isInputNumber(displaySelectionList(["Random thing generation", "Settings", "Help", "Credits"], "Menu"), mainMenu)

mainMenu()

def randomThingGenerator():
    isInputNumber(displaySelectionList(mainDictToList(), "random"), randomThingGenerator)
    #if result == None:
    #    print("Plese enter a propper value")
    #    time.sleep(1)
    #    randomThingGenerator()

randomThingGenerator()

#displaySelectionList(mainDictToList(), "main")