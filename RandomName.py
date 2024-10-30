from bs4 import BeautifulSoup
import requests 
import json

#Lists of what items can be pulled from "Iron Arachne"
race = ["dragonborn", "dwarf", "elf", "gnome", "goblin", "halfling", "halforc", "human", "orc", "tiefling", "troll"] #halfelf
ntype = ["male", "female", "family", "given", "region", "town"]

#Called by the display function
# rIndex is the race list index
# tIndex is the type index
def NameGen(rIndex : int, tIndex : int):
    #Compiles the url to make the request to based on the given inputs
    URL = "https://names.ironarachne.com/race/" + race[rIndex] + "/" + ntype[tIndex] + "/10"
    
    page = requests.get(URL, allow_redirects=True)
    
    #Parse and return the name portion of the site
    soup = BeautifulSoup(page.content, "html.parser")
    print(str(soup))
    value = json.loads(str(soup))

    return value["names"]