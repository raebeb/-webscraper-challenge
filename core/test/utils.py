from django.test import TestCase
from core.utils import get_books, create_soup

class UtilsTestCase(TestCase):
    def setUp(self):
        self.url = 'http://books.toscrape.com/'

    def test_create_soup(self):
        soup = create_soup(self.url)
        self.assertIsNotNone(soup)
    
    def test_create_soup_error(self):
        soup = create_soup('http://books.toscrape.com/catalogue/page-10000.html')
        self.assertIsNone(soup)

    def test_get_books(self):
        books_saved = get_books()
        self.assertTrue(books_saved)

    def tearDown(self) -> None:
        return super().tearDown()