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
    print(secondValue)
    text = text[:secondValue]
    return text, secondValue + firstValue

def getTables(inputText : str, depth : int):
    result = firstTable(inputText)
    if result[0] == "":
        return
    vals[len(vals) - 1]['Table'].append(result[0])
    inputText = inputText[result[1]:]
    if depth > 0:
        getTables(inputText, depth - 1)

def fullTable(inputText : str, inputName : str):
    vals.append({"Name": inputName, "Table" : []})
    getTables(inputText, 10)

fullTable(page.text, "Basic")

with open("Test.json", "w") as f:
    json.dump(vals, f)