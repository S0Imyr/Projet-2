import requests
from bs4 import BeautifulSoup


def requete_text(url):
    reponse = requests.get(url)
    reponse.encoding = 'utf-8'
    if reponse.ok:
        soup = BeautifulSoup(reponse.text, "html.parser")
    else:
        soup = "page non lue par la requête"
    return soup
