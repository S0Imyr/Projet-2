# -- coding: utf-8 --
import requests
from bs4 import BeautifulSoup


url = "http://books.toscrape.com/index.html"

# Recherche des catégories
categories_url = {}
reponse = requests.get(url)
reponse.encoding = 'utf-8'
if reponse.ok:
    soup = BeautifulSoup(reponse.text, "html.parser")


def category_no_space(texte):
    category = texte.text.split("\n")
    category = category[2].replace(" ", "")
    return category


secteur = soup.find("ul", {"class": "nav nav-list"}).find("li").find("li").find("a")
k = 5
while k == 5:
    categories_url[category_no_space(secteur)] = "http://books.toscrape.com/"+secteur.get("href")
    secteur = secteur.find_next("a")
    k = len(secteur.text.split("\n"))

print(categories_url)
# fonction Scraper page url

# Iterer les pages
# fonction Controle s'il y a une classe next
