from bs4 import BeautifulSoup
import requests 
from requests_html import HTMLSession
import time
import json

URL = "https://www.reddit.com/r/BehindTheTables/comments/4iq4of/basic_dungeons/"

page = requests.get(URL, allow_redirects=True)
#print(page.status_code)

#print(page.url)

#soup = BeautifulSoup(page.content, "html.parser")

vals = []

def firstTable(inputText : str):
    text = inputText
    firstValue = inputText.find("<strong>d")
    text = text[firstValue:]
    secondValue = text.find("</ol>")
    if secondValue == -1:
        secondValue = text.find("</div>")
    #print(secondValue)
    text = text[:secondValue]
    return text, secondValue + firstValue

def getTables(inputText : str, depth : int):
    result = firstTable(inputText)
    if result[0] == "":
        return
    addTo(result[0])
    inputText = inputText[result[1]:]
    if depth > 0:
        getTables(inputText, depth - 1)

def addTo(value : str):
    removeVals = ["</li><li>\n", "</p>\n", "<p>\n", "<strong>", "</strong>", "<li>\n", "</p><ol>\n", "</li>"]
    changeForEnter = ["<br />"]
    for i in range(len(removeVals)):
        value = value.replace(removeVals[i], "")
    for i in range(len(changeForEnter)):
        value = value.replace(changeForEnter[i], "")
    vals[len(vals) - 1]['Table'].append(value)

def fullTable(inputText : str, inputName : str):
    vals.append({"Name": inputName, "Table" : []})
    getTables(inputText, 10)

#fullTable(page.text, "Basic")

#with open("Test.json", "w") as f:
#    json.dump(vals, f)

with open("SiteDataJSON.json", "r") as f:
    JSONList = json.load(f)

for i in range(5):
    print(i)
    page = requests.get(JSONList[i]["URL"], allow_redirects=True)
    fullTable(page.text, JSONList[i]["Name"])
    #time.sleep(1)

with open("Tables.json", "w") as f:
    json.dump(vals, f)
