# -- coding: utf-8 --
from urllib.parse import urljoin

from typing import Dict

from src.scraping.scraping import request_text, BASE_URL

UNUSED_TAG = 1


def scrap_category(url_home: str) -> Dict[str, str]:
    """
    Search for categories on the home page and return a dictionary of category names and their URLs.

    :param url_home: URL of the home page
    :return: Dictionary of category names and their URLs
    """
    soup = request_text(url_home)
    categories_tags = soup.select("ul.nav.nav-list a")
    categories = {
        link.text.strip(): urljoin(BASE_URL, link.get("href")) for link in categories_tags[UNUSED_TAG:] if link.name
    }

    return categories


def page_books_url(url_page: str) -> Dict[str, str]:
    """
    Extract the books and their urls for a page.

    :param url_page: url of the page.
    :return: Dictionary of book titles and their URLs for the given page.
    """
    book_urls = {}
    soup = request_text(url_page)
    book_tags = soup.select("article.product_pod a")

    for book_tag in book_tags:
        if book_tag.get("title"):
            book_title = book_tag.get("title")
            href = book_tag.get("href")
            clean_href = href.lstrip("../")
            book_url = f"{BASE_URL}/catalogue/{clean_href}"
            # Ensure unique titles by appending "bis" to duplicates
            if book_title in book_urls:
                book_title += "bis"
            book_urls[book_title] = book_url
    return book_urls


def browse_pages(url_category: str) -> Dict[str, str]:
    """
    Browse the pages of a category to extract all links to books in the category.

    :param url_category: Category URL.
    :return: Dictionary of book titles and their URLs for the given category.
    """
    i = 1
    books_urls = {}
    page_url = url_category

    while True:
        soup = request_text(page_url)
        books_info = page_books_url(page_url)
        books_urls.update(books_info)
        next_page = soup.find("li", {"class": "next"})
        if next_page is None:
            break
        i += 1
        page_url = url_category.replace('index.html', f"page-{i}.html")
    return books_urls
