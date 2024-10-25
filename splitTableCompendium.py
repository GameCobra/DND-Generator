import json

tables = []

#Opens the text file
file = open('TableCompendium', 'r', encoding="utf8")
Lines = file.readlines()

textLines : list = []

#Headers = 0
#SubHeading = 0

#Gose though every line in the text file
for i in range(len(Lines)):

    #If the line is a header
    if Lines[i].startswith("%") == True:
        #Headers += 1
        #SubHeading = 0
        textLines.append({"Header" : Lines[i][1:].replace("\n", ""), "Sub Pages" : []})
    
    #If the line is a sub heading
    if Lines[i].startswith("$") == True:
        #SubHeading += 1
        textLines[-1]["Sub Pages"].append({"Sub Title": Lines[i][1:].replace("\n", ""), "Table" : []})
    
    #If the line is the start of a table
    if Lines[i] == "\n":
        
        #Determins what number has to be rolled to propperly use the table
        dice = Lines[i + 1].split(" ")[0]

        #Adds the table to the JSON of tables
        textLines[-1]["Sub Pages"][-1]["Table"].append({"Table Title" : Lines[i + 1][len(dice):][:-2], "Amount" : int(dice[1:]), "Entries" : []})
        
        #Adds the elements to the table list
        for j in range(int(dice[1:])):
            if Lines[i + j + 2].startswith("%") or Lines[i + j + 2].startswith("%") or Lines[i + j + 2] == "\n":
                break
            entry = Lines[i + j + 2].split(" ")[0]                
            textLines[-1]["Sub Pages"][-1]["Table"][-1]["Entries"].append({"Min" : entry[:-1].split("-")[0],"Max" : entry[:-1].split("-")[-1], "Text" : Lines[i + j + 2][len(entry) + 1:].replace("\n", "")})
        
        #Skipes the able elements for the main loop
        i += 1 + int(dice[1:])

#Saves the list to the JSON
with open('Tables.json', 'w') as f:
    json.dump(textLines, f, indent=4)


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