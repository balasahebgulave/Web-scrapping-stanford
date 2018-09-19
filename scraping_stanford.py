#Importing necessary libraries
from bs4 import BeautifulSoup
import requests
import urllib
import re

#Getting html response in "response" variable
response=urllib.request.urlopen("http://cs230.stanford.edu/proj-spring-2018.html")

#Parsing html response via beautifulsoup
soup=BeautifulSoup(response,"lxml")
soup.prettify

#Declaring empty lists to store scraped data
names,posters,reports,link_reports,link_posters,save_r,save_p=[],[],[],[],[],[],[]

#Finding all links in "ul" class
a=soup.findAll("ul")
for i in a:
    b=i.findAll("li")

#Collecting project names, report urls and poster urls from links    
for i in b:
    names.append(i.find("strong").text)
    reports.append(i.find("a")["href"].lstrip("."))
    try:
        posters.append(i.findAll("a")[1]["href"].lstrip("."))
    except:
        pass
#Removing special characters from project names    
for i,j in enumerate(names):
    names[i]=re.sub(r"[^a-zA-Z0-9]","",j)

#Joining url and downloading response of each report and poster(pdf)
for i in reports:
    link_reports.append("http://cs230.stanford.edu{}".format(i))
for i in posters:
    link_posters.append("http://cs230.stanford.edu{}".format(i))    
for i in link_reports:
    save_r.append(requests.get(i))
for i in link_posters:
    save_p.append(requests.get(i))

#Writing downloaded response in file format    
for i,j in enumerate(save_r):
    with open("{}_report.pdf".format(names[i]),"wb") as fp:
        fp.write(j.content)
for i,j in enumerate(save_p):
    with open("{}_posters.pdf".format(names[i]),"wb") as fp:
        fp.write(j.content)        
    
        

    