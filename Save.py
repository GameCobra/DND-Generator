import json

'''
save JSON format
Type:
Name:
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

def FormatJSON(type, name, elementList : list, notesList : list):
    Elements = []
    for i in range(len(elementList)):
        Elements.append({"Element Type": elementList[i][0], "Text": elementList[i][1], "Additional Info": elementList[i][2]})
    notes = []
    for i in range(len(notesList)):
        notes.append({"Title": notesList[i][0], "Text": notesList[i][1]})
    value = {"Type": type, "Name": name, "Elements": Elements, "Notes": notes}
    print(value)
    return value

def SaveJSON(value):
    # Try to load existing data, if file does not exist, create an empty list
    try:
        with open('SaveData.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    # Add the new value to the list of data
    data.append(value)
    with open('SaveData.json', 'w') as h:
        json.dump(data, h, indent=4)

#SaveJSON(FormatJSON("Char", "Test", [["nm", "5", "notes"], ["nm", "Test", "More notes"]], [["Location", "nowhare"], ["APple", "Banana"]]))