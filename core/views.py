import csv

from django.shortcuts import render
from django.http import HttpResponse
from core.utils import get_books

from core.models import Book

def index(request):
    """
    View for the home page of the site.
    Args:
        request (HttpRequest): The request object.
    Returns:
        template (str): template to render
    """
    return render(request,'core/index.html')


def create_csv(request):
    """
    View used to create a csv file of all books in the database.
    Args:
        request (HttpRequest): The request object.

    Returns:
        response (HttpResponse): The response object with file to download.
    """

    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'
    writer = csv.writer(response,  delimiter=';')  

    # Save books to database
    books_saved = get_books()

    if books_saved is True:
        books = Book.objects.all()

        response.write(u'\ufeff'.encode('utf8'))
        writer.writerow(['Title', 'Price', 'Stock', 'Category', 'Cover', 'UPC', 'Product Type', 'Price Excl. Tax', 'Price Incl. Tax', 'Tax', 'Availability', 'Number of Reviews'])
        for book in books:
            response.write(u'\ufeff'.encode('utf8'))
            writer = csv.writer(response,  delimiter=';')  
            writer.writerow([book.title, book.price, book.stock, book.category, book.cover, book.upc, book.product_type, book.price_excl_tax, book.price_incl_tax, book.tax, book.availability, book.number_of_reviews])

        return response

    else:
        return render(request,'core/index.html')
