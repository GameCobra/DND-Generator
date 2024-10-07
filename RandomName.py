from bs4 import BeautifulSoup
import requests 

URL = "https://names.ironarachne.com/"

page = requests.get(URL, allow_redirects=True)
#print(page.status_code)

#print(page.url)

soup = BeautifulSoup(page.content, "html.parser")

print(soup)