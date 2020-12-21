from django.test import SimpleTestCase

# Create your tests here.
class SimpleTests(SimpleTestCase):
    def test_listing_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
    def test_search_page_status_code(self):
        response = self.client.get('/listings/search/')
        self.assertEquals(response.status_code, 200)