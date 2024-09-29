import json

tables = []

file = open('TableCompendium', 'r', encoding="utf8")
Lines = file.readlines()
Lines = Lines[:6000]
textLines : list = []
for i in range(len(Lines)):
    if Lines[i].startswith("$") == True:
        textLines.append({"Page Title": Lines[i], "Table" : []})
    if Lines[i] == "\n":
        textLines[len(textLines) - 1]["Table"].append({"Table Title" : Lines[i + 1], "Entries" : []})
        i += 1
print(textLines)



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