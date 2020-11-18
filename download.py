import Scraping
import UrlCategory
import Write_csv
import urllib
import os


def create_file_cat(home):
    for category in UrlCategory.scrap_category(home):
        if not os.path.exists('Data/'+category):
            os.mkdir('Data/'+category)
        Write_csv.init_category_csv(category)
        url_category = UrlCategory.browse_page(
            UrlCategory.scrap_category(home)[category])
        for livre in url_category:
            Write_csv.write_csv(Scraping.extract(
                url_category[livre], category), category)


def create_csv(home):
    if not os.path.exists('Data/0 Books'):
        os.mkdir('Data/0 Books')
    Write_csv.init_category_csv("0 Books")
    for category in UrlCategory.scrap_category(home):
        url_category = UrlCategory.browse_page(
            UrlCategory.scrap_category(home)[category])
        for livre in url_category:
            Write_csv.write_csv(Scraping.extract(
                url_category[livre], category), "0 Books")


def images(home):
    for category in UrlCategory.scrap_category(home):
        url_category = UrlCategory.browse_page(
            UrlCategory.scrap_category(home)[category])
        if not os.path.exists("Data/"+category + "/Images"):
            os.mkdir("Data/"+category + "/Images")
        for livre in url_category:
            format_title = str(livre).replace("/", "").replace(
                '\\', "").replace(":", "").replace(
                "*", "").replace("\"", "").replace(
                "<", "").replace(">", "").replace(
                "?", "").replace("|", "")  # caractère nom de fichiers
            urllib.request.urlretrieve(
                Scraping.extract(url_category[livre], category)
                ['image_url'], "Data/"+category+"/Images/" + format_title[:min(
                    50, len(str(format_title)))] + ".jpg")
