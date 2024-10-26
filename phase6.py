from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os
import csv
import statistics

# Enregistrer une police qui supporte les caractères français
pdfmetrics.registerFont(TTFont('DejaVu', 'DejaVuSans.ttf'))

def load_csv_files(directory):
    data = {}
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            category = filename[:-4].replace('_', ' ')
            data[category] = []
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data[category].append(row)
    return data

def calculate_statistics(data):
    all_prices = []
    category_prices = {}
    for category, books in data.items():
        prices = [float(book['price_including_tax'][1:]) for book in books]
        all_prices.extend(prices)
        category_prices[category] = prices

    global_avg_price = statistics.mean(all_prices)
    most_represented_category = max(data, key=lambda x: len(data[x]))
    most_expensive_category = max(category_prices, key=lambda x: statistics.mean(category_prices[x]))

    return global_avg_price, most_represented_category, most_expensive_category

def create_pdf_report(data, output_path):
    doc = SimpleDocTemplate(output_path, pagesize=A4)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='French', fontName='DejaVu', fontSize=12))

    story = []

    # Titre
    story.append(Paragraph("Rapport des prix des livres d'occasion", styles['Heading1']))
    story.append(Spacer(1, 12))

    # Statistiques clés
    global_avg_price, most_represented_category, most_expensive_category = calculate_statistics(data)
    story.append(Paragraph(f"Prix moyen global : £{global_avg_price:.2f}", styles['French']))
    story.append(Paragraph(f"Catégorie la plus représentée : {most_represented_category}", styles['French']))
    story.append(Paragraph(f"Catégorie la plus chère : {most_expensive_category}", styles['French']))
    story.append(Spacer(1, 12))

    # Diagramme circulaire
    story.append(Paragraph("Répartition des livres par catégorie", styles['Heading2']))
    story.append(Paragraph("Ce diagramme montre la distribution en pourcentage des livres dans chaque catégorie.", styles['French']))
    story.append(Image('charts/category_distribution_pie_chart.png', width=6*inch, height=4*inch))
    story.append(Spacer(1, 12))

    # Graphique en barres
    story.append(Paragraph("Prix moyen des livres par catégorie", styles['Heading2']))
    story.append(Paragraph("Ce graphique illustre le prix moyen des livres pour chaque catégorie, permettant de comparer facilement les prix entre les différentes catégories.", styles['French']))
    story.append(Image('charts/average_price_bar_chart.png', width=6*inch, height=4*inch))

    doc.build(story)

def main():
    csv_directory = 'csv'
    output_pdf = 'rapport_prix_livres.pdf'

    data = load_csv_files(csv_directory)
    create_pdf_report(data, output_pdf)
    print(f"Le rapport PDF a été généré : {output_pdf}")

if __name__ == "__main__":
    main()

