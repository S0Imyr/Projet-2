import UrlCategory
import download
import os


home = "http://books.toscrape.com/index.html"
print(UrlCategory.scrap_category(home))

if not os.path.exists('Data'):
    os.mkdir('Data')

#download.images(home)
download.create_file_cat(home)
#download.create_csv(home)
