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

# Phase 4

Enfin, étendez votre travail en écrivant un script qui consulte le site de **OldBooks Finder**, extrait toutes les **catégories de livres disponibles**, puis extrait les informations produit de tous les livres appartenant à toutes les différentes catégories. Vous devrez écrire les données dans un fichier CSV **distinct pour chaque catégorie** de livres. Pensez à également récupérer toutes les images et les enregistrer dans des dossiers séparés, et explicitement nommés.

Je propose d'extraire la list des category a partir de la page d'accueil:
https://books.toscrape.com/index.html

# Phase 5

Maintenant que vous avez réussi à collecter les données des prix des livres de **OldBooks Finder**, il est temps d'explorer ces données pour en tirer des insights. Pour cela, vous allez créer des visualisations avec **Matplotlib** afin de comprendre comment se répartissent les prix des livres d'occasion chez ce concurrent.

Instructions supplémentaires :
1. Histogramme des prix :
Créez un diagramme circulaire montrant la répartition des livres par catégorie spécifique (Le pourcentage de livres par catégories).
2. Graphique en barres pour les catégories de livres :
Créez un graphique en barres qui montre le prix moyen des livres pour chaque catégorie de livres collectée. Cela permettra de visualiser quelles catégories de livres ont les prix les plus élevés et les plus bas.

On peut essayer de  créer des graphiques avec ReportLab, c’est également le module que nous utiliserons pour générer le PDF final en Phase 6: https://www.reportlab.com/chartgallery/pie/

# **Phase 6 : Génération du rapport PDF**

Après avoir généré des visualisations avec **Matplotlib**, vous pouvez maintenant les intégrer dans un rapport PDF contenant des informations supplémentaires pour une présentation professionnelle.

Instructions supplémentaires :
1.Création d'un PDF :Utilisez une bibliothèque telle que reportlab pour générer un fichier PDF intitulé rapport_prix_livres.pdf.
2.Inclusion des graphiques :
-Diagramme circulaire : Intégrez le diagramme circulaire montrant la répartition des livres par catégorie.
- Graphique en barres : Intégrez le graphique en barres illustrant le prix moyen des livres par catégorie.
3.Texte et informations supplémentaires :
- Ajoutez un titre pour le rapport : "Rapport des prix des livres d'occasion".
- Insérez une courte description avant chaque graphique, expliquant ce que montre la visualisation.
- Affichez également quelques statistiques clés, comme le prix moyen global des livres, la catégorie la plus représentée, et la catégorie la plus chère.
4.Présentation soignée :
- Assurez-vous que les graphiques et le texte sont bien présentés et alignés dans le PDF pour une apparence propre et professionnelle.
