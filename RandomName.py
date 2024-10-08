from bs4 import BeautifulSoup
import requests 
import json

race = ["dragonborn", "dwarf", "elf", "gnome", "goblin", "halfling", "halforc", "human", "orc", "tiefling", "troll"] #halfelf
ntype = ["male", "female", "family", "given", "region", "town"]

def Name(rIndex : int, tIndex : int):

    #CompiledDisplay(race, "Race Selection", Name)

    URL = "https://names.ironarachne.com/race/" + race[rIndex - 1] + "/" + ntype[tIndex - 1] + "/10"

    page = requests.get(URL, allow_redirects=True)
    #print(page.status_code)

    #print(page.url)

    soup = BeautifulSoup(page.content, "html.parser")
    value = json.loads(str(soup))

    return value["names"]