# -- coding: utf-8 --
import requete


def scrap_category(url_home):
    """
    Recherche des catégories sur la page d'accueil
    s'adapte si nouvelles catégories sont ajoutées
    :param url_home: page d'accueil
    :return: le dictionnaire qui à la catégorie associe son url
    """
    categories_url = {}
    soup_home = requete.request_text(url_home)
    secteur = soup_home.find(
        "ul", {"class": "nav nav-list"}).find("li").find("li").find("a")
    k = 5
    while k == 5:
        categories_url[secteur.text.strip()] = \
            "http://books.toscrape.com/"+secteur.get("href")
        secteur = secteur.find_next("a")
        k = len(secteur.text.split("\n"))
    return categories_url


def page_livre_url(soupe):
    """
    Extrait les livres et leurs url pour une page
    :param soupe (beautifulsoup) de la page
    :return: un dictionnaire qui à un titre associe son url
    pour les livres de la page
    """
    reponse = {}
    livre = soupe.find("h3")
    test = True
    while test:
        lien = livre.find("a").get("href")[8:]
        if livre.find("a").get("title") in reponse:
            titre = livre.find("a").get("title") + "bis"
        else:
            titre = livre.find("a").get("title")
        reponse[titre] = "http://books.toscrape.com/catalogue" + lien
        test = livre.find_next("h3") is not None
        livre = livre.find_next("h3")
    return reponse


def browse_page(url_category):
    """
    Parcourt les pages d'une catégorie
    pour extraire tous les liens
    des livres de la catégorie
    :param url_category: l'url de la catégorie
    :return: un dictionnaire qui à un titre associe son url
    pour tous les livres de la catégorie
    """
    url_base = url_category[:-10]
    i = 1
    test = True
    reponse = {}
    while test:
        soup = requete.request_text(url_category)
        d = page_livre_url(soup)
        reponse.update(d)
        test = soup.find("li", {"class": "next"}) is not None
        i += 1
        url_category = url_base + "page-" + str(i) + ".html"
    return reponse
