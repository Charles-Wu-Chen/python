__author__ = 'charlesw'

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import datetime

random.seed(datetime.datetime.now())

global pages
pages = []

def getLinks(articleUrl):

    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html,"html.parser")
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id ="mw-content-text").findAll("p")[0])
#        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("This page is missing something! No worries though!")
    for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")) :
        if link.attrs['href'] not in pages:
            newPage = link.attrs['href']
            print ("----------------\n"+newPage)
            pages.append(newPage)
            getLinks(newPage)

getLinks("")

#links = getLinks("/wiki/Kevin_Bacon")
#while len(links)>1 :
#    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
#    print (newArticle)
#    links = getLinks(newArticle)

