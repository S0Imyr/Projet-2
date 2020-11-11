# -- coding: utf-8 --
import requests
from bs4 import BeautifulSoup
import time

"""
links=[]

for i in range(26):
    url = "http://example.webscraping.com/places/default/index/"+str(i)
    reponse = requests.get(url)
    if reponse.ok :
        soup = BeautifulSoup(reponse.text,"html.parser")
        tds = soup.findAll("td")
        for td in tds :
            a = td.find("a")
            link = a["href"]
            links.append("http://example.webscraping.com/"+link)
        time.sleep(3)
print(links)
print(len(links))


with open("urls.txt", "w") as file :
    for link in links:
        file.write(link + "\n")



with open("urls.txt", "r") as file:
    for row in file:
        print(row)
"""
url="http://example.webscraping.com//places/default/view/Zimbabwe-252"

reponse = requests.get(url)

if reponse.ok:
    soup = BeautifulSoup(reponse.text)
    country = soup.find("tr",{"id":"places_country__row"}).find("td",{"class":"w2p_fw"})