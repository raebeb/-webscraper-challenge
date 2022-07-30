from bs4 import BeautifulSoup
import requests
import csv

def get_books():
    """
    Get all books from a page
    """
    base_url = 'http://books.toscrape.com/'
    for page in range(1, 51):
        print('********************************')
        print(f'PAGE {page}')

        query_parameter = f'catalogue/page-{page}.html'
        full_url = base_url + query_parameter
        print(type(full_url))
        response = requests.get(full_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        books = soup.find_all('article')

        for book in books:
            print('*** START BOOK ***')
            #print(f'RESPONSE =====> {book}')
            book_query_parameter = book.find('a')['href']
            book_title = book.find('h3').text
            book_cover = book.find(class_='thumbnail')['src']
            print(f'cover ====> {book_cover}')
            print(f'Title =====> {book_title}')
            print(f'url =====> {book_query_parameter}')
            book_full_url = base_url + 'catalogue/' + book_query_parameter
            response = requests.get(book_full_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            price = soup.find(class_='price_color').text
            print(f'price ===> {price}')
            stock = soup.find(class_='instock availability').text
            print(f'STOCK ==> {stock}')
            category = soup.find_all('li')[2].text
            print(f'CATEGORY ===> {category}')

            ### PRODUCT INFO

            table = soup.find_all('tr')
            upc = table[0].text
            product_type = table[1].find('td').text
            price_excl_tax = table[2].find('td').text
            price_incl_tax = table[3].find('td').text
            tax = table[4].find('td').text
            availabililty = table[5].find('td').text
            number_of_reviews = table[6].find('td').text

            print(f'TABLE ===> {number_of_reviews}')

            print('*** END BOOK ***')
