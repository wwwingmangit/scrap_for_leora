import requests
from bs4 import BeautifulSoup
from scrape import scrape_book_page
import csv
from urllib.parse import urljoin

def get_book_urls(category_url):
    book_urls = []
    while category_url:
        print(f"Fetching page: {category_url}")
        response = requests.get(category_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract book URLs from the current page
        for book in soup.select('article.product_pod h3 a'):
            book_url = urljoin(category_url, book['href'])
            book_urls.append(book_url)
        
        # Check for next page
        next_button = soup.select_one('li.next a')
        if next_button:
            category_url = urljoin(category_url, next_button['href'])
        else:
            category_url = None
    
    print(f"Total books found: {len(book_urls)}")
    return book_urls

def save_to_csv(data, filename):
    if data:
        keys = data[0].keys()
        with open(filename, 'w', newline='', encoding='utf-8') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)

def main():
    category_url = 'https://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html'
    
    print("Fetching book URLs...")
    book_urls = get_book_urls(category_url)
    
    print(f"Found {len(book_urls)} books. Scraping data for each book...")
    all_book_data = []
    for url in book_urls:
        book_data = scrape_book_page(url)
        if book_data:
            all_book_data.append(book_data)
    
    if all_book_data:
        # Extract category name from the URL
        category_name = category_url.split('/')[-2].split('_')[0]
        output_file = f'csv/phase2_{category_name}.csv'
        save_to_csv(all_book_data, output_file)
        print(f"Scraped {len(all_book_data)} books. Data saved to {output_file}")
    else:
        print("No data was scraped.")

if __name__ == "__main__":
    main()