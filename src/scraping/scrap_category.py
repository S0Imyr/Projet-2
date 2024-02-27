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


def page_books_url(url_page: str) -> dict:
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
            book_url = urljoin(BASE_URL, book_tag.get('href'))
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
        page_url = f"{BASE_URL}page-{i}.html"
    return books_urls


if __name__ == '__main__':

    categories_url = {
        'Academic': 'http://books.toscrape.com/catalogue/category/books/academic_40/index.html',
        'Add a comment': 'http://books.toscrape.com/catalogue/category/books/add-a-comment_18/index.html',
        'Adult Fiction': 'http://books.toscrape.com/catalogue/category/books/adult-fiction_29/index.html',
        'Art': 'http://books.toscrape.com/catalogue/category/books/art_25/index.html',
        'Autobiography': 'http://books.toscrape.com/catalogue/category/books/autobiography_27/index.html',
        'Biography': 'http://books.toscrape.com/catalogue/category/books/biography_36/index.html',
        'Business': 'http://books.toscrape.com/catalogue/category/books/business_35/index.html',
        'Childrens': 'http://books.toscrape.com/catalogue/category/books/childrens_11/index.html',
        'Christian': 'http://books.toscrape.com/catalogue/category/books/christian_43/index.html',
        'Christian Fiction': 'http://books.toscrape.com/catalogue/category/books/christian-fiction_34/index.html',
        'Classics': 'http://books.toscrape.com/catalogue/category/books/classics_6/index.html',
        'Contemporary': 'http://books.toscrape.com/catalogue/category/books/contemporary_38/index.html',
        'Crime': 'http://books.toscrape.com/catalogue/category/books/crime_51/index.html',
        'Cultural': 'http://books.toscrape.com/catalogue/category/books/cultural_49/index.html',
        'Default': 'http://books.toscrape.com/catalogue/category/books/default_15/index.html',
        'Erotica': 'http://books.toscrape.com/catalogue/category/books/erotica_50/index.html',
        'Fantasy': 'http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html',
        'Fiction': 'http://books.toscrape.com/catalogue/category/books/fiction_10/index.html',
        'Food and Drink': 'http://books.toscrape.com/catalogue/category/books/food-and-drink_33/index.html',
        'Health': 'http://books.toscrape.com/catalogue/category/books/health_47/index.html',
        'Historical': 'http://books.toscrape.com/catalogue/category/books/historical_42/index.html',
        'Historical Fiction': 'http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html',
        'History': 'http://books.toscrape.com/catalogue/category/books/history_32/index.html',
        'Horror': 'http://books.toscrape.com/catalogue/category/books/horror_31/index.html',
        'Humor': 'http://books.toscrape.com/catalogue/category/books/humor_30/index.html',
        'Music': 'http://books.toscrape.com/catalogue/category/books/music_14/index.html',
        'Mystery': 'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html',
        'New Adult': 'http://books.toscrape.com/catalogue/category/books/new-adult_20/index.html',
        'Nonfiction': 'http://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html',
        'Novels': 'http://books.toscrape.com/catalogue/category/books/novels_46/index.html',
        'Paranormal': 'http://books.toscrape.com/catalogue/category/books/paranormal_24/index.html',
        'Parenting': 'http://books.toscrape.com/catalogue/category/books/parenting_28/index.html',
        'Philosophy': 'http://books.toscrape.com/catalogue/category/books/philosophy_7/index.html',
        'Poetry': 'http://books.toscrape.com/catalogue/category/books/poetry_23/index.html',
        'Politics': 'http://books.toscrape.com/catalogue/category/books/politics_48/index.html',
        'Psychology': 'http://books.toscrape.com/catalogue/category/books/psychology_26/index.html',
        'Religion': 'http://books.toscrape.com/catalogue/category/books/religion_12/index.html',
        'Romance': 'http://books.toscrape.com/catalogue/category/books/romance_8/index.html',
        'Science': 'http://books.toscrape.com/catalogue/category/books/science_22/index.html',
        'Science Fiction': 'http://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html',
        'Self Help': 'http://books.toscrape.com/catalogue/category/books/self-help_41/index.html',
        'Sequential Art': 'http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html',
        'Short Stories': 'http://books.toscrape.com/catalogue/category/books/short-stories_45/index.html',
        'Spirituality': 'http://books.toscrape.com/catalogue/category/books/spirituality_39/index.html',
        'Sports and Games': 'http://books.toscrape.com/catalogue/category/books/sports-and-games_17/index.html',
        'Suspense': 'http://books.toscrape.com/catalogue/category/books/suspense_44/index.html',
        'Thriller': 'http://books.toscrape.com/catalogue/category/books/thriller_37/index.html',
        'Travel': 'http://books.toscrape.com/catalogue/category/books/travel_2/index.html',
        'Womens Fiction': 'http://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html',
        'Young Adult': 'http://books.toscrape.com/catalogue/category/books/young-adult_21/index.html'
    }
    home_books = {
        'A Light in the Attic': 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html',
        "It's Only the Himalayas": 'http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html',
        'Libertarianism for Beginners': 'http://books.toscrape.com/catalogue/libertarianism-for-beginners_982/index.html',
        'Mesaerion: The Best Science Fiction Stories 1800-1849': 'http://books.toscrape.com/catalogue/mesaerion-the-best-science-fiction-stories-1800-1849_983/index.html',
        'Olio': 'http://books.toscrape.com/catalogue/olio_984/index.html',
        'Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991': 'http://books.toscrape.com/catalogue/our-band-could-be-your-life-scenes-from-the-american-indie-underground-1981-1991_985/index.html',
        'Rip it Up and Start Again': 'http://books.toscrape.com/catalogue/rip-it-up-and-start-again_986/index.html',
        'Sapiens: A Brief History of Humankind': 'http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html',
        "Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)": 'http://books.toscrape.com/catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html',
        'Set Me Free': 'http://books.toscrape.com/catalogue/set-me-free_988/index.html',
        "Shakespeare's Sonnets": 'http://books.toscrape.com/catalogue/shakespeares-sonnets_989/index.html',
        'Sharp Objects': 'http://books.toscrape.com/catalogue/sharp-objects_997/index.html',
        'Soumission': 'http://books.toscrape.com/catalogue/soumission_998/index.html',
        'Starving Hearts (Triangular Trade Trilogy, #1)': 'http://books.toscrape.com/catalogue/starving-hearts-triangular-trade-trilogy-1_990/index.html',
        'The Black Maria': 'http://books.toscrape.com/catalogue/the-black-maria_991/index.html',
        'The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics': 'http://books.toscrape.com/catalogue/the-boys-in-the-boat-nine-americans-and-their-epic-quest-for-gold-at-the-1936-berlin-olympics_992/index.html',
        'The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull': 'http://books.toscrape.com/catalogue/the-coming-woman-a-novel-based-on-the-life-of-the-infamous-feminist-victoria-woodhull_993/index.html',
        'The Dirty Little Secrets of Getting Your Dream Job': 'http://books.toscrape.com/catalogue/the-dirty-little-secrets-of-getting-your-dream-job_994/index.html',
        'The Requiem Red': 'http://books.toscrape.com/catalogue/the-requiem-red_995/index.html',
        'Tipping the Velvet': 'http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html'
    }
    biography_books_url = {
        'Benjamin Franklin: An American Life': 'http://books.toscrape.com/benjamin-franklin-an-american-life_460/index.html',
        'Louisa: The Extraordinary Life of Mrs. Adams': 'http://books.toscrape.com/louisa-the-extraordinary-life-of-mrs-adams_818/index.html',
        'Setting the World on Fire: The Brief, Astonishing Life of St. Catherine of Siena': 'http://books.toscrape.com/setting-the-world-on-fire-the-brief-astonishing-life-of-st-catherine-of-siena_603/index.html',
        "The Faith of Christopher Hitchens: The Restless Soul of the World's Most Notorious Atheist": 'http://books.toscrape.com/the-faith-of-christopher-hitchens-the-restless-soul-of-the-worlds-most-notorious-atheist_495/index.html',
        'The Rise of Theodore Roosevelt (Theodore Roosevelt #1)': 'http://books.toscrape.com/the-rise-of-theodore-roosevelt-theodore-roosevelt-1_276/index.html'
    }

    assert scrap_category(BASE_URL) == categories_url
    assert page_books_url(BASE_URL) == home_books
    assert browse_pages(categories_url['Biography']) == biography_books_url
