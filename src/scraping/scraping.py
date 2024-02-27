# -- coding: utf-8 --

import requests
from bs4 import BeautifulSoup

IMG_TITLE_MAX_LENGTH = 50

BASE_URL = "http://books.toscrape.com"
# Position in the table for UPC, price without tax, price with tax and availability
UPC_POSITION = 0
PRICE_WITHOUT_TAX_POSITION = 2
PRICE_WITH_TAX_POSITION = 3
AVAILABILITY_POSITION = 5


def format_title(title: str) -> str:
    """
    Replace prohibited characters in a title with characters allowed in filenames.

    :param title: The book title.
    :return: The formatted title.
    """
    prohibited_chars = ["/", '\\', ":", "*", "\"", "<", ">", "?", "|"]
    formatted_title = str(title)
    for char in prohibited_chars:
        formatted_title = formatted_title.replace(char, "")
    return formatted_title


def available(table: list) -> str:
    """
    Extract the availability information from a table and return the number of copies available.

    :param table: The book information table.
    :return: The number of copies available as a string.
    """
    response = ""
    for char in table[AVAILABILITY_POSITION].text:
        if char.isnumeric():
            response += char
    return response


def find_rating(soup: BeautifulSoup) -> int:
    """
    Look for the book's rating in the BeautifulSoup of a book page.

    :param soup: BeautifulSoup of a book page.
    :return: Book's rating as an integer (1 to 5).
    """
    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    product_main_div = soup.find("div", {"class": "col-sm-6 product_main"})

    for class_name, rating_value in rating_map.items():
        star_rating_element = product_main_div.findChild("p", {"class": f"star-rating {class_name}"})
        if star_rating_element is not None:
            return rating_value

    return 0  # Return 0 if no rating is found


def extract(url: str, category: str) -> dict:
    """
    Extract information about a book.

    :param url: URL of the book.
    :param category: Category of the book.
    :return: Dictionary containing book information.
    """
    soup = request_text(url)
    table = soup.find("table", {"class": "table table-striped"}).find_all("td")
    title = soup.find("div", {"class": "col-sm-6 product_main"}).find("h1").text.strip()
    upc = table[0].text
    price_tax = table[2].text[1:]
    price = table[3].text[1:]
    nb_available = available(table)
    description_element = soup.find("div", {"id": "product_description"})
    description = description_element.find_next("p").text if description_element else ""
    rating = find_rating(soup)
    image_element = soup.find("div", {"class": "item active"}).findChild("img")
    image_url = BASE_URL + image_element.get("src")[5:] if image_element else "image non trouvée (extraction)"
    formatted_title = format_title(title)
    image_name = formatted_title[:IMG_TITLE_MAX_LENGTH] + ".jpg"

    response = {
        "product_page_url": url,
        "universal_product_code (upc)": upc,
        "title": title,
        "price_including_tax": price_tax,
        "price_excluding_tax": price,
        "number_available": nb_available,
        "product_description": description,
        "category": category,
        "review_rating": rating,
        "image_url": image_url,
        "image_name": image_name
    }
    return response


def request_text(url: str) -> BeautifulSoup:
    """
    Test if a URL is accessible, then create a BeautifulSoup object with the page content.

    :param url: URL of the page
    :return: BeautifulSoup object of the page content
    :raises requests.exceptions.RequestException: if there's an issue with the request
    """
    try:
        response = requests.get(url)
        response.encoding = 'utf-8'
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        return soup
    except requests.exceptions.RequestException as e:
        print(f"The request fails for the url {url}.")
        raise requests.exceptions.RequestException from e
