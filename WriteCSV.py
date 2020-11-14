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



init_category_csv('Crime')
write_csv({'product_page_url': 'http://books.toscrape.com/catalogue/the-long-shadow-of-small-ghosts-murder-and-memory-in-an-american-city_848/index.html', 'universal_ product_code (upc)': 'abeafe151a587d3b', 'title': 'The Long Shadow of Small Ghosts: Murder and Memory in an American City', 'price_including_tax': '10.97', 'price_excluding_tax': '10.97', 'number_available': '15', 'product_description': 'In Cold Blood meets Adrian Nicole LeBlanc’s Random Family: A harrowing, profoundly personal investigation of the causes, effects, and communal toll of a deeply troubling crime—the brutal murder of three young children by their parents in the border city of Brownsville, Texas.On March 11, 2003, in Brownsville, Texas—one of America’s poorest cities—John Allen Rubio and Angel In Cold Blood meets Adrian Nicole LeBlanc’s Random Family: A harrowing, profoundly personal investigation of the causes, effects, and communal toll of a deeply troubling crime—the brutal murder of three young children by their parents in the border city of Brownsville, Texas.On March 11, 2003, in Brownsville, Texas—one of America’s poorest cities—John Allen Rubio and Angela Camacho murdered their three young children. The apartment building in which the brutal crimes took place was already rundown, and in their aftermath a consensus developed in the community that it should be destroyed. It was a place, neighbors felt, that was plagued by spiritual cancer. In 2008, journalist Laura Tillman covered the story for The Brownsville Herald. The questions it raised haunted her, particularly one asked by the sole member of the city’s Heritage Council to oppose demolition: is there any such thing as an evil building? Her investigation took her far beyond that question, revealing the nature of the toll that the crime exacted on a city already wracked with poverty. It sprawled into a six-year inquiry into the larger significance of such acts, ones so difficult to imagine or explain that their perpetrators are often dismissed as monsters alien to humanity. With meticulous attention and stunning compassion, Tillman surveyed those surrounding the crimes, speaking with the lawyers who tried the case, the family’s neighbors and relatives and teachers, even one of the murderers: John Allen Rubio himself, whom she corresponded with for years and ultimately met in person. The result is a brilliant exploration of some of our age’s most important social issues, from poverty to mental illness to the death penalty, and a beautiful, profound meditation on the truly human forces that drive them. It is disturbing, insightful, and mesmerizing in equal measure. ...more', 'category': 'Crime', 'review_rating': 1, 'image_url': 'http://books.toscrape.com//media/cache/2b/50/2b50fa031b2411a94bc68de0bbdd96fb.jpg'}, 'Crime')
