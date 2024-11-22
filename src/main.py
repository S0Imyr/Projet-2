# -- coding: utf-8 --

from src.scraping import download
from pathlib import Path
import requests

# Constants
HOME_URL = "http://books.toscrape.com/index.html"
DATA_DIR = Path("data")


def check_connection(url: str) -> bool:
    """
    Check internet connectivity by trying to access a URL.

    :param url: The URL to check for internet connectivity.
    :return: True if there is an internet connection, False otherwise.
    :raises requests.exceptions.RequestException: if there's an issue with the request
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException:
        return False


def main():
    if not check_connection(HOME_URL):
        raise Exception("No internet connection available.")

    if not DATA_DIR.exists():
        DATA_DIR.mkdir(parents=True, exist_ok=True)

    download.scrap_and_create_csv_files(HOME_URL, data_dir=DATA_DIR)
    download.download_book_images(HOME_URL, data_dir=DATA_DIR)


if __name__ == "__main__":
    main()
