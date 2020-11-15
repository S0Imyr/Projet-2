import Scraping
import UrlCategory
import Write_csv
import urllib

home = "http://books.toscrape.com/index.html"
print(UrlCategory.scrap_category(home))

for category in UrlCategory.scrap_category(home):
    Write_csv.init_category_csv(category)
    url_category = UrlCategory.browse_page(
        UrlCategory.scrap_category(home)[category])
    for livre in url_category:
        Write_csv.write_csv(Scraping.extract(
            url_category[livre], category), category)

for category in UrlCategory.scrap_category(home):
    url_category = UrlCategory.browse_page(
        UrlCategory.scrap_category(home)[category])
    for livre in url_category:
        format_title = str(livre).replace("/", "").replace(
            '\\', "").replace(":", "").replace(
            "*", "").replace("\"", "").replace(
            "<", "").replace(">", "").replace(
            "?", "").replace("|", "")  # caractère nom de fichiers
        urllib.request.urlretrieve(
            Scraping.extract(url_category[livre], category)
            ['image_url'], "Images/" + format_title[:min(
                50, len(str(format_title)))] + ".jpg")
