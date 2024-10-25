import json
import os


def GetRandomTables():
    parrent = os.getcwd()
    with open(os.path.join(parrent, "Tables.json"), 'r') as f:
        Tables = json.load(f)
        f.close()
    return Tables

Tables = GetRandomTables()

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
    if command[0] == "dis":
        if len(command) == 2:
            displayValues(Tables[int(command[1])]["Sub Title"])

Main()
