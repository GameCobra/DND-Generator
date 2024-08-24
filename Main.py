from bs4 import BeautifulSoup
import requests 
from requests_html import HTMLSession


# Everything broken
# Get the redirect of the url found on the redit page
# remove the rdt text [:-10]
# then append the url link text name (hyper link)
# use that as the redit page to look at



URL = "https://www.reddit.com/r/BehindTheTables/wiki/index/"

page = requests.get(URL, allow_redirects=True)

print(page.url)

soup = BeautifulSoup(page.content, "html.parser")

# Create a list to store the data
data = []

# Loop through all <a> tags (which are links)
for link in soup.find_all("a"):
    url = link.get('href')  # Get the URL from the href attribute
    text = link.get_text()   # Get the text of the hyperlink

    if text != "PDF":
        data.append(f"{text}:{url}") #{text}: 

for i in range(17):
    data.pop(0)

data = data[:327]

'''
for i in range(len(data)):
    if data[i] == "https://redd.it/4iq4of":
        print(i)
'''

#'''
# Write the results to a file
with open("URLData.txt", "w") as f:
    for item in data:
        f.write(item + "\n")
#'''