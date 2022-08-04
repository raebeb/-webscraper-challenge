from django.test import TestCase
from core.utils import get_books, create_soup

class UtilsTestCase(TestCase):
    """
    Test for the utils.py file methods

    Args:
        TestCase (class): TestCase class
    """
    def setUp(self):
        """
        Define url for testing purposes
        """
        self.url = 'http://books.toscrape.com/'

    def test_create_soup(self):
        """
        Test the create_soup function
        """
        soup = create_soup(self.url)
        self.assertIsNotNone(soup)

    def test_create_soup_error(self):
        """
        Test the create_soup function with an error
        """
        soup = create_soup('http://books.toscrape.com/catalogue/page-10000.html')
        self.assertIsNone(soup)

    def test_get_books(self):
        """
        Test the get_books function
        """
        books_saved = get_books()
        self.assertTrue(books_saved)
