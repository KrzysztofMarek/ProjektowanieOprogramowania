import unittest
import json
from zaslepki_baz_danych import ZASLEPKA


class TestyZaslepka(unittest.TestCase):
    def setUp(self):
        self.app = ZASLEPKA.app.test_client()
        # uruchomienie flaska

    def tearDown(self):
        pass

    def test_pobierz_pracownika(self):
        exmpl_pracownik = {
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

    def test_pobierz_restauracje_z_miasta(self):
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

        r1 = self.app.get('/pobierz_restauracje_z_miasta', query_string=dict(miasto='Poznan'))
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
        self.assertEqual(200, r1.status_code)

    def test_usun_danie(self):
        r1 = self.app.get('/usun_danie', query_string=dict(id_dania=1, id_restauracji=0))
        self.assertEqual(r1.status_code, 200)

    def test_modyfikuj_danie(self):
        r1 = self.app.post('/modyfikuj_danie', json={
            'id_restauracji': 1,
            'id_dania': 1,
            'nazwa': 'Naleśniki',
            'cena': 19.99,
            'opis': 'Klasyczne naleśniki'
        })
        self.assertEqual(200, r1.status_code)

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
                    'kontakt': {'imie': 'Jan', 'nazwisko': 'Kowalski', 'telefon': '123456789',
                                'adres': 'Konwaliowa 3'}
                },
                {
                    'id_zamowienia': 2,
                    'lista_dan': [
                        {'id_dania': 1, 'nazwa': 'Kawa'},
                        {'id_dania': 2, 'nazwa': 'Ciastko'},
                        {'id_dania': 3, 'nazwa': 'Bulka'}
                    ],
                    'status': 'przygotowywane',
                    'kontakt': {'imie': 'Adam', 'nazwisko': 'Wypadam', 'telefon': '123456789', 'adres': 'Wysoka 3'}

                },
                {
                    'id_zamowienia': 3,
                    'lista_dan': [
                        {'id_dania': 1, 'nazwa': 'Kawa'},
                        {'id_dania': 2, 'nazwa': 'Ciastko'},
                        {'id_dania': 3, 'nazwa': 'Bulka'}
                    ],
                    'status': 'w_drodze',
                    'kontakt': {'imie': 'Andrzej', 'nazwisko': 'Adrianowski', 'telefon': '123456789',
                                'adres': 'Cicha 3'}
                }
            ]
        }
        expctd = json.dumps(json_data)
        self.assertEqual(json.loads(expctd), json.loads(json.dumps(r1.get_json())))

    def test_zmien_status_zamowienia(self):
        r1 = self.app.post('/zmien_status_zamowienia', json={'id_zamowienia': 0, 'status': 'anulowane'})
        self.assertEqual(r1.status_code, 200)

    def test_dodaj_zamowienie_Z(self):
        r1 = self.app.post('/dodaj_zamowienie_Z',
                           json={'id_klienta': 2, 'id_restauracji': 1,
                                 'lista_dan': [{'id_dania': 1, 'nazwa': 'Chleb'},
                                               {'id_dania': 2, 'nazwa': 'Kawa'}],
                                 'kwota': 29.99})
        self.assertEqual(r1.status_code, 200)

    def test_edytuj_zamowienie_Z(self):
        r1 = self.app.post('/edytuj_zamowienie_Z',
                           json={'id_zamowienia': 1, 'lista_dan': [{'id_dania': 1, 'nazwa': 'Chleb'},
                                                                   {'id_dania': 2, 'nazwa': 'Kawa'}],
                                 'cena': 55.55})
        self.assertEqual(r1.status_code, 200)

    def test_zmien_status_zamowienia_Z(self):
        r1 = self.app.post('/zmien_status_zamowienia_Z', json={'id_zamowienia': 1, 'status': 'anulowane'})
        self.assertEqual(r1.status_code, 200)

    def test_pobierz_zamowienia_Z(self):
        lista_zamowien = {
            'lista_zamowien': [
                {
                    'id_zamowienia': 1,
                    'id_klienta': 1,
                    'id_restauracji': 1,
                    'lista_dan': [
                        {'id_dania': 1, 'nazwa': 'Kawa'},
                        {'id_dania': 2, 'nazwa': 'Ciastko'},
                        {'id_dania': 3, 'nazwa': 'Bulka'}
                    ],
                    'kwota': 26.88,
                    'status': 'oczekujace',
                    'data_zlozenia': '2018-09-10',
                    'ocena': '2/10',
                    'adres': "Grunwaldzka 13"
                },
                {
                    'id_zamowienia': 2,
                    'id_klienta': 2,
                    'id_restauracji': 3,
                    'lista_dan': [
                        {'id_dania': 1, 'nazwa': 'Kawa'},
                        {'id_dania': 2, 'nazwa': 'Ciastko'},
                        {'id_dania': 3, 'nazwa': 'Bulka'}
                    ],
                    'kwota': 59.88,
                    'status': 'przygotowywane',
                    'data_zlozenia': '2018-06-11',
                    'ocena': '4/10',
                    'adres': "Wolności 15"

                },
                {
                    'id_zamowienia': 3,
                    'id_klienta': 1,
                    'id_restauracji': 5,
                    'lista_dan': [
                        {'id_dania': 1, 'nazwa': 'Kawa'},
                        {'id_dania': 2, 'nazwa': 'Ciastko'},
                        {'id_dania': 3, 'nazwa': 'Bulka'}
                    ],
                    'kwota': 43.80,
                    'status': 'w_drodze',
                    'data_zlozenia': '2018-12-16',
                    'ocena': '8/10',
                    'adres': "Alternatywy 4"

                }
            ]
        }
        r1 = self.app.get('/pobierz_zamowienia_Z', query_string=dict(id_restauracji=0))
        expctd = json.dumps(lista_zamowien)
        self.assertEqual(json.loads(expctd), json.loads(json.dumps(r1.get_json())))

    def test_pobierz_zamowienie_Z(self):
        zamowienie = {
            'id_zamowienia': 1,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 26.88,
            'status': 'oczekujace',
            'data_zlozenia': '2018-09-10',
            'ocena': '2/10',
            'adres': "Grunwaldzka 13"
        }
        r1 = self.app.get('/pobierz_zamowienie_Z', query_string=dict(id_zamowienia=0))
        expctd = json.dumps(zamowienie)
        self.assertEqual(json.loads(expctd), json.loads(json.dumps(r1.get_json())))

    def test_pobierz_pracownikow(self):
        lista_pracownikow = {
            'lista_pracownikow': [
                {
                    'id_pracownika': 'janPan',
                    'id_restauracji': 1,
                    'imie': 'Jan',
                    'nazwisko': 'Nowak',
                    'telefon': '123456789',
                    'stanowisko': 'pracownik kuchni',
                    'haslo': 'soicrupogi'
                },
                {
                    'id_pracownika': 'AAmen',
                    'id_restauracji': 2,
                    'imie': 'Andrzej',
                    'nazwisko': 'Adrianowski',
                    'telefon': '777888999',
                    'stanowisko': 'dostawca',
                    'haslo': '39084utco'

                },
                {
                    'id_pracownika': 'KNow',
                    'id_restauracji': 4,
                    'imie': 'Kasia',
                    'nazwisko': 'Nowak',
                    'telefon': '333444555',
                    'stanowisko': 'menadzer restauracji',
                    'haslo': 'kKdPS'

                }
            ]
        }
        r1 = self.app.get('/pobierz_pracownikow', query_string=dict(id_restauracji=0))
        expctd = json.dumps(lista_pracownikow)
        self.assertEqual(json.loads(expctd), json.loads(json.dumps(r1.get_json())))

    def test_dodaj_pracownika(self):
        r1 = self.app.post('/dodaj_pracownika', json={'id_restauracji': 1, 'imie': 'Tomek', 'nazwisko': 'Potomek',
                                                      'telefon': '123456789', 'stanowisko': 'Menadzer',
                                                      'id_pracownika': 'ptak',
                                                      'haslo': 'nawspak'})
        self.assertEqual(r1.status_code, 200)

    def test_usun_pracownika(self):
        r1 = self.app.get('/usun_pracownika', query_string=dict(id_pracownika='janPan'))
        self.assertEqual(r1.status_code, 200)

    def test_pobierz_restauracje(self):
        lista_restauracji = {
            'lista_restauracji': [
                {
                    'nazwa': 'Cebuliowo',
                    'id_restauracji': 1,
                    'adres': 'Bitwy 17'
                },
                {
                    'nazwa': 'Pizza House',
                    'id_restauracji': 2,
                    'adres': 'Okopowa 2'
                },
                {
                    'nazwa': 'Students Dream',
                    'id_restauracji': 3,
                    'adres': 'Granadierow 5'
                },
                {
                    'nazwa': 'AleJazda!',
                    'id_restauracji': 4,
                    'adres': 'Działowa 12'
                }
            ]
        }
        r1 = self.app.get('/pobierz_restauracje')
        expctd = json.dumps(lista_restauracji)
        self.assertEqual(json.loads(expctd), json.loads(json.dumps(r1.get_json())))

    def test_dodaj_restauracje(self):
        r1 = self.app.post('/dodaj_restauracje', json={
            'nazwa': 'AleJazda!',
            'adres': 'Działowa 12'
        })
        self.assertEqual(r1.status_code, 200)

    def test_usun_restauracje(self):
        r1 = self.app.get('/usun_restauracje', query_string=dict(id_restauracji=1))
        self.assertEqual(r1.status_code, 200)


if __name__ == '__main__':
    unittest.main()
