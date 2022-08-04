from django.test import TestCase

from core.models import Book

class BookTestCase(TestCase):
    """
    test cases for book model
    Args:
        TestCase (class): TestCase class
    """
    def setUp(self):
        """
        Create a book for testing purposes
        """
        Book.objects.create(
            title='Book 1',
            price='$10.00',
            stock='10',
            category='Category 1',
            cover='Cover 1',
            upc='UPC 1',
            product_type='Product Type 1',
            price_excl_tax='$10.00',
            price_incl_tax='$10.00',
            tax='$10.00',
            availability='Available',
            number_of_reviews=10)

    def test_book_title(self):
        """
        Test the title of the book
        """
        book = Book.objects.get(title='Book 1')
        self.assertEqual(book.title, 'Book 1')

    def test_book_price(self):
        """
        Test the price of the book
        """
        book = Book.objects.get(price='$10.00')
        self.assertEqual(book.price, '$10.00')

    def test_book_stock(self):
        """
        Test the stock of the book
        """
        book = Book.objects.get(stock='10')
        self.assertEqual(book.stock, '10')

    def test_book_category(self):
        """
        Test the category of the book
        """
        book = Book.objects.get(category='Category 1')
        self.assertEqual(book.category, 'Category 1')

    def test_book_cover(self):
        """
        Test the cover of the book
        """
        book = Book.objects.get(cover='Cover 1')
        self.assertEqual(book.cover, 'Cover 1')

    def test_book_upc(self):
        """
        Test the upc of the book
        """
        book = Book.objects.get(upc='UPC 1')
        self.assertEqual(book.upc, 'UPC 1')

    def test_book_product_type(self):
        """
        Test the product type of the book
        """
        book = Book.objects.get(product_type='Product Type 1')
        self.assertEqual(book.product_type, 'Product Type 1')

    def test_book_price_excl_tax(self):
        """
        Test the price excl tax of the book
        """
        book = Book.objects.get(price_excl_tax='$10.00')
        self.assertEqual(book.price_excl_tax, '$10.00')

    def test_book_price_incl_tax(self):
        """
        Test the price incl tax of the book
        """
        book = Book.objects.get(price_incl_tax='$10.00')
        self.assertEqual(book.price_incl_tax, '$10.00')

    def test_book_tax(self):
        """
        Test the tax of the book
        """
        book = Book.objects.get(tax='$10.00')
        self.assertEqual(book.tax, '$10.00')

    def test_book_availability(self):
        """
        Test the availability of the book
        """
        book = Book.objects.get(availability='Available')
        self.assertEqual(book.availability, 'Available')

    def test_book_number_of_reviews(self):
        """
        Test the number of reviews of the book
        """
        book = Book.objects.get(number_of_reviews=10)
        self.assertEqual(book.number_of_reviews, 10)   

    def tearDown(self) -> None:
        """
        Clean up after each test
        """
        Book.objects.all().delete()
