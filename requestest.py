import requests
from bs4 import BeautifulSoup


def request_text(url):
    """
    Test if a url is accessible then create a soup with beautiful soup
    :param url: url page
    :return: page soup
    """
    reponse = requests.get(url)
    reponse.encoding = 'utf-8'
    if reponse.ok:
        soup = BeautifulSoup(reponse.text, "html.parser")
    else:
        soup = "page non lue par la requête"
    return soup
