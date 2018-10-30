import unittest

from oferty.oferty_logic import app


class TestIntegrations(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_cities_response(self):
        response = self.app.get('/cities')
        output = {"Warszawa": 1, "Sierpc": 3, "Radom": 2}
        self.assertEqual(output, response.form)

    def test_restaurants_response(self):
        response = self.app.get('/cities/1')
        self.assertNotEqual(None, response.form)

    def test_cities_response(self): 
        response = self.app.get('/restaurant-offer/1')
        self.assertNotEqual(None, response.form)
