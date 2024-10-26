import requests
from bs4 import BeautifulSoup
from scrape import scrape_book_page, save_to_csv, get_book_urls
from urllib.parse import urljoin
import os

def main():
    # category_url = 'https://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html'
    category_url = 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    # category_url = 'https://books.toscrape.com/catalogue/category/books/classics_6/index.html'
    
    print("Fetching book URLs...")
    book_urls = get_book_urls(category_url)
    
    print(f"Found {len(book_urls)} books. Scraping data for each book...")
    all_book_data = []
    for index, url in enumerate(book_urls, start=1):
        # Extract the book title from the URL
        book_title = url.split('/')[-2].replace('-', ' ').title()
        print(f"Fetching book {index}/{len(book_urls)}: {book_title}")
        
        book_data = scrape_book_page(url)
        if book_data:
            all_book_data.append(book_data)
        else:
            print(f"  - Failed to fetch book data")
    
    if all_book_data:
        # Extract category name from the URL
        category_name = category_url.split('/')[-2].split('_')[0]
        output_file = f'csv/phase2_{category_name}.csv'
        
        # Create the 'csv' directory if it doesn't exist
        os.makedirs('csv', exist_ok=True)
        
        save_to_csv(all_book_data, output_file)
        print(f"Scraped {len(all_book_data)} books. Data saved to {output_file}")
    else:
        print("No data was scraped.")

if __name__ == "__main__":
    main()
