import unittest

import oferty_logic
from oferty_logic import app


class TestIntegrations(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_cities_response(self):
        response = self.app.get('/cities')
        output = {"Warszawa": 1, "Sierpc": 2, "Radom": 3}
        self.assertEqual(output, response)


    def test_restaurants_response(self):
        response = self.app.get('/cities/offer')
        pass

    def test_cities_response(self):
        response = self.app.get('/cities/offer/restaurant')
        pass