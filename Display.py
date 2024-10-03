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


def randomThingGenerator():
    isInputNumber(displaySelectionList(mainDictToList(), "random"), randomThingGenerator)
    #if result == None:
    #    print("Plese enter a propper value")
    #    time.sleep(1)
    #    randomThingGenerator()

def CompiledDisplay(itemList: list, menuName: str, returnFunction):
    value = isInputNumber(displaySelectionList(itemList, menuName), returnFunction)
    if value <= 0:
        print("Please enter a number greater then 0")
        time.sleep(1)
        returnFunction()
    if value > len(itemList):
        print(f"Please enter a number less then {len(itemList)}")
        time.sleep(1)
        returnFunction()
    return value

def mainMenu():
    while True:
        value = isInputNumber(displaySelectionList(["Random thing generation", "Settings", "Help", "Credits"], "Menu"), mainMenu)
        if value == 1:
            randomThingGenerator()
        if value == 3:
            print("Please check the .readme file for instructions")
            time.sleep(1)

mainMenu()

#displaySelectionList(mainDictToList(), "main")