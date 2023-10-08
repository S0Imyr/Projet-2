# -- coding: utf-8 --

from tqdm import tqdm
from pathlib import Path
import requests

import scraping
import scrap_category
import write_csv

IMG_TITLE_MAX_LENGTH = 50


def scrap_and_create_csv_files(home_page: str, data_dir: str = 'data') -> None:
    """
    Scrap data for all categories, create a folder for each category if it doesn't exist,
    and create a CSV file inside it. Then extract and write the data to the CSV.

    :param home_page: The home page URL.
    :param data_dir: The directory where data will be stored (default is 'data').
    :return: None
    """
    print("Progression du nombre de catégories dont le csv est créé")
    for category in tqdm(scrap_category.scrap_category(home_page)):
        category_path = Path(data_dir) / category
        category_path.mkdir(parents=True, exist_ok=True)
        write_csv.init_category_csv(category)
        url_category = scrap_category.browse_page(
            scrap_category.scrap_category(home_page)[category])
        for book in url_category:
            write_csv.write_csv(scraping.extract(
                url_category[book], category), category)


def download_book_images(home_page: str, data_dir: str = 'data') -> None:
    """
    Loop through all categories, create a folder for each category if it doesn't exist, along with
    an 'Images' subfolder. Then download the image of each book in the category, naming it by
    removing prohibited characters with a maximum of 50 characters.

    :param home_page: The home page URL.
    :param data_dir: The directory where data will be stored (default is 'data').
    :return: None
    """
    print("Progression du nombre de catégories dont les images sont téléchargées")
    for category in tqdm(scrap_category.scrap_category(home_page)):
        category_path = Path(data_dir) / category / "Images"
        category_path.mkdir(parents=True, exist_ok=True)
        url_category = scrap_category.browse_page(
            scrap_category.scrap_category(home_page)[category])
        for book in url_category:
            format_title = scraping.format_title(book)
            image_url = scraping.extract(url_category[book], category)['image_url']
            image_name = format_title[:min(IMG_TITLE_MAX_LENGTH, len(str(format_title)))] + ".jpg"
            image_path = category_path / image_name
            try:
                response = requests.get(image_url)
                response.raise_for_status()
                with open(image_path, "wb") as image_file:
                    image_file.write(response.content)
            except requests.exceptions.RequestException as e:
                print(f"Error downloading image: {e}")
