import csv


def init_category_csv(category):
    """
    Create a folder of the indicated category and a csv file inside
    with the same name as the category
    :param category: category to add
    :return: None
    """
    with open('Data/'+category+'/'+category+'.csv',
              'w', newline='', encoding="utf-8") as csvfile:
        csvfile.write("sep = ,\n")
        fieldnames = ['product_page_url',
                      'universal_ product_code (upc)', 'title',
                      'price_including_tax', 'price_excluding_tax',
                      'number_available', 'product_description',
                      'category', 'review_rating', 'image_url', 'image_name']
        writer = csv.DictWriter(
            csvfile, fieldnames=fieldnames, dialect='excel')
        writer.writeheader()


def write_csv(dico, category):
    """
    Write the information from a dictionary on a line, 
    knowing that the titles of the csv stick with dictionary keys
    :param dico: dictionary of book's informations 
    :param category: book's category
    :return: None
    """
    with open('Data/'+category+'/'+category+'.csv', 'a',
              newline='', encoding="utf-8") as csvfile:
        fieldnames = ['product_page_url',
                      'universal_ product_code (upc)',
                      'title', 'price_including_tax',
                      'price_excluding_tax', 'number_available',
                      'product_description', 'category',
                      'review_rating', 'image_url', 'image_name']
        writer = csv.DictWriter(
            csvfile, fieldnames=fieldnames, dialect='excel')
        writer.writerow(dico)
