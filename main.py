import Scraping
import UrlCategory


home = "http://books.toscrape.com/index.html"

print(Scraping.extract("http://books.toscrape.com/catalogue"
                       "/its-only-the-himalayas_981/index.html", "Travel"))

print(UrlCategory.scrap_category(home))

print(UrlCategory.browse_page('http://books.toscrape.com/catalogue/category/books/travel_2/index.html'))