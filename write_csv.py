import csv


def init_category_csv(category):
    """
    Crée un dossier de la catégorie indiqué,
    et un fichier csv à l'intérieur
    avec le même nom que la catégorie
    :param category: catégorie à créer
    :return: vide
    """
    with open('Data/'+category+'/'+category+'.csv',
              'w', newline='', encoding="utf-8") as csvfile:
        csvfile.write("sep = ,\n")
        fieldnames = ['product_page_url',
                      'universal_ product_code (upc)', 'title',
                      'price_including_tax', 'price_excluding_tax',
                      'number_available', 'product_description',
                      'category', 'review_rating', 'image_url']
        writer = csv.DictWriter(
            csvfile, fieldnames=fieldnames, dialect='excel')
        writer.writeheader()


def write_csv(dico, category):
    """
    Ecris les informations d'un dictionnaire sur une
    ligne, sachant que les titres du csv colle avec
    les clés du dictionnaire
    :param dico: dictionnaire de données d'un livre
    :param category: catégorie du livre
    :return: vide
    """
    with open('Data/'+category+'/'+category+'.csv', 'a',
              newline='', encoding="utf-8") as csvfile:
        fieldnames = ['product_page_url',
                      'universal_ product_code (upc)',
                      'title', 'price_including_tax',
                      'price_excluding_tax', 'number_available',
                      'product_description', 'category',
                      'review_rating', 'image_url']
        writer = csv.DictWriter(
            csvfile, fieldnames=fieldnames, dialect='excel')
        writer.writerow(dico)
