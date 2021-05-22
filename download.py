import scraping
import scrap_category
import write_csv
import urllib
import os
from tqdm import tqdm


def create_file_cat(home):
    """
    Loop through all categories,
    creates a folder of the category if it doesn't exist and the csv inside
    then for all books in the category extract and write the data on the csv.
    :param home: home page
    :return: None
    """
    print("Nombre de catégories dont le csv est créé")
    for category in tqdm(scrap_category.scrap_category(home)):
        if not os.path.exists('Data/'+category):
            os.mkdir('Data/'+category)
        write_csv.init_category_csv(category)
        url_category = scrap_category.browse_page(
            scrap_category.scrap_category(home)[category])
        for livre in url_category:
            write_csv.write_csv(scraping.extract(
                url_category[livre], category), category)


def images(home):
    """
    Loop through all categories,
    creates a folder of the category if it doesn't exist and the images folder inside
    then on all the books in the category downloads in the images folder,
    the image of each book by naming it by removing the
    prohibited characters with a maximum of 50 characters
    :param home: home page
    :return: None
    """
    print("Nombre de catégories dont les images sont téléchargées")
    for category in tqdm(scrap_category.scrap_category(home)):
        url_category = scrap_category.browse_page(
            scrap_category.scrap_category(home)[category])
        if not os.path.exists("Data/"+category + "/Images"):
            os.mkdir("Data/"+category + "/Images")
        for livre in url_category:
            format_title = scraping.format_title(livre)
            urllib.request.urlretrieve(
                scraping.extract(url_category[livre], category)
                ['image_url'], "Data/"+category+"/Images/" + format_title[:min(
                    50, len(str(format_title)))] + ".jpg")
