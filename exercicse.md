# Phase 1

Choisissez n'importe quelle page produit sur le site de OldBooks Finder. Écrivez un script Python qui visite cette page et en extrait les informations suivantes :

product_page_url
universal_product_code (upc)
title
price_including_tax
price_excluding_tax
number_available
product_description
category
review_rating
image_url

Écrivez les données dans un fichier CSV qui utilise les champs ci-dessus comme en-têtes de colonnes.

nous allons utiliser:
https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html

# Phase 2

Maintenant que vous avez obtenu les informations concernant un premier livre, vous pouvez essayer de récupérer toutes les données nécessaires pour toute une **catégorie d'ouvrages**.

Choisissez n'importe quelle catégorie sur le site de **OldBooks Finder**. Écrivez un script Python qui consulte la page de la catégorie choisie et extrait l'URL de la page produit de chaque livre appartenant à cette catégorie.

Combinez cela avec le travail que vous avez déjà effectué dans la phase 1 afin d'extraire les données produit de tous les livres de la catégorie choisie, puis écrivez les données dans un **seul fichier CSV**.

**Remarque** : certaines pages de catégorie comptent plus de 20 livres, qui sont répartis sur différentes pages (avec **pagination**). Votre application doit être capable de parcourir automatiquement les multiples pages si présentes.

Par exemple:
https://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html
qui est la meme chose que
https://books.toscrape.com/catalogue/category/books/nonfiction_13/page-1.html
https://books.toscrape.com/catalogue/category/books/nonfiction_13/page-2.html
https://books.toscrape.com/catalogue/category/books/nonfiction_13/page-3.html
https://books.toscrape.com/catalogue/category/books/nonfiction_13/page-4.html
https://books.toscrape.com/catalogue/category/books/nonfiction_13/page-5.html
https://books.toscrape.com/catalogue/category/books/nonfiction_13/page-6.html

# Phase 3

Ensuite, prolongez votre travail existant pour **télécharger et enregistrer l'image** de chaque livre que vous consultez sur le site, et l’enregistrer dans un dossier (il existe des modules python pour créer et manipuler des dossiers). Pensez à nommer l’image de manière explicite.