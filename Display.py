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
    content = layer(True)
    goodConent = []
    for item in content[0]:
        print(item)
        if arg.lower() in str(item).lower():
            goodConent.append(item)
    if len(goodConent) == 0:
        print("Nothing was found in our search, please change you input: " + str(arg))
        time.sleep(1)
        layer()
    value = CompiledDisplay(goodConent, "Search: " + str(arg) + " | " + content[1], layer)
    if content[3] == "1":
        MenuSelection = value
    if content[3] == "2":
        MenuSelection2 = value
    content[2]()
    #exit()

def isInputNumber(inputVal : str, callFunction, endOfLine = False):
    try:
        inputVal = int(inputVal)
        if endOfLine == True:
            callFunction
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
    value = int(isInputNumber(displaySelectionList(itemList, menuName), returnFunction, endOfLine))
    if value <= 0:
        print("Please enter a number greater then 0")
        time.sleep(1)
        returnFunction()
    if value > len(itemList):
        print(f"Please enter a number less then {len(itemList)}")
        time.sleep(1)
        returnFunction()
    return value

def TopLayer(getValues = False):
    name = "random"
    if getValues == True:
        return GrabHeaders(), name, SecondLayer, "1"
    global MenuSelection
    MenuSelection = CompiledDisplay(GrabHeaders(), name, TopLayer)
    SecondLayer()
    #if result == None:
    #    print("Plese enter a propper value")
    #    time.sleep(1)
    #    randomThingGenerator()

def SecondLayer(getValues = False):
    name = "sub"
    if getValues == True:
        return GrabSubSections(MenuSelection - 1), name, TheirdLayer, "2"
    global MenuSelection2
    MenuSelection2 = CompiledDisplay(GrabSubSections(MenuSelection - 1), name, SecondLayer)
    TheirdLayer()

def TheirdLayer(getValues = False):
    name = "sub sub"
    if getValues == True:
        return GrabSubSubSections(MenuSelection - 1, MenuSelection2 - 1), name, mainMenu, "3"
    CompiledDisplay(GrabSubSubSections(MenuSelection - 1, MenuSelection2 - 1), name, SecondLayer, True)

def TotalNameTopicSelection():
    r = CompiledDisplay(race, "Race Selection", TotalNameTopicSelection)
    t = CompiledDisplay(ntype, "Type Selection", TotalNameTopicSelection)
    CompiledDisplay(Name(r, t), "Names", TotalNameTopicSelection, endOfLine= True)

def mainMenu():
    while True:
        value = CompiledDisplay(["Random thing generater", "Random Name", "Saves" "Settings", "Help", "Credits"], "Menu", mainMenu)
        if value == 1:
            TopLayer()
        if value == 2:
            TotalNameTopicSelection()
        if value == 3:
            pass
        if value == 5:
            print("Please check the .readme file for instructions")
            time.sleep(1)

mainMenu()

#displaySelectionList(mainDictToList(), "main")