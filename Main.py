from bs4 import BeautifulSoup
import requests 


URL = "https://www.reddit.com/r/BehindTheTables/wiki/index/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

f = open("demofile3.txt", "w")
f.write(page.text)
f.close()