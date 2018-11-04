import unittest
import json
from zaslepki_baz_danych import oferty, realizacja, zamowienia, zarzadzanie_personelem


class TestyOfety(unittest.TestCase):
    def setUp(self):
        self.app = oferty.app.test_client()
        #uruchomienie flaska

    def tearDown(self):
        pass

    def test_pobierz_menu_restauracji(self):
        #r1 = self.app.get('/pobierz_menu_restauracji', json={'id_restauracji': 0})
        r1 = self.app.get('/pobierz_menu_restauracji', query_string=dict(id_restauracji=0))
        json_data = {
            'lista': [
            {
                'id_dania': 1,
                'nazwa': 'Ciastko',
                'cena': 29.99,
                'opis': 'Pycha ciacho'

            },
            {
                'id_dania': 2,
                'nazwa': 'Kawa',
                'cena': 5.99,
                'opis': 'Dobra kawusia'
            }
        ]
        }
        expctd = json.dumps(json_data)
        self.assertEqual(json.loads(expctd), json.loads(json.dumps(r1.get_json())))

        r2 = self.app.get('/pobierz_menu_restauracji', query_string=dict(id_restauracji=2))
        restaurant_menu = {
            'lista': [
                {
                    'id_dania': 1,
                    'nazwa': 'Ciastko',
                    'cena': 29.99,
                    'opis': 'Pycha ciacho'

                },
                {
                    'id_dania': 2,
                    'nazwa': 'Kawa',
                    'cena': 5.99,
                    'opis': 'Dobra kawusia'
                },
                {
                    'id_dania': 3,
                    'nazwa': 'Bułka',
                    'cena': 2.99,
                    'opis': 'Duża buła'
                }
            ]
        }
        expctd = json.dumps(restaurant_menu)
        self.assertEqual(json.loads(expctd), json.loads(json.dumps(r2.get_json())))

class TestyRealizacja(unittest.TestCase):
    def setUp(self):
        self.app = realizacja.app.test_client()
        #uruchomienie flaska

    def tearDown(self):
         #wyłaczenie flaska
        pass

    def test_pobierz_zamowienia(self):
        r1 = self.app.get('/pobierz_zamowienia', query_string=dict(id_restauracji=0))
        json_data = {
            'lista_zamowien': [
                {
                    'id_zamowienia': 1,
                    'lista_dan': [
                        {'id_dania': 1, 'nazwa': 'Kawa'},
                        {'id_dania': 2, 'nazwa': 'Ciastko'},
                        {'id_dania': 3, 'nazwa': 'Bulka'}
                    ],
                    'status': 'oczekujace',
                },
                {
                    'id_zamowienia': 2,
                    'lista_dan': [
                        {'id_dania': 1, 'nazwa': 'Kawa'},
                        {'id_dania': 2, 'nazwa': 'Ciastko'},
                        {'id_dania': 3, 'nazwa': 'Bulka'}
                    ],
                    'status': 'przygotowywane',

                },
                {
                    'id_zamowienia': 3,
                    'lista_dan': [
                        {'id_dania': 1, 'nazwa': 'Kawa'},
                        {'id_dania': 2, 'nazwa': 'Ciastko'},
                        {'id_dania': 3, 'nazwa': 'Bulka'}
                    ],
                    'status': 'w_drodze',

                }
            ]
        }
        expctd = json.dumps(json_data)
        self.assertEqual(json.loads(expctd), json.loads(json.dumps(r1.get_json())))

    def test_zmien_status_zamowienia(self):
        r1 = self.app.post('/zmien_status_zamowienia', data=dict(id_zamowienia=0, status='anulowane'))
        self.assertEqual(r1.status_code, 200)


class TestyZamowienia(unittest.TestCase):
    def setUp(self):
        self.app = zamowienia.app.test_client()
        #uruchomienie flaska

    def tearDown(self):
        pass

    def test_dodaj_zamowienie(self):
        r1 = self.app.post('/dodaj_zamowienie', data=dict(id_klienta=2, id_restauracji=1, lista_dan=[1, 'Chleb',
                                                                                                     2, 'Kwa'],
                                                                                                      kwota=29.99))
        self.assertEqual(r1.status_code, 200)


class TestyZarzadzaniePersonelem(unittest.TestCase):
    def setUp(self):
        self.app = zarzadzanie_personelem.app.test_client()
        # uruchomienie flaska

    def tearDown(self):
        pass

    def test_dodaj_pracownika(self):
        r1 = self.app.post('/dodaj_pracownika',data=dict(id_restauracji=1, imie="Tomek", nazwisko="Potomek",
                                                         telefon="123456789", stanowisko='Manadzer',
                                                         login='ptak', haslo='nawspak'))
        self.assertEqual(r1.status_code, 200)


if __name__ == '__main__':
    unittest.main()
