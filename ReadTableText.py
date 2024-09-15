import json

file = open('RedditTables\ReditPage copy 1', 'r')
Lines = file.readlines()
textLines : list = []
for i in range(len(Lines)):
    textLines.append(Lines[i].replace("\n", ""))
    if len(textLines[len(textLines) - 1]) == 0:
        textLines.pop(len(textLines) - 1)
print(textLines)