# -*- coding: utf-8 -*-
"""TechnicalTest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15bjbLFB3JR8pmObNq2g3oDaE7klFdXok

URL : https://www.pascalcoste-shopping.com/esthetique/fond-de-teint.html
"""

import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin
import time
import random

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

def extract_product_details(product_container, base_url):
    name = product_container.find('h3', class_='product-name').text.strip()
    price = product_container.find('span', class_='uk-price').text.strip().replace('€', '').replace(',', '.')
    brand = product_container.find('div', class_='uk-width-expand').text.strip()

    a_tag = product_container.find('a', class_='product-item-photo')
    if a_tag:
        img_tag = a_tag.find('img', class_='product-image-photo')
        if img_tag:
            img_src = img_tag.get('src')
            if img_src and not img_src.startswith('data:image'):
                img_url = img_src
            else:
                img_url = img_tag.get('data-amsrc')
        else:
            img_url = None
    else:
        img_url = None

    product_url = urljoin(base_url, product_container.find('a', class_='product-item-link')['href'])

    return {
        'Name': name,
        'Price': round(float(price), 2),
        'Brand': brand,
        'Image URL': img_url,
        'Product URL': product_url
    }

def crawl_products(url):
    all_product_details = []
    headers = {'User-Agent': USER_AGENT}
    next_page_url = url

    while next_page_url:
        res  = requests.get(next_page_url, headers=headers)
        if res .status_code != 200:
            print(f"Failed to fetch {next_page_url}. Status code: {res .status_code}")
            break

        soup = BeautifulSoup(res .content, 'html.parser')
        product_containers = soup.find_all('div', class_='uk-panel')

        for container in product_containers:
            product_details = extract_product_details(container, url)
            all_product_details.append(product_details)

        next_button = soup.find('a', class_='next')
        next_page_url = urljoin(url, next_button['href']) if next_button else None

        time.sleep(random.uniform(1, 3))

    return all_product_details

def save_to_json(product_details, filename='products.json'):
    with open(filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(product_details, jsonfile, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    url = 'https://www.pascalcoste-shopping.com/esthetique/fond-de-teint.html'
    product_details = crawl_products(url)
    if product_details:
        save_to_json(product_details)
        print("Product details extracted and saved to 'products.json'.")
    else:
        print("No product details extracted.")