# -- coding: utf-8 --
import requete


home = "http://books.toscrape.com/index.html"

# Recherche des catégories
categories_url = {}
soup_home = requete.requete_text(home)


def category_no_space(texte):
    category = texte.text.split("\n")
    category = category[2].replace(" ", "")
    return category


# def scrap_category(category,url):
secteur = soup_home.find("ul", {"class": "nav nav-list"}).find("li").find("li").find("a")
k = 5
while k == 5:   # S'adapte si nouvelles catégories
    categories_url[category_no_space(secteur)] = "http://books.toscrape.com/"+secteur.get("href")
    secteur = secteur.find_next("a")
    k = len(secteur.text.split("\n"))


def page_livre_url(soupe):  # fonction Scraper les livres et leurs url pour une page
    reponse = {}
    livre = soupe.find("h3")
    test = True
    while test:
        reponse[livre.find("a").get("title")] = livre.find("a").get("href")
        test = livre.find_next("h3") is not None
        livre = livre.find_next("h3")
    return reponse


def browse_page(url):   # Itérer les pages
    url_base = url[:-10]
    i = 1
    test = True
    while test:
        soup = requete.requete_text(url)
        # Scrap des liens
        test = soup.find("li", {"class": "next"}) is not None
        i += 1
        url = url_base + "page-" + str(i)+".html"
