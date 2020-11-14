import Scraping
import UrlCategory

home = "http://books.toscrape.com/index.html"



print(Scraping.extract("http://books.toscrape.com/catalogue"
              "/its-only-the-himalayas_981/index.html", "Travel"))

print(UrlCategory.scrap_category(home))
