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
#print(page.status_code)

#print(page.url)

soup = BeautifulSoup(page.content, "html.parser")
'''
print(soup.text)
with open("basic.txt", "w") as f:
    f.write(page.text)
'''
# Create a list to store the data
mainData = []

# Loop through all <a> tags (which are links)
for link in soup.find_all("a"):
    url = link.get('href')  # Get the URL from the href attribute
    text = link.get_text()   # Get the text of the hyperlink
    if text != "PDF":
        mainData.append([text,url]) #{text}: 


print(len(mainData))
for i in range(17):
    mainData.pop(0)

mainData = mainData[:327]

for i in range(len(mainData)):
    startURLText = "https://redd.it/"
    if mainData[i][1].startswith(startURLText):
        urlText = requests.get(mainData[i][1], allow_redirects=True).url[:-10]
        urlText = "https://www.reddit.com/r/BehindTheTables/comments/" + urlText[len(startURLText):]
        advancedPage = requests.get(urlText, allow_redirects=True)
        pageText = advancedPage.text
        startFindText = "<shreddit-canonical-url-updater value="
        startTextIndex = pageText.find(startFindText)
        if startTextIndex == -1:
            continue
        pageText = pageText[startTextIndex + 1 + len(startFindText):]
        pageText = pageText[:pageText.find("></shreddit-canonical-url-updater>") - 1]
        urlText = pageText
        mainData[i] = [mainData[i][0], urlText]
    #print(urlText)

    #mainData[i] = [mainData[i][0], urlText]
    print(i)
    #followedURL = requests.get(url, allow_redirects=True)



# Write the results to a file
with open("URLData.txt", "w", encoding="utf-8") as f:
    for item in mainData:
        f.write(item[0] + ":" + item[1] + "\n")
