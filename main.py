import download
import os
import requests

# Constants
BASE_URL = "http://books.toscrape.com/index.html"
DATA_DIR = "data"


def check_internet_connection(url):
    """
    Check internet connectivity by trying to access a URL.
    :param url: The URL to check for internet connectivity.
    :return: True if there is an internet connection, False otherwise.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return True
    except requests.exceptions.ConnectionError:
        return False


def main():
    if not check_internet_connection(BASE_URL):
        raise Exception("No internet connection available.")

    if not os.path.exists(DATA_DIR):
        os.mkdir(DATA_DIR)

    download.scrap_and_create_csv_files(BASE_URL, data_dir=DATA_DIR)
    download.download_book_images(BASE_URL, data_dir=DATA_DIR)


if __name__ == "__main__":
    main()
