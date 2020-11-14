# -- coding: utf-8 --
import requete


home = "http://books.toscrape.com/index.html"

# Recherche des catégories
categories_url = {}

soup = requete.requete_text(home)


def category_no_space(texte):
    category = texte.text.split("\n")
    category = category[2].replace(" ", "")
    return category


secteur = soup.find("ul", {"class": "nav nav-list"}).find("li").find("li").find("a")
k = 5
while k == 5:   # S'adapte si nouvelles catégories
    categories_url[category_no_space(secteur)] = "http://books.toscrape.com/"+secteur.get("href")
    secteur = secteur.find_next("a")
    k = len(secteur.text.split("\n"))

print(categories_url)
# fonction Scraper page url
# def scrap_category(category,url):


# Itérer les pages
category = 'Travel'
url = 'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
url_base = url[:-10]
i = 1
test = True
while test:
    test = soup.find("li", {"class": "next"}) is not None
    i += 1
    url = url_base + "page-" + str(i)+".html"
    print(url)   # Test
# fonction Controle s'il y a une class next
