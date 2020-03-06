import requests as req
import time
import os
import func
from bs4 import BeautifulSoup as bs4
holderFile = "content.txt"
address = 'https://oldschool.runescape.com/'
page = req.get(address)
sourceCode = bs4(page.content, 'html.parser')
newsSection = sourceCode.find('section', class_="content")
cleanedSection = newsSection.text

infoList = []
func.writeFile(holderFile, cleanedSection)
filledList = func.readFile(holderFile, infoList)

readMoreRemover = "Read More..."
filledList[1] = filledList[1] + "\n"
for x in filledList:
    if x[:12] == "Game Updates":
        indexTrackerTitle = filledList.index(x)-1
        filledList[indexTrackerTitle] = "Title: " + filledList[indexTrackerTitle]
        indexTrackerDescription = filledList.index(x)+1
        filledList[indexTrackerDescription] = "Description: " + filledList[indexTrackerDescription] + "\n"
        new = "Date: " + x
        filledList[filledList.index(x)] = new
    if x[:14] == "Future Updates":
        indexTrackerTitle = filledList.index(x)-1
        filledList[indexTrackerTitle] = "Title: " + filledList[indexTrackerTitle]
        indexTrackerDescription = filledList.index(x)+1
        filledList[indexTrackerDescription] = "Description: " + filledList[indexTrackerDescription] + "\n"
        new = "Date: " + x
        filledList[filledList.index(x)] = new
    if x[:9] == "Community":
        indexTrackerTitle = filledList.index(x)-1
        filledList[indexTrackerTitle] = "Title: " + filledList[indexTrackerTitle]
        indexTrackerDescription = filledList.index(x)+1
        filledList[indexTrackerDescription] = "Description: " + filledList[indexTrackerDescription] + "\n"
        new = "Date: " + x
        filledList[filledList.index(x)] = new
    if readMoreRemover in x:
        new = x.replace(readMoreRemover,"")
        filledList[filledList.index(x)] = new

for x in filledList:
    print(x)



