import requests
from bs4 import BeautifulSoup
import csv
import json  # Used only for pretty-printing the result
from urllib.parse import urljoin
import os
import re

def scrape_book_page(url):
    """
    Scrapes a book page from the OldBooks Finder website and extracts relevant information.

    Args:
    url (str): The URL of the book page to scrape.

    Returns:
    dict: A dictionary containing the following book information:
        - product_page_url (str): The URL of the book page
        - universal_product_code (str): The UPC of the book
        - title (str): The title of the book
        - price_including_tax (str): The price including tax
        - price_excluding_tax (str): The price excluding tax
        - number_available (str): The number of books available
        - product_description (str): The description of the book
        - category (str): The category of the book
        - review_rating (str): The review rating of the book
        - image_url (str): The URL of the book's image

    Returns None if the page couldn't be retrieved or parsed successfully.

    Raises:
    requests.RequestException: If there's an error in making the HTTP request.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Ensure we're using the correct encoding
        response.encoding = response.apparent_encoding
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract required information
            title = soup.find('h1').text.strip()
            category = soup.find('ul', class_='breadcrumb').find_all('li')[2].text.strip()
            
            # Extract product information
            product_info = {}
            table = soup.find('table', class_='table table-striped')
            if table:
                rows = table.find_all('tr')
                for row in rows:
                    key = row.find('th').text.strip()
                    value = row.find('td').text.strip()
                    product_info[key] = value
            
            # Extract other required fields
            book_data = {
                'product_page_url': url,
                'universal_product_code (upc)': product_info.get('UPC', ''),
                'title': title,
                'price_including_tax': product_info.get('Price (incl. tax)', ''),
                'price_excluding_tax': product_info.get('Price (excl. tax)', ''),
                'number_available': product_info.get('Availability', '').split('(')[-1].split()[0],
                'product_description': soup.select_one('meta[name="description"]')['content'].strip(),
                'category': category,
                'review_rating': soup.find('p', class_='star-rating')['class'][1],
                'image_url': 'https://books.toscrape.com/' + soup.find('img')['src'].replace('../', '')
            }
            
            return book_data
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"An error occurred while making the request: {e}")
        return None

def save_to_csv(data, filename):
    """
    Saves the given data to a CSV file.

    Args:
    data (list of dict): The data to be saved, where each dict represents a row.
    filename (str): The name of the file to save the data to.
    """
    if data:
        keys = data[0].keys()
        with open(filename, 'w', newline='', encoding='utf-8') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)

def get_book_urls(category_url):
    """
    Retrieves all book URLs from a given category page, including pagination.

    This function scrapes the initial category page and any subsequent pages,
    collecting URLs for all books in the category.

    Args:
    category_url (str): The URL of the category page to start scraping from.

    Returns:
    list of str: A list of URLs, each pointing to a specific book's page.

    Raises:
    requests.RequestException: If there's an error in making the HTTP request.
    """
    book_urls = []
    while category_url:
        print(f"Fetching page: {category_url}")
        try:
            response = requests.get(category_url)
            response.raise_for_status()
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
        except requests.RequestException as e:
            print(f"An error occurred while fetching {category_url}: {e}")
            category_url = None
    
    print(f"Total books found: {len(book_urls)}")
    return book_urls

def get_categories(url):
    """
    Extracts the list of book categories from the home page.

    Args:
    url (str): The URL of the home page.

    Returns:
    list of tuple: A list of (category_name, category_url) tuples.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        categories = []
        category_list = soup.select('ul.nav-list > li > ul > li > a')
        
        for category in category_list:
            category_name = category.text.strip()
            category_url = urljoin(url, category['href'])
            categories.append((category_name, category_url))
        
        return categories
    except requests.RequestException as e:
        print(f"An error occurred while fetching the categories: {e}")
        return []

def download_image(url, destination_folder, filename):
    """Download and save an image from a given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # Create the destination folder if it doesn't exist
        os.makedirs(destination_folder, exist_ok=True)
        
        # Clean the filename
        clean_filename = re.sub(r'[\\/*?:"<>|]', "_", filename)
        
        # Save the image
        file_path = os.path.join(destination_folder, clean_filename)
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"    Image saved: {file_path}")
        return True
    except requests.RequestException as e:
        print(f"    Failed to download image: {e}")
        return False
