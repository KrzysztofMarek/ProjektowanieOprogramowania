import unittest
import json
from zaslepki_baz_danych.oddzielnie import oferty, realizacja, zamowienia, zarzadzanie_personelem, konta, zarzadzanie_siecia


class TestyKonta(unittest.TestCase):
    def setUp(self):
        self.app = konta.app.test_client()
        #uruchomienie flaska

    def tearDown(self):
        pass

    def test_pobierz_pracownika(self):
        exmpl_pracownik =  {
                'login': 'jusepe',
                'hasło': 'wodjfoph35vg',
                'stanowisko': 'Pracownik kuchni'

            }
        expctd = json.dumps(exmpl_pracownik)

        r1 = self.app.get('/pobierz_pracownika', query_string=dict(id_pracownika='jusepe'))
        self.assertEqual(json.loads(expctd), json.loads(json.dumps(r1.get_json())))


    def test_pobierz_klienta(self):
        exmpl_klient = {
                'login': 'hydroMen',
                'hasło': 'sdhvgo'

            }
        expctd = json.dumps(exmpl_klient)

        r1 = self.app.get('/pobierz_klienta', query_string=dict(id_klienta='hydroMen'))
        self.assertEqual(json.loads(expctd), json.loads(json.dumps(r1.get_json())))


class TestyOfety(unittest.TestCase):
    def setUp(self):
        self.app = oferty.app.test_client()
        #uruchomienie flaska

    def tearDown(self):
        pass

    def test_pobierz_menu_restauracji(self):
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

        r1 = self.app.get('/pobierz_menu_restauracji', query_string=dict(id_restauracji=0))
        self.assertEqual(json.loads(expctd), json.loads(json.dumps(r1.get_json())))

        r2 = self.app.get('/pobierz_menu_restauracji', query_string=dict(id_restauracji=1))
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


    def test_pobierz_restauracje(self):
        restaurant_list = {
            'lista': [
                {
                    'id_restauracji': 1,
                    'nazwa': 'Don Keke',
                    'adres': 'Liliowa 12'

                },
                {
                    'id_restauracji': 2,
                    'nazwa': 'Bambino',
                    'adres': 'Arnolda 4'
                },
                {
                    'id_restauracji': 3,
                    'nazwa': 'Que pasa',
                    'adres': 'Grunwaldzka 13'
                }
            ]
        }
        expctd = json.dumps(restaurant_list)

        r1 = self.app.get('/pobierz_restauracje', query_string=dict(miasto='Poznan'))
        self.assertEqual(json.loads(expctd), json.loads(json.dumps(r1.get_json())))

    def test_pobierz_miasta(self):
            cities_list = {
                'lista': [
                    {
                        'nazwa': 'Warszawa'
                    },
                    {
                        'nazwa': 'Radom'
                    },
                    {
                        'nazwa': 'Torun'
                    }
                ]
            }
            expctd = json.dumps(cities_list)

            r1 = self.app.get('/pobierz_miasta')
            self.assertEqual(json.loads(expctd), json.loads(json.dumps(r1.get_json())))


    def test_dodaj_danie(self):
        r1 = self.app.post('/dodaj_danie', json={
                'id_restauracji': 1,
                'nazwa': 'Naleśniki',
                'cena': 19.99,
                'opis': 'Klasyczne naleśniki'
            })
        self.assertEqual(r1.status_code, 200)

    def test_usun_danie(self):

        r1 = self.app.get('/usun_danie', query_string=dict(id_dania=1, id_restauracji=0))
        self.assertEqual(r1.status_code, 200)


class TestyRealizacja(unittest.TestCase):
    def setUp(self):
        self.app = realizacja.app.test_client()
        #uruchomienie flaska

    def tearDown(self):
         #wyłaczenie flaska
        pass

    def test_pobierz_zamowienia(self):
        r1 = self.app.get('/pobierz_zamowienia', json={'id_restauracji' : 0})
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
        r1 = self.app.post('/zmien_status_zamowienia', json={'id_zamowienia': 0, 'status': 'anulowane'})
        self.assertEqual(r1.status_code, 200)


class TestyZamowienia(unittest.TestCase):
    def setUp(self):
        self.app = zamowienia.app.test_client()
        #uruchomienie flaska

    def tearDown(self):
        pass

    def test_dodaj_zamowienie(self):
        r1 = self.app.post('/dodaj_zamowienie', json={'id_klienta': 2, 'id_restauracji':1, 'lista_dan': [{'id_dania': 1, 'nazwa': 'Chleb'},
                                                                                                         {'id_dania': 2, 'nazwa': 'Kawa'}],
                                                      'kwota': 29.99})
        self.assertEqual(r1.status_code, 200)


class TestyZarzadzaniePersonelem(unittest.TestCase):
    def setUp(self):
        self.app = zarzadzanie_personelem.app.test_client()
        # uruchomienie flaska

    def tearDown(self):
        pass

    def test_dodaj_pracownika(self):
        r1 = self.app.post('/dodaj_pracownika', json={'id_restauracji': 1, 'imie': 'Tomek', 'nazwisko': 'Potomek',
                                                      'telefon': '123456789', 'stanowisko': 'Menadzer', 'login': 'ptak',
                                                      'haslo': 'nawspak'})
        self.assertEqual(r1.status_code, 200)


if __name__ == '__main__':
    unittest.main()
