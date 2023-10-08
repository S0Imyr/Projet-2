# Web scraping

Ceci est un projet d'apprentissage du scraping avec Python.  
On souhaite éviter d'utiliser scrapy.

## Installation

Sur un terminal se placer sur un dossier cible.

Puis suivre les étapes suivantes :
1. Cloner le dépôt ici présent en tapant: `git clone https://github.com/S0Imyr/Web-scraping.git`
2. Accéder au dossier ainsi créé avec la commande : `cd Web-scraping`
3. Créer un environnement virtuel pour le projet avec `python -m venv env` sous windows ou `python3 -m venv env` sous macos ou linux.
4. Activez l'environnement virtuel avec `./env/Scripts/activate` sous windows ou `source env/bin/activate` sous MacOS ou Linux.
5. Installez les dépendances du projet avec la commande `pip install -r requirements.txt`

## Exécution

6. Exécuter le script en tapant : `python main.py`
7. Les fichiers csv se créent.
8. Le téléchargement des images se lancent après.

## Données

Dans le dossier Web-scraping, on retrouve un dossier data.
Le fichier Data contient un dossier par catégorie.  
Chaque fichier "catégorie" contient :
 - un fichier csv au nom de la catégorie</li>
 - un dossier images avec les images de tous les livres de la "catégorie".</li>

