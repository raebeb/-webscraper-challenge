from bs4 import BeautifulSoup
import requests
import csv
import logging
from django.core.exceptions import ObjectDoesNotExist
from core.models import Book

def create_soup(url):
    """
    Create a BeautifulSoup object from a url

    Args:
        url (str): url to make request to

    Returns:
        soup (BeautifulSoup): BeautifulSoup object generated from response
    """
    response = requests.get(url)
    if response.status_code != 200:
        logging.error(f'Error: {response}')
        return None
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def get_books():
    
    """
    Get all books from a page
    """
    base_url = 'http://books.toscrape.com/'
    for page in range(1, 51):
        print('********************************')
        print(f'PAGE {page}')

        query_parameter = f'catalogue/page-{page}.html'
        full_url = f'{base_url}{query_parameter}'
        soup = create_soup(full_url)

        if soup is None:
            logging.error(f'Error: {soup}')
            continue

        books = soup.find_all('article')

        for book in books:
            print('*** START BOOK ***')

            book_query_parameter = book.find('a')['href']
            book_full_url = f'{base_url}catalogue/{book_query_parameter}'
            soup = create_soup(book_full_url)
            
            if soup is None:
                logging.error(f'Error: {soup}')
                continue

            try:
                table = soup.find_all('tr')
                upc = (table[0].text).strip()
                new_book = Book.objects.get(upc=upc)
                print(f'*** BOOK {new_book.title} EXISTS IN DATABASE ***')
            except ObjectDoesNotExist:
                new_book = Book()
                new_book.title = soup.find('h1').text
                new_book.price = (soup.find(class_='price_color').text).replace('Â', '')
                new_book.stock = (soup.find(class_='instock availability').text).strip()
                new_book.category = (soup.find_all('li')[2].text).strip()
                new_book.cover = f"{base_url}{book.find(class_='thumbnail')['src']}"
                table = soup.find_all('tr')
                new_book.upc = (table[0].text).strip()
                new_book.product_type = table[1].find('td').text
                new_book.price_excl_tax = (table[2].find('td').text).replace('Â', '')
                new_book.price_incl_tax = (table[3].find('td').text).replace('Â', '')
                new_book.tax = (table[4].find('td').text).replace('Â', '')
                new_book.availability = table[5].find('td').text
                new_book.number_of_reviews = int(table[6].find('td').text)
                new_book.save()

                print(f'*** BOOK {new_book.title} SAVED! ***')

    return True

