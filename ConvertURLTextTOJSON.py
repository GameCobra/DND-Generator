import json
file = open('URLData.txt', 'r')
Lines = file.readlines()

L = [{"Name":1, "URL": 2}]

for line in Lines:
    splitText = line.split("|")
    #print(name)