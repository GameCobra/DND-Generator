import json
import pyperclip

tables = []

file = open('TableCompendium', 'r', encoding="utf8")
Lines = file.readlines()
#Lines = Lines[:6000]
textLines : list = []
for i in range(len(Lines)):
    if Lines[i].startswith("%") == True:
        textLines.append({"Header" : Lines[i][1:].replace("\n", ""), "Sub Pages" : []})
    if Lines[i].startswith("$") == True:
        textLines[-1]["Sub Pages"].append({"Sub Title": Lines[i][1:].replace("\n", ""), "Table" : []})
    if Lines[i] == "\n":
        dice = Lines[i + 1].split(" ")[0]
        #print(dice)
        #print(len(textLines[-1]["Sub Pages"]))
        textLines[-1]["Sub Pages"][-1]["Table"].append({"Table Title" : Lines[i + 1][len(dice):][:-2], "Amount" : int(dice[1:]), "Entries" : []})
        for j in range(int(dice[1:])):
            if Lines[i + j + 2].startswith("%") or Lines[i + j + 2].startswith("%") or Lines[i + j + 2] == "\n":
                break
            entry = Lines[i + j + 2].split(" ")[0]                
            textLines[-1]["Sub Pages"][-1]["Table"][-1]["Entries"].append({"Min" : entry[:-1].split("-")[0],"Max" : entry[:-1].split("-")[-1], "Text" : Lines[i + j + 2][len(entry) + 1:].replace("\n", "")})
        i += 1 + int(dice[1:])
print(textLines)
pyperclip.copy(textLines)
#print(textLines[-1])


'''
pageName = textLines[0]
textLines.pop(0)

while len(textLines) != 0:
    diceValue = 0
    print(textLines[0])
    try:
        diceValue = int(textLines[0][1:4])
    except:
        try:
            diceValue = (textLines[0][1:3])
        except:
            diceValue = int(textLines[0][1:2])

    tables.append({"Title" : pageName, "Dice Value": diceValue, "Entries" : textLines[1:diceValue + 1]})
    textLines = textLines[diceValue + 1:]
print(tables)
'''