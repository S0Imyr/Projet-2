import requests
from bs4 import BeautifulSoup


def request_text(url):
    """
    Teste si un url est accessible puis créé une soupe avec beautiful soup
    :param url: l'url de la page
    :return: soupe de la page
    """
    reponse = requests.get(url)
    reponse.encoding = 'utf-8'
    if reponse.ok:
        soup = BeautifulSoup(reponse.text, "html.parser")
    else:
        soup = "page non lue par la requête"
    return soup
