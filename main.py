import Scraping
import UrlCategory
import WriteCSV

home = "http://books.toscrape.com/index.html"
print(UrlCategory.scrap_category(home))

for category in UrlCategory.scrap_category(home):
    WriteCSV.init_category_csv(category)
    url_category = UrlCategory.browse_page(UrlCategory.scrap_category(home)[category])
    for livre in url_category:
        WriteCSV.write_csv(Scraping.extract(url_category[livre], category), category)
