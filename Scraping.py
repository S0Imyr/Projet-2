# -- coding: utf-8 --
import requete


def available(table):
    reponse = ""
    for k in table[5].text:
        if k.isnumeric():
            reponse += k
    return reponse


def find_rating(soupe):
    rating = 0
    if soupe.find("div", {"class": "col-sm-6 product_main"}).findChild(
            "p", {"class": "star-rating One"}) is not None:
        rating = 1
    if soupe.find("div", {"class": "col-sm-6 product_main"}).findChild(
            "p", {"class": "star-rating Two"}) is not None:
        rating = 2
    if soupe.find("div", {"class": "col-sm-6 product_main"}).findChild(
            "p", {"class": "star-rating Three"}) is not None:
        rating = 3
    if soupe.find("div", {"class": "col-sm-6 product_main"}).findChild(
            "p", {"class": "star-rating Four"}) is not None:
        rating = 4
    if soupe.find("div", {"class": "col-sm-6 product_main"}).findChild(
            "p", {"class": "star-rating Five"}) is not None:
        rating = 5
    return rating


def extract(url, category):
    soup = requete.requete_text(url)
    if soup.find("table", {"class": "table table-striped"}
                    ).find_all("td") is None :
        tab = ["tableau non trouvé"]*7
    else:
        tab = soup.find("table", {"class": "table table-striped"}
                    ).find_all("td")

    if soup.find("div", {"class": "col-sm-6 product_main"}
                      ).find("h1").text is None :
        title = "titre non trouvé lors de l'extraction"
    else:
        title = soup.find("div", {"class": "col-sm-6 product_main"}
                      ).find("h1").text

    upc = tab[0].text
    price_tax = tab[2].text[1:]
    price = tab[3].text[1:]
    nb_available = available(tab)
    if soup.find("div", {"id": "product_description"}) is None:
        description = ""
    else:
        description = soup.find("div", {"id": "product_description"}
                                ).find_next("p").text
    rating = find_rating(soup)
    if soup.find("div", {"class": "item active"}
                 ).findChild("img").get("src")[5:] is None :
        image_url = "image non trouvée (extraction)"
    else:
        image_url = "http://books.toscrape.com" + \
                soup.find("div", {"class": "item active"}
                          ).findChild("img").get("src")[5:]
    r = {"product_page_url": url, "universal_ product_code (upc)":
         upc, "title": title, "price_including_tax": price_tax,
         "price_excluding_tax": price, "number_available": nb_available,
         "product_description": description, "category": category,
         "review_rating": rating, "image_url": image_url}
    return r
