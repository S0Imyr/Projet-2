# -- coding: utf-8 --

import csv
from pathlib import Path

DATA_FOLDER = Path('../data')


def init_category_csv(category: str) -> None:
    """
    Create a folder for the indicated category and a CSV file inside it
    with the same name as the category.

    :param category: The category name.
    :return: None
    """
    folder_path = DATA_FOLDER / category
    csv_file_path = folder_path / f'{category}.csv'
    folder_path.mkdir(parents=True, exist_ok=True)
    with open(csv_file_path, 'w', encoding="utf-8") as csvfile:
        csvfile.write("sep = ,\n")
        fieldnames = [
            'product_page_url', 'universal_product_code (upc)', 'title',
            'price_including_tax', 'price_excluding_tax', 'number_available',
            'product_description', 'category', 'review_rating',
            'image_url', 'image_name'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect='excel')
        writer.writeheader()


def write_csv(data: dict, category: str) -> None:
    """
    Write the information from a dictionary to a CSV file.
    The keys of the dictionary should match the CSV fieldnames.

    :param data: Dictionary of book's information.
    :param category: Book's category.
    :return: None
    """
    csv_file_path = DATA_FOLDER / category / f'{category}.csv'

    with open(csv_file_path, 'a', encoding="utf-8") as csvfile:
        fieldnames = [
            'product_page_url', 'universal_product_code (upc)', 'title',
            'price_including_tax', 'price_excluding_tax', 'number_available',
            'product_description', 'category', 'review_rating',
            'image_url', 'image_name'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect='excel')
        writer.writerow(data)
