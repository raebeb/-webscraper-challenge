from django.test import TestCase
from django.test import Client

class ViewsTestCase(TestCase):
    def setUp(self):
        pass

    def test_index(self):
        response = self.client.get('/core/')
        self.assertEqual(response.status_code, 200)

    def test_create_csv(self):
        response = self.client.get('/core/getfile/')
        self.assertEqual(response.status_code, 200)