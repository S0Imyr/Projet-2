import Scraping
import UrlCategory
import Write_csv
import urllib
import os
from tqdm import tqdm


def create_file_cat(home):
    """
    Boucle sur l'ensemble des catégories,
    crée un dossier de la catégorie s'il n'existe pas
    et le csv à l'intérieur
    puis sur l'ensemble des livres de la catégorie
    extrait puis écris sur le csv les données de chaque livre
    :param home: page d'accueil
    :return:
    """
    print("Nombre de catégories dont le csv est créé")
    for category in tqdm(UrlCategory.scrap_category(home)):
        if not os.path.exists('Data/'+category):
            os.mkdir('Data/'+category)
        Write_csv.init_category_csv(category)
        url_category = UrlCategory.browse_page(
            UrlCategory.scrap_category(home)[category])
        for livre in url_category:
            Write_csv.write_csv(Scraping.extract(
                url_category[livre], category), category)


def images(home):
    """
    Boucle sur l'ensemble des catégories,
    crée un dossier de la catégorie s'il n'existe pas
    et le dossier images à l'intérieur
    puis sur l'ensemble des livres de la catégorie
    télécharge dans le dossier images, l'image
    de chaque livre en la nommant en retirant les
    caractères interdits et avec 50 caractères maximum
    :param home: page d'accueil
    :return:
    """
    for category in tqdm(UrlCategory.scrap_category(home)):
        url_category = UrlCategory.browse_page(
            UrlCategory.scrap_category(home)[category])
        if not os.path.exists("Data/"+category + "/Images"):
            os.mkdir("Data/"+category + "/Images")
        for livre in url_category:
            format_title = str(livre).replace("/", "").replace(
                '\\', "").replace(":", "").replace(
                "*", "").replace("\"", "").replace(
                "<", "").replace(">", "").replace(
                "?", "").replace("|", "")
            urllib.request.urlretrieve(
                Scraping.extract(url_category[livre], category)
                ['image_url'], "Data/"+category+"/Images/" + format_title[:min(
                    50, len(str(format_title)))] + ".jpg")
