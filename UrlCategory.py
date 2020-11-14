# -- coding: utf-8 --
import requete


def category_no_space(texte):
    category = texte.text.split("\n")
    category = category[2].replace(" ", "")
    return category


def scrap_category(url_home):  # Recherche des catégories
    categories_url = {}
    soup_home = requete.requete_text(url_home)
    secteur = soup_home.find("ul", {"class": "nav nav-list"}).find("li").find("li").find("a")
    k = 5
    while k == 5:   # S'adapte si nouvelles catégories
        categories_url[category_no_space(secteur)] = "http://books.toscrape.com/"+secteur.get("href")
        secteur = secteur.find_next("a")
        k = len(secteur.text.split("\n"))
    return categories_url


def page_livre_url(soupe):  # fonction Scraper les livres et leurs url pour une page
    reponse = {}
    livre = soupe.find("h3")
    test = True
    while test:
        lien = livre.find("a").get("href")[8:]
        reponse[livre.find("a").get("title")] = "http://books.toscrape.com/catalogue" + lien
        test = livre.find_next("h3") is not None
        livre = livre.find_next("h3")
    return reponse


def browse_page(url_category):   # Itérer les pages
    url_base = url_category[:-10]
    i = 1
    test = True
    reponse = {}
    while test:
        soup = requete.requete_text(url_category)  # Scrap des liens
        d = page_livre_url(soup)
        reponse.update(d)
        test = soup.find("li", {"class": "next"}) is not None
        i += 1
        url_category = url_base + "page-" + str(i) + ".html"
    return reponse
