import UrlCategory
import download

home = "http://books.toscrape.com/index.html"
print(UrlCategory.scrap_category(home))

#download.images(home)
#download.create_csv_cat(home)
download.create_csv(home)
