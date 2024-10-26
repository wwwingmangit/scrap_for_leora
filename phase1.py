import csv
import json
from scrape import scrape_book_page

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = data.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(data)

# URL of the book page
url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

# Scrape the book page
result = scrape_book_page(url)

# Print the result
if result:
    print("Scraped data:")
    print(json.dumps(result, indent=2, ensure_ascii=False))

# Save to CSV if data was successfully scraped
if result:
    save_to_csv(result, 'csv/phase1.csv')
    print("Data has been saved to book_data.csv")
else:
    print("Failed to scrape the book data.")
