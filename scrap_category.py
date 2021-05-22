# -- coding: utf-8 --
import requestest


def scrap_category(url_home):
    """
    Search for categories on the home page
    adapts if new categories are added
    :param url_home: home page
    :return: the dictionary of categories and their url
    """
    categories_url = {}
    soup_home = requestest.request_text(url_home)
    secteur = soup_home.find(
        "ul", {"class": "nav nav-list"}).find("li").find("li").find("a")
    k = 5
    while k == 5:
        categories_url[secteur.text.strip()] = \
            "http://books.toscrape.com/"+secteur.get("href")
        secteur = secteur.find_next("a")
        k = len(secteur.text.split("\n"))
    return categories_url


def page_books_url(soup):
    """
    Extract the books and their urls for a page
    :param soup: page soup
    :return: dictionary of title of books and their url for the given page (soup)
    """
    reponse = {}
    livre = soup.find("h3")
    test = True
    while test:
        lien = livre.find("a").get("href")[8:]
        if livre.find("a").get("title") in reponse:
            title = livre.find("a").get("title") + "bis"
        else:
            title = livre.find("a").get("title")
        reponse[title] = "http://books.toscrape.com/catalogue" + lien
        test = livre.find_next("h3") is not None
        livre = livre.find_next("h3")
    return reponse


def browse_page(url_category):
    """
    Browse the pages of a category to extract all links books in the category
    :param url_category: category url
    :return: dictionary of title of books and their url for the given category
    """
    url_base = url_category[:-10]
    i = 1
    test = True
    reponse = {}
    while test:
        soup = requestest.request_text(url_category)
        d = page_books_url(soup)
        reponse.update(d)
        test = soup.find("li", {"class": "next"}) is not None
        i += 1
        url_category = url_base + "page-" + str(i) + ".html"
    return reponse
