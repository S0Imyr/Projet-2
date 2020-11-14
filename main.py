import Scraping
import UrlCategory


home = "http://books.toscrape.com/index.html"



print(UrlCategory.scrap_category(home))

for category in UrlCategory.scrap_category(home) :
    u = UrlCategory.browse_page(UrlCategory.scrap_category(home)[category])
    for livre in u :
        print(Scraping.extract(u[livre],category))