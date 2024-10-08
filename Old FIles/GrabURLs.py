from bs4 import BeautifulSoup
import requests 
from requests_html import HTMLSession
import time

# Everything broken
# Get the redirect of the url found on the redit page
# remove the rdt text [:-10]
# then append the url link text name (hyper link)
# use that as the redit page to look at


def getRedirect(URLText: str):
    startText = "<shreddit-redirect href="
    pageText = URLText[URLText.find(startText) + 1 + len(startText):]
    index = pageText.find("></shreddit-redirect>")
    pageText = pageText[:index - 1]
    prefix = "https://www.reddit.com"
    pageText = prefix + pageText
    return pageText, index

def deapRedirect(URL: str):
    page = requests.get(URL, allow_redirects=True)
    if page.status_code == 429:
        print("error 429")
        exit()
    text, index = getRedirect(page.text)
    if index == -1:
        return URL
    else:
        return deapRedirect(text)


URL = "https://www.reddit.com/r/BehindTheTables/wiki/index/"

page = requests.get(URL, allow_redirects=True)
print(page.status_code)

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


#print(len(mainData))
for i in range(17):
    mainData.pop(0)

mainData = mainData[:327] #327
'''
for i in range(50): #len(mainData)
    print(mainData[i][1])
    #time.sleep(1)
    removeURL = "https://redd.it/"
    urlData = requests.get(removeURL + mainData[i][1][len(removeURL):], allow_redirects=True)
    urlText = urlData.url[:-10]
    print(urlText)
    startURLText = "https://www.reddit.com/comments/"
    if urlText.startswith(startURLText):
        urlText = "https://www.reddit.com/r/BehindTheTables/comments/" + urlText[len(startURLText):]
        print(urlText)
        advancedPage = requests.get(urlText, allow_redirects=True)
        pageText = advancedPage.text
        pageText = getRedirect(pageText)[0]
        print(pageText)
        startBitToAdd = "https://www.reddit.com"
        urlText = startBitToAdd + pageText

    #print(urlText)
    if urlData.status_code == 429:
        print("error")
        #i -= 1
        time.sleep(45)
        #continue
    mainData[i] = [mainData[i][0], urlText]
    print(i)
    #followedURL = requests.get(url, allow_redirects=True)


'''
for j in range(32):
    for i in range(10): #len(mainData)
        wantToRemovePrefix = "https://redd.it/"
        appendPrefix = "https://www.reddit.com/comments/"
        if mainData[i + j * 10][1].startswith(wantToRemovePrefix):
            modifiedURL = appendPrefix + mainData[i + j * 10][1][len(wantToRemovePrefix):]
            mainData[i + j * 10][1] = deapRedirect(modifiedURL)
        print(f"{j} | {i}")
    time.sleep(45)

# Write the results to a file
with open("URLData.txt", "w", encoding="utf-8") as f:
    for item in mainData:
        f.write(item[0] + ":" + item[1] + "\n")
