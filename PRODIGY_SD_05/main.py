import sys
sys.path.append("C:/Users/Admin/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0/LocalCache/local-packages/Python311/site-packages")

import requests
from bs4 import BeautifulSoup
import csv

url = 'https://exclusivebooks.co.za/'

def scrape_eCommerce_website(url):

    response = requests.get(url)

    if response.status_code == 200:
     
        soup = BeautifulSoup(response.content, 'html.parser')

       
        product_data = []

        product_names = soup.select('.product-name')  
        product_prices = soup.select('.product-price')  
        product_ratings = soup.select('.product-rating')  

        for name, price, rating in zip(product_names, product_prices, product_ratings):
            product_data.append({
                'Name': name.get_text(strip=True),
                'Price': price.get_text(strip=True),
                'Rating': rating.get_text(strip=True)
            })

        return product_data
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return None

def save_to_csv(data, filename='product_data.csv'):

    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Name', 'Price', 'Rating']  # Adjust based on the extracted data
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)


        writer.writeheader()

     
        writer.writerows(data)

if __name__ == "__main__":

    website_url = 'https://exclusivebooks.co.za/'
    

    scraped_data = scrape_eCommerce_website(website_url)

    if scraped_data:
  
        save_to_csv(scraped_data)
        print(f"Scraped data saved to 'product_data.csv'")