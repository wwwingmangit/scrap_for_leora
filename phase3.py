import requests
from bs4 import BeautifulSoup
from scrape import scrape_book_page, get_book_urls
from urllib.parse import urljoin
import os

def download_image(url, destination_folder, filename):
    """Download and save an image from a given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # Create the destination folder if it doesn't exist
        os.makedirs(destination_folder, exist_ok=True)
        
        # Save the image
        file_path = os.path.join(destination_folder, filename)
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"  - Image saved: {file_path}")
    except requests.RequestException as e:
        print(f"  - Failed to download image: {e}")

def main():
    category_url = 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    # category_url = 'https://books.toscrape.com/catalogue/category/books/classics_6/index.html'
    
    # Extract category name from the URL
    category_name = category_url.split('/')[-2].split('_')[0]
    
    print("Fetching book URLs...")
    book_urls = get_book_urls(category_url)
    
    print(f"Found {len(book_urls)} books. Downloading images for each book...")
    for index, url in enumerate(book_urls, start=1):
        # Extract the book title from the URL
        book_title = url.split('/')[-2].replace('-', ' ').title()
        print(f"Processing book {index}/{len(book_urls)}: {book_title}")
        
        book_data = scrape_book_page(url)
        if book_data:
            # Download the image
            image_url = book_data['image_url']
            image_extension = os.path.splitext(image_url)[1]  # Get the file extension
            image_filename = f"{book_title}{image_extension}"
            download_image(image_url, f'images/{category_name}', image_filename)
        else:
            print(f"  - Failed to fetch book data")
    
    print(f"Finished downloading images for {len(book_urls)} books.")

if __name__ == "__main__":
    main()
