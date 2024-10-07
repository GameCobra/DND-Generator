import json
import time
import random
from RandomName import Name, race, ntype

Tables = []

MenuSelection = 0
MenuSelection2 = 0

#use https://names.ironarachne.com/  (for name generator)

with open('Tables.json') as f:
    Tables = json.load(f)

def GrabHeaders():
    newList = []
    for i in Tables:
        newList.append(i["Header"])
    return newList

def GrabSubSections(index : int):
    l = GrabHeaders()
    newList = []
    for i in Tables[index]["Sub Pages"]:
        newList.append(i["Sub Title"])
    return newList

def GrabSubSubSections(index : int, subIndex : int):
    l = GrabHeaders()
    newList = []
    for i in Tables[index]["Sub Pages"][subIndex]["Table"]:
        #print(i)
        dice = random.randint(0, int(i["Amount"]))
        selEntry = "No Entrie"
        for j in i["Entries"]:
            if int(j["Min"]) <= dice and int(j["Max"]) >= dice:
                selEntry = j["Text"]
                break
        newList.append(i["Table Title"] + "  " + selEntry)
    return newList


#* Wanted commands
#* Sel, Main, Ser

def search(arg : str, layer):
    print(arg)
    exit()

def isInputNumber(inputVal : str, callFunction, endOfLine = False):
    try:
        inputVal = int(inputVal)
    except:
        if inputVal == "menu":
            mainMenu()
        elif inputVal.startswith("ser "):
            search(inputVal[4:], callFunction)
        else:
            if endOfLine == False:
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




def CompiledDisplay(itemList: list, menuName: str, returnFunction, endOfLine = False):
    value = isInputNumber(displaySelectionList(itemList, menuName), returnFunction, endOfLine)
    if value <= 0:
        print("Please enter a number greater then 0")
        time.sleep(1)
        returnFunction()
    if value > len(itemList):
        print(f"Please enter a number less then {len(itemList)}")
        time.sleep(1)
        returnFunction()
    return value

def TopLayer():
    MenuSelection = CompiledDisplay(GrabHeaders(), "random", TopLayer)
    SecondLayer()
    #if result == None:
    #    print("Plese enter a propper value")
    #    time.sleep(1)
    #    randomThingGenerator()

def SecondLayer():
    MenuSelection2 = CompiledDisplay(GrabSubSections(MenuSelection - 1), "sub", SecondLayer)
    TheirdLayer()

def TheirdLayer():
    CompiledDisplay(GrabSubSubSections(MenuSelection - 1, MenuSelection2 - 1), "sub sub", SecondLayer, True)

def RaceSelection():
    return CompiledDisplay(race, "Race Selection", RaceSelection)

def TypeSelection():
    return CompiledDisplay(ntype, "Type Selection", TypeSelection)

def mainMenu():
    while True:
        value = CompiledDisplay(["Random thing generater", "Random Name", "Settings", "Help", "Credits"], "Menu", mainMenu)
        if value == 1:
            TopLayer()
        if value == 2:
            r = RaceSelection()
            t = TypeSelection()
            CompiledDisplay(Name(r, t))
        if value == 4:
            print("Please check the .readme file for instructions")
            time.sleep(1)

mainMenu()

#displaySelectionList(mainDictToList(), "main")