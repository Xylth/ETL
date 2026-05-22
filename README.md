
# Projet ETL 

Ce projet permet de scraper les données du site : http://books.toscrape.com/





## Pré-requis

Python 3.13.3

## Installation

Récupérer le repository via la commande :
```
git clone https://github.com/Xylth/ETL.git
```
Se rendre à la racine du repository via la commande :
```
cd ETL
```
Créer un environnement virtuel, pour l'exemple le nom sera .env, via la commande :
```
Python -m venv .env
```
Activer l'environnement virtuel via la commande :
```
.env\Scripts\activate
```
Installer les modules définis dans requirements.txt via la commande :
```
pip install -r requirements.txt
```

## Utilisation

Pour utiliser le projet, rendez-vous vous à la racine du clone du repository

Activer l'environnement virtuel, ici il est nommé .env, via la commande :
```
.env\Scripts\activate
```

Lancer l'application via la commande :
```
Python -m app
```

## Résultat
Le résultat de l'exécution se trouve dans le dossier exports à la racine du clone du repository dans le dossier "exports"

Les résultats sont séparés entre les dossiers "csv" et "img"

Dans "csv" on a un fichier par catégorie et dans "img" on a un dossier par catégorie. Chaque image de livre est nommée par son UPC.