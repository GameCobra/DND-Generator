import json

'''
save JSON format
Type:
Elements: [
    Element Type: 
    Text:
    Additional info:
    ]
Notes: [
    Title:
    Text:
    ]
'''

def FormatJSON(type, elementList : list, notesList : list):
    Elements = []
    for i in range(len(elementList)):
        Elements.append({"Element Type": elementList[i][0], "Text": elementList[i][1], "Additional Info": elementList[i][2]})
    notes = []
    for i in range(len(notesList)):
        notes.append({"Title": notesList[i][0], "Text": notesList[i][1]})
    value = {"Type": type, "Elements": Elements, "Notes": notes}
    print(value)
    return value

def SaveJSON(value):
    with open('SaveData.json') as f:
        data = json.load(f)
        print(data)
        v = list(data).append(value)
        with open('SaveData.json', "w") as h:
            json.dump(v , h)

SaveJSON(FormatJSON("Char", [["nm", "5", "notes"], ["nm", "Test", "More notes"]], [["Location", "nowhare"], ["APple", "Banana"]]))