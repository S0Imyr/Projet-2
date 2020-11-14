import csv


def init_category_csv(category):
    with open('CSV/'+str(category)+'.csv', 'w', newline='', encoding="utf-8") as csvfile:
        fieldnames = ['product_page_url', 'universal_ product_code (upc)', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect='excel')
        writer.writeheader()


def write_csv(dico, category):
    with open('CSV/'+str(category)+'.csv', 'a', newline='', encoding="utf-8") as csvfile:
        fieldnames = ['product_page_url', 'universal_ product_code (upc)', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect='excel')
        writer.writerow(dico)
