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
        Elements.append({"Element Type": elementList[i][0], "Text": elementList[i][1], "Additional Info": [i][2]})
    notes = []
    for i in range(len(notesList)):
        notes.append({"Title": notesList[i][0], "Text": notesList[i][1]})
    value = {"Type": type, "Elements": Elements, "Notes": notes}