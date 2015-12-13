__author__ = 'charlesw'
from urllib.request import urlopen
from bs4 import BeautifulSoup
from bs4 import re

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")

nameList = bsObj.findAll("span", {"class":"green"})
#print(bsObj.findAll(id="text")) # this skip the name input, just checking on attr input
for name in nameList:
    print(name.get_text())


html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
for child in bsObj.find("table",{"id":"giftList"}).children:
    print(child)

print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

for i in bsObj.find("table",{"id":"giftList"}).findAll("img"):
    print (i.parent.previous_sibling.previous_sibling.previous_sibling.get_text() +' -- '+i.parent.previous_sibling.get_text())

images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
    print(image["src"])
    print (image.parent.previous_sibling.previous_sibling.previous_sibling.get_text() +' -- '+image.parent.previous_sibling.get_text())