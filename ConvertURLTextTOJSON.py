import json
file = open('URLData.txt', 'r')
Lines = file.readlines()


JSONList = []

for line in Lines:
    splitText = line.split("|")
    JSONList.append({"Name":splitText[0], "URL":splitText[1]})

with open('SiteDAtaJSON.json', 'w') as f:
    json.dump(JSONList, f)