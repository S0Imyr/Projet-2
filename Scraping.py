# -- coding: utf-8 --
import requests
from bs4 import BeautifulSoup


def extract(url, category):
    reponse = requests.get(url)
    reponse.encoding = 'utf-8'
    if reponse.ok:
        soup = BeautifulSoup(reponse.text, "html.parser")
        tab = soup.find("table", {"class": "table table-striped"}
                        ).find_all("td")
        title = soup.find("div", {"class": "col-sm-6 product_main"}
                          ).find("h1").text
        upc = tab[0].text
        price_tax = tab[2].text[1:]
        price = tab[3].text[1:]
        nb_available = ""
        for k in tab[5].text:
            if k.isnumeric():
                nb_available += k
        description = soup.find("div", {"id": "product_description"}
                                ).find_next("p").text
        rating = 0
        if soup.find("div", {"class": "col-sm-6 product_main"}).findChild(
                "p", {"class": "star-rating Ont"}) is not None:
            rating = 1
        if soup.find("div", {"class": "col-sm-6 product_main"}).findChild(
                "p", {"class": "star-rating Two"}) is not None:
            rating = 2
        if soup.find("div", {"class": "col-sm-6 product_main"}).findChild(
                "p", {"class": "star-rating Three"}) is not None:
            rating = 3
        if soup.find("div", {"class": "col-sm-6 product_main"}).findChild(
                "p", {"class": "star-rating Four"}) is not None:
            rating = 4
        if soup.find("div", {"class": "col-sm-6 product_main"}).findChild(
                "p", {"class": "star-rating Five"}) is not None:
            rating = 5
        image_url = "http://books.toscrape.com/" + \
                    soup.find("div", {"class": "item active"}
                              ).findChild("img").get("src")[5:]
    else:
        upc = title = price_tax = price = nb_available = "erreur d'extraction"
        description = rating = image_url = "erreur d'extraction"
    r = {"product_page_url": url, "universal_ product_code (upc)":
         upc, "title": title, "price_including_tax": price_tax,
         "price_excluding_tax": price, "number_available": nb_available,
         "product_description": description, "category": category,
         "review_rating": rating, "image_url": image_url}
    return r
