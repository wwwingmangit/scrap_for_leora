# scrap_for_leora

Ce projet est un exercice de web scraping pour extraire des informations sur les livres du site [Books to Scrape](https://books.toscrape.com/).

## Résumé des phases

### Phase 1
- Objectif : Extraire les informations d'un seul livre.
- Fonctionnalités :
  - Récupération du titre, du prix, de la note, et de l'URL de l'image.
  - Affichage des informations extraites.

### Phase 2
- Objectif : Extraire les informations de tous les livres d'une catégorie.
- Fonctionnalités :
  - Récupération des URLs de tous les livres d'une catégorie.
  - Extraction des informations pour chaque livre.
  - Sauvegarde des données dans un fichier CSV.

### Phase 3
- Objectif : Télécharger les images des livres d'une catégorie.
- Fonctionnalités :
  - Extraction des URLs des images pour chaque livre.
  - Téléchargement et sauvegarde des images dans un dossier spécifique.

### Phase 4
- Objectif : Extraire les informations et les images de tous les livres de toutes les catégories.
- Fonctionnalités :
  - Récupération de toutes les catégories du site.
  - Extraction des informations et téléchargement des images pour chaque livre de chaque catégorie.
  - Sauvegarde des données dans des fichiers CSV séparés pour chaque catégorie.
  - Gestion améliorée des erreurs et des noms de fichiers contenant des caractères spéciaux.

## Utilisation

Pour exécuter le script final (phase4), utilisez la commande suivante :
