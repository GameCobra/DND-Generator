import json
import os
import random

NoteList = [None] * 10

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
        dice = random.randint(1, int(i["Amount"]))
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
    for i in range(len(command) - 1):
        if command[i + 1].startswith("-"):
            command[i + 1] = NoteList[int(command[i + 1][1])]
        #    print(command[i + 1][0:])
    #print(NoteList)
    #print(command)
    return command

def displayValues(valueList: list, displayHeader: str):
    print(f"-----{displayHeader}-----")
    for i in range(len(valueList)):
        print(f"{i} - {valueList[i]}")

def Commands():
    pass


def Main():
    command = EnterCommand()
    #print(command)
    if command[0].lower() == "dt":
        if len(command) == 1:
            displayValues(SignleListConverter(Tables, "Header"), "Table Titles")
        if len(command) == 2:
            displayValues(SignleListConverter(Tables[int(command[1])]["Sub Pages"], "Sub Title"), f"Tables - {int(command[1])}")
        if len(command) == 3:
            displayValues(GenTableValues(int(command[1]), int(command[2])), f"Tables - {int(command[1])} - {command[2]}")
    if command[0].lower() == "n":
        global NoteList
        NoteList[int(command[1])] = int(command[2])
            
while True:
    Main()
