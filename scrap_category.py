# -- coding: utf-8 --

from scraping import request_text, BASE_URL
from bs4 import BeautifulSoup
from typing import Dict


def scrap_category(url_home: str) -> dict:
    """
    Search for categories on the home page and return a dictionary of category names and their URLs.

    :param url_home: URL of the home page
    :return: Dictionary of category names and their URLs
    """
    categories_url = {}
    soup_home = request_text(url_home)
    category = soup_home.find("ul", {"class": "nav nav-list"}).find("li").find("li").find("a")
    k = 5
    while k == 5:
        categories_url[category.text.strip()] = \
            "http://books.toscrape.com/"+category.get("href")
        category = category.find_next("a")
        k = len(category.text.split("\n"))
    return categories_url


def page_books_url(soup: BeautifulSoup) -> dict:
    """
    Extract the books and their urls for a page.

    :param soup: BeautifulSoup object representing the page.
    :return: Dictionary of book titles and their URLs for the given page.
    """
    books_info = {}
    book_heading = soup.find("h3")

    while book_heading:
        book_link = book_heading.find("a")
        book_title = book_link.get("title")
        book_url = f"{BASE_URL}/catalogue{book_link.get('href')[8:]}"

        # Ensure unique titles by appending "bis" to duplicates
        if book_title in books_info:
            book_title += "bis"

        books_info[book_title] = book_url
        book_heading = book_heading.find_next("h3")

    return books_info


def browse_page(url_category: str) -> Dict[str, str]:
    """
    Browse the pages of a category to extract all links to books in the category.

    :param url_category: Category URL.
    :return: Dictionary of book titles and their URLs for the given category.
    """
    url_base = url_category[:-10]
    i = 1
    books_urls = {}

    while True:
        soup = request_text(url_category)
        books_info = page_books_url(soup)
        books_urls.update(books_info)

        next_page = soup.find("li", {"class": "next"})
        if next_page is None:
            break

        i += 1
        url_category = f"{url_base}page-{i}.html"

    return books_urls
