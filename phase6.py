import os
import csv
from collections import defaultdict
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.lib import colors
from reportlab.graphics import renderPDF
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.graphics.shapes import String

def read_csv_files(csv_directory):
    all_data = []
    for filename in os.listdir(csv_directory):
        if filename.endswith('.csv'):
            category = filename.replace('.csv', '').replace('_', ' ')
            filepath = os.path.join(csv_directory, filename)
            with open(filepath, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    row['category'] = category
                    all_data.append(row)
    return all_data

def create_category_distribution_pie_chart(data):
    category_counts = defaultdict(int)
    for book in data:
        category_counts[book['category']] += 1
    
    total_books = sum(category_counts.values())
    
    # Sort categories by count and take top 10
    top_categories = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    
    drawing = Drawing(500, 300)
    pie = Pie()
    pie.x = 150
    pie.y = 0
    pie.width = 200
    pie.height = 200
    pie.data = [count for _, count in top_categories]
    pie.labels = [f"{category[:15]}..." if len(category) > 15 else category for category, _ in top_categories]
    pie.slices.strokeWidth = 0.5
    
    # Use a color scheme
    color_scheme = [colors.red, colors.orange, colors.yellow, colors.green, colors.blue,
                    colors.indigo, colors.violet, colors.pink, colors.cyan, colors.magenta]
    for i, color in enumerate(color_scheme):
        pie.slices[i].fillColor = color
    
    # Add a legend
    from reportlab.graphics.charts.legends import Legend
    legend = Legend()
    legend.x = 370
    legend.y = 50
    legend.deltay = 15
    legend.fontSize = 8
    legend.alignment = 'right'
    legend.columnMaximum = 10
    legend.colorNamePairs = [(color_scheme[i], f"{category[:15]}... ({count/total_books:.1%})") 
                             for i, (category, count) in enumerate(top_categories)]
    drawing.add(legend)
    
    drawing.add(pie)
    return drawing

def create_average_price_bar_chart(data):
    category_prices = defaultdict(list)
    for book in data:
        category_prices[book['category']].append(float(book['price_including_tax'].replace('£', '')))
    
    avg_prices = {category: sum(prices) / len(prices) for category, prices in category_prices.items()}
    
    # Sort categories by average price and take top 10
    top_categories = sorted(avg_prices.items(), key=lambda x: x[1], reverse=True)[:10]
    
    drawing = Drawing(500, 300)
    bc = VerticalBarChart()
    bc.x = 50
    bc.y = 50
    bc.height = 200
    bc.width = 400
    bc.data = [[price for _, price in top_categories]]
    bc.categoryAxis.categoryNames = [category[:15] + '...' if len(category) > 15 else category for category, _ in top_categories]
    bc.valueAxis.valueMin = 0
    bc.valueAxis.valueMax = max(price for _, price in top_categories) * 1.1
    bc.bars[0].fillColor = colors.blue
    
    # Customize the chart
    bc.categoryAxis.labels.boxAnchor = 'ne'
    bc.categoryAxis.labels.dx = -8
    bc.categoryAxis.labels.dy = -2
    bc.categoryAxis.labels.angle = 30
    bc.categoryAxis.labels.fontSize = 8
    
    bc.valueAxis.labelTextFormat = '£%.2f'
    bc.valueAxis.labels.fontSize = 8
    
    # Add value labels on top of bars
    for i, (category, price) in enumerate(top_categories):
        label = String(bc.x + (i + 0.5) * bc.width / len(top_categories), bc.y + bc.height * price / bc.valueAxis.valueMax + 5,
                       '£%.2f' % price)
        label.fontSize = 8
        label.textAnchor = 'middle'
        drawing.add(label)
    
    drawing.add(bc)
    return drawing

def generate_charts(csv_directory, output_directory):
    data = read_csv_files(csv_directory)
    
    os.makedirs(output_directory, exist_ok=True)
    
    # Create a PDF document
    pdf_path = os.path.join(output_directory, 'book_analysis_charts.pdf')
    doc = SimpleDocTemplate(pdf_path, pagesize=A4)
    
    # Create a list to hold the elements
    elements = []
    
    # Add a title
    styles = getSampleStyleSheet()
    elements.append(Paragraph("Book Analysis Charts", styles['Title']))
    elements.append(Spacer(1, 12))
    
    # Create and add the pie chart
    elements.append(Paragraph("Category Distribution", styles['Heading2']))
    elements.append(Spacer(1, 6))
    pie_chart = create_category_distribution_pie_chart(data)
    elements.append(pie_chart)
    elements.append(Spacer(1, 12))
    
    # Create and add the bar chart
    elements.append(Paragraph("Average Price by Category", styles['Heading2']))
    elements.append(Spacer(1, 6))
    bar_chart = create_average_price_bar_chart(data)
    elements.append(bar_chart)
    
    # Build the PDF
    doc.build(elements)
    print(f"Charts saved as '{pdf_path}'")

def main():
    csv_directory = 'csv'
    output_directory = 'charts'
    
    if not os.path.exists(csv_directory):
        print(f"Error: CSV directory '{csv_directory}' not found.")
        return
    
    print("Generating charts based on CSV files...")
    generate_charts(csv_directory, output_directory)
    print("Charts generation completed.")

if __name__ == "__main__":
    main()
