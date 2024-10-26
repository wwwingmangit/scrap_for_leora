import os
import csv
import matplotlib
matplotlib.use('Agg')  # Set the backend to Agg (non-interactive)
import matplotlib.pyplot as plt
import numpy as np

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

def create_category_distribution_pie_chart(data, output_path):
    categories = list(data.keys())
    book_counts = [len(books) for books in data.values()]
    
    plt.figure(figsize=(12, 8))
    plt.pie(book_counts, labels=categories, autopct='%1.1f%%', startangle=90)
    plt.title('Distribution of Books by Category')
    plt.axis('equal')
    plt.savefig(output_path)
    plt.close()

def create_average_price_bar_chart(data, output_path):
    categories = list(data.keys())
    avg_prices = []
    
    for books in data.values():
        prices = [float(book['price_including_tax'][1:]) for book in books]  # Remove '£' symbol
        avg_prices.append(np.mean(prices))
    
    plt.figure(figsize=(12, 8))
    plt.bar(categories, avg_prices)
    plt.title('Average Book Price by Category')
    plt.xlabel('Category')
    plt.ylabel('Average Price (£)')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def main():
    csv_directory = 'csv'
    charts_directory = 'charts'
    
    # Ensure the charts directory exists
    os.makedirs(charts_directory, exist_ok=True)
    
    data = load_csv_files(csv_directory)
    
    pie_chart_path = os.path.join(charts_directory, 'category_distribution_pie_chart.png')
    create_category_distribution_pie_chart(data, pie_chart_path)
    print(f"Category distribution pie chart saved as '{pie_chart_path}'")
    
    bar_chart_path = os.path.join(charts_directory, 'average_price_bar_chart.png')
    create_average_price_bar_chart(data, bar_chart_path)
    print(f"Average price bar chart saved as '{bar_chart_path}'")

if __name__ == "__main__":
    main()
