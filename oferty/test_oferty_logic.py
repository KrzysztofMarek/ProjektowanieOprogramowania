import unittest

import oferty
from oferty import app


class TestIntegrations(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_cities_response(self):
        response = self.app.get('/cities')
        output = {"Warszawa": 1, "Sierpc": 3, "Radom": 2}
        self.assertEqual(output, response)


    def test_restaurants_response(self):
        response = self.app.get('/cities/1')
        pass

    def test_cities_response(self):
        response = self.app.get('/restaurant-offer/1')
        pass