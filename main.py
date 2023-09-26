import download
import os

# Constantes
BASE_URL = "http://books.toscrape.com/index.html"
DATA_DIR = "data"


def main():
    if not os.path.exists(DATA_DIR):
        os.mkdir(DATA_DIR)
    download.scrap_and_create_csv_files(BASE_URL, data_dir=DATA_DIR)
    download.download_book_images(BASE_URL, data_dir=DATA_DIR)


if __name__ == "__main__":
    main()



