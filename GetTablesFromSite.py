from bs4 import BeautifulSoup
import requests 
from requests_html import HTMLSession
import time

URL = "https://www.reddit.com/r/BehindTheTables/comments/4iq4of/basic_dungeons/"

page = requests.get(URL, allow_redirects=True)
#print(page.status_code)

#print(page.url)

#soup = BeautifulSoup(page.content, "html.parser")

firstValue = page.text.find("<strong>d")
text = page.text[firstValue:]
text = text[:text.find("</ol><p>")]
print(text)