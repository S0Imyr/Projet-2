# -- coding: utf-8 --

import csv
from pathlib import Path

DATA_FOLDER = Path(__file__).resolve().parent.parent / 'data'
# Champs CSV centralisés
CSV_FIELDNAMES = [
    'product_page_url', 'universal_product_code (upc)', 'title',
    'price_including_tax', 'price_excluding_tax', 'number_available',
    'product_description', 'category', 'review_rating',
    'image_url', 'image_name'
]

def init_category_csv(category: str) -> None:
    """
    Create a folder for the indicated category and a CSV file inside it
    with the same name as the category.

    :param category: The category name.
    :return: None
    """
    try:
        # Crée le dossier de la catégorie
        folder_path = DATA_FOLDER / category
        folder_path.mkdir(parents=True, exist_ok=True)

        # Définit le chemin du fichier CSV
        csv_file_path = folder_path / f'{category}.csv'

        # Initialise le fichier CSV avec les en-têtes
        with csv_file_path.open('w', encoding="utf-8", newline='') as csvfile:
            csvfile.write("sep=,\n")  # Optionnel, pour indiquer le séparateur
            writer = csv.DictWriter(csvfile, fieldnames=CSV_FIELDNAMES, dialect='excel')
            writer.writeheader()

    except Exception as e:
        print(f"Error initializing CSV for category '{category}': {e}")


def write_csv(data: dict, category: str) -> None:
    """
    Write the information from a dictionary to a CSV file.
    The keys of the dictionary should match the CSV fieldnames.

    :param data: Dictionary of book's information.
    :param category: Book's category.
    :return: None
    """
    try:
        # Chemin du fichier CSV
        csv_file_path = DATA_FOLDER / category / f'{category}.csv'

        # Écrit les données dans le fichier CSV
        with csv_file_path.open('a', encoding="utf-8", newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=CSV_FIELDNAMES, dialect='excel')
            writer.writerow(data)

    except Exception as e:
        print(f"Error writing to CSV for category '{category}': {e}")
