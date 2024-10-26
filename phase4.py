from scrape import get_categories, get_book_urls, scrape_book_page, save_to_csv, download_image
import os

def main():
    home_url = 'https://books.toscrape.com/index.html'
    categories = get_categories(home_url)
    
    print("Starting to scrape all categories...")
    for category_name, category_url in categories:
        print(f"\nProcessing category: {category_name}")
        
        # Get all book URLs for this category
        book_urls = get_book_urls(category_url)
        
        # Scrape data for each book
        all_book_data = []
        for index, url in enumerate(book_urls, start=1):
            print(f"  Scraping book {index}/{len(book_urls)}")
            book_data = scrape_book_page(url)
            if book_data:
                all_book_data.append(book_data)
                
                # Download the image
                image_url = book_data['image_url']
                image_filename = f"{book_data['title'].replace(' ', '_')}.jpg"
                download_image(image_url, f'images/{category_name}', image_filename)
            else:
                print(f"  Failed to scrape book: {url}")
        
        # Save category data to CSV
        if all_book_data:
            csv_filename = f'csv/{category_name.replace(" ", "_")}.csv'
            os.makedirs('csv', exist_ok=True)
            save_to_csv(all_book_data, csv_filename)
            print(f"  Saved data for {len(all_book_data)} books to {csv_filename}")
        else:
            print(f"  No data was scraped for category: {category_name}")

if __name__ == "__main__":
    main()
