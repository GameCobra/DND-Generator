import json
import time
import random
from RandomName import Name, race, ntype
from Save import SaveJSON, FormatJSON
import os

outputList = []

Tables = []

MenuSelection = 0
MenuSelection2 = 0

#use https://names.ironarachne.com/  (for name generator)

#Loads the table file so it may be accses
with open('Tables.json') as f:
    Tables = json.load(f)

# Get the first layer of the tables JSON
# This will be page titles
def GrabHeaders():
    newList = []
    for i in Tables:
        newList.append(i["Header"])
    return newList

# Takes a index for what page title it will grab the sub data for
def GrabSubSections(index : int):
    l = GrabHeaders()
    newList = []
    for i in Tables[index]["Sub Pages"]:
        newList.append(i["Sub Title"])
    return newList

# Grabs the sub data of the sub data of a page header
# Its like a tree
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


# Deals with the search command
# searchs the current layer for the desired item
def search(arg : str, layer):
    global MenuSelection
    global MenuSelection2
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
        for i in range(len(content[0])):
            if goodConent[value - 1] == content[0][i]:
                MenuSelection = i + 1
    if content[3] == "2":
        for i in range(len(content[0])):
            if goodConent[value - 1] == content[0][i]:
                MenuSelection2 = i + 1
    content[2]()

def save(arg):
    ElementsList = []
    for i in range(len(outputList[-1])):
        ElementsList.append(["Charecter", outputList[-1][i], "none"])
    SaveJSON(FormatJSON("Character", arg, ElementsList, ["none", "none", "none"]))
    pass

# A general function thats main purpose it to return if a value is a number
# if it is not a number then if will call another function, this way it will ask you the question again
# But now it is such a used function, command logic is also in it
def isInputNumber(inputVal : str, callFunction, endOfLine = False):
    try:
        inputVal = int(inputVal)
        if endOfLine == True:
            callFunction
    except:
        if inputVal == "menu":
            mainMenu()
        elif inputVal.startswith("ser"):
            search(inputVal.split(" ")[1], callFunction)
        elif inputVal.startswith("save"):
            save(inputVal.split(" ")[1])
        else:
            if endOfLine == False:
                print("Plese enter a propper value")
                time.sleep(1)
        callFunction()
        return None
    else:
        return inputVal
        

# Prints the given list and returns the user input
def displaySelectionList(itemeList: list, menuName: str):
    print(f"-----{menuName}-----")
    for i in range(len(itemeList)):
        print(f"{i + 1} - {itemeList[i]}")
    return input("> ")


def CompiledDisplay(itemList: list, menuName: str, returnFunction, endOfLine = False):
    outputList.append(itemList)
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

def SavesMenu():
    value = CompiledDisplay(["Explore saves", "new save", "Clear saves"], "Saveing menu", SavesMenu)
    if value == 1:
        pass
    if value == 3:
        open('SaveData.json', 'w').close()

def mainMenu():
    #try:
    while True:
        value = CompiledDisplay(["Random thing generater", "Random Name", "Saves", "Settings", "Help", "Credits"], "Menu", mainMenu)
        if value == 1:
            TopLayer()
        if value == 2:
            TotalNameTopicSelection()
        if value == 3:
            SavesMenu()
        if value == 5:
            print("Please check the .readme file for instructions")
            time.sleep(1)
    #except Exception as ex:
    #    print("An Error has occured, please restart the restart the program")
    #    time.sleep(1)
    #    print(ex)

mainMenu()

#displaySelectionList(mainDictToList(), "main")