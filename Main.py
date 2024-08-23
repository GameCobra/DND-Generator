from bs4 import BeautifulSoup
import requests 
from requests_html import HTMLSession


# Everything broken
# Get the redirect of the url found on the redit page
# remove the rdt text [:-10]
# then append the url link text name (hyper link)
# use that as the redit page to look at



URL = "https://redd.it/4iq4of"

page = requests.get(URL, allow_redirects=True)
page = requests.get(page.url[:-10], allow_redirects=True)
print(page.url)

soup = BeautifulSoup(page.content, "html.parser")


data = []
for link in soup.find_all("a"):
    data.append(link.get('href'))

f = open("demofile3.txt", "w")
for item in data:
    f.write(item + "\n")
f.close()
