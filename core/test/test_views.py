from django.test import TestCase

class ViewsTestCase(TestCase):
    """
    test cases for views
    Args:
        TestCase (class): TestCase class
    """

    def test_index(self):
        """
        Test the index page
        """
        response = self.client.get('/core/')
        self.assertEqual(response.status_code, 200)

    def test_create_csv(self):
        """
        Test the create_csv page
        """
        response = self.client.get('/core/getfile/')
        self.assertEqual(response.status_code, 200)