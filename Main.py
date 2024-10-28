import json
import os
import random


def GetRandomTables():
    parrent = os.getcwd()
    with open(os.path.join(parrent, "Tables.json"), 'r') as f:
        Tables = json.load(f)
        f.close()
    return Tables

Tables = GetRandomTables()

def GenTableValues(index : int, subIndex : int):
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

def SignleListConverter(input : list, Value):
    newlist = []
    for i in range(len(input)):
        newlist.append(input[i][Value])
    return newlist

def EnterCommand():
    userInput = input(">")
    command = userInput.split(" ")
    return command

def displayValues(valueList: list, displayHeader: str):
    print(f"-----{displayHeader}-----")
    for i in range(len(valueList)):
        print(f"{i} - {valueList[i]}")

def Main():
    command = EnterCommand()
    if command[0].lower() == "dt":
        if len(command) == 1:
            displayValues(SignleListConverter(Tables, "Header"), "Tables")
        if len(command) == 2:
            displayValues(SignleListConverter(Tables[int(command[1])]["Sub Pages"], "Sub Title"), f"Tables - {int(command[1])}")
        if len(command) == 3:
            displayValues(GenTableValues(int(command[1]), int(command[2])), PutSomeThingHere)
            

Main()
