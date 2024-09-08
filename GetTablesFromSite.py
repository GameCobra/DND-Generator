from bs4 import BeautifulSoup
import requests 
from requests_html import HTMLSession
import time

URL = "https://www.reddit.com/r/BehindTheTables/comments/4iq4of/basic_dungeons/"

page = requests.get(URL, allow_redirects=True)
#print(page.status_code)

#print(page.url)

#soup = BeautifulSoup(page.content, "html.parser")

def firstTable(inputText : str):
    text = inputText
    firstValue = inputText.find("<strong>d")
    text = text[firstValue:]
    secondValue = text.find("</ol><p>")
    text = text[:secondValue]
    return text, secondValue + firstValue

print(firstTable(page.text)[0])