import download
import os


if __name__ == "__main__":
    home = "http://books.toscrape.com/index.html"
    if not os.path.exists('Data'):
        os.mkdir('Data')
    download.create_file_cat(home)
    download.images(home)
