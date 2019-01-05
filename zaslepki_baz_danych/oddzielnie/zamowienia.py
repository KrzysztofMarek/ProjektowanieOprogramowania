from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)


@app.route('/')
def main_site():
    return 404


lista_zamowien_Z = {
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
            'ocena': 2,
            'miasto': 'Warszawa',
            'adres': "Grunwaldzka 13"
        },
        {
            'id_zamowienia': 2,
            'id_klienta': 2,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 59.88,
            'status': 'dostarczone',
			'oplacone': True,
            'data_zlozenia': '2018-06-11',
            'ocena': 4,
            'miasto': 'Gdynia',
            'adres': "Wolności 15"

        },
        {
            'id_zamowienia': 3,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Radom',
            'adres': "Alternatywy 4"

        },
        {
            'id_zamowienia': 4,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Radom',
            'adres': "Alternatywy 4"

        },
        {
            'id_zamowienia': 5,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'dostarczone',
			'oplacone': True,
            'czas_dostawy': 72,
            'czas_realizacji': 45,
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Gdynia',
            'adres': "Alternatywy 4"

        },
        {
            'id_zamowienia': 6,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'dostarczone',
			'oplacone': True,
            'czas_dostawy': 12,
            'czas_realizacji': 25,
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Gdynia',
            'adres': "Alternatywy 4"

        },
        {
            'id_zamowienia': 7,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Gdynia',
            'adres': "Alternatywy 4"

        },
        {
            'id_zamowienia': 8,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Warszawa',
            'adres': "Alternatywy 4"
        },
        {
            'id_zamowienia': 9,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Warszawa',
            'adres': "Alternatywy 4"
        },
        {
            'id_zamowienia': 10,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Gdynia',
            'adres': "Alternatywy 4"
        },
        {
            'id_zamowienia': 11,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'dostarczone',
			'oplacone': True,
            'czas_dostawy': 32,
            'czas_realizacji': 44,
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Radom',
            'adres': "Alternatywy 4"
        },
        {
            'id_zamowienia': 12,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Gdynia',
            'adres': "Alternatywy 4"
        },
        {
            'id_zamowienia': 13,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Warszawa',
            'adres': "Alternatywy 4"
        },
        {
            'id_zamowienia': 14,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'dostarczone',
			'oplacone': True,
            'czas_dostawy': 18,
            'czas_realizacji': 67,
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Warszawa',
            'adres': "Alternatywy 4"
        },
        {
            'id_zamowienia': 15,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'dostarczone',
			'oplacone': True,
            'czas_dostawy': 32,
            'czas_realizacji': 85,
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Gdynia',
            'adres': "Alternatywy 4"
        },
        {
            'id_zamowienia': 16,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 26.88,
            'status': 'dostarczone',
			'oplacone': True,
            'czas_dostawy': 22,
            'czas_realizacji': 15,
            'data_zlozenia': '2018-09-10',
            'ocena': 2,
            'miasto': 'Warszawa',
            'adres': "Grunwaldzka 13"
        },
        {
            'id_zamowienia': 17,
            'id_klienta': 2,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 59.88,
            'status': 'dostarczone',
			'oplacone': True,
            'czas_dostawy': 10,
            'czas_realizacji': 28,
            'data_zlozenia': '2018-06-11',
            'ocena': 4,
            'miasto': 'Gdynia',
            'adres': "Wolności 15"

        },
        {
            'id_zamowienia': 18,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Radom',
            'adres': "Alternatywy 4"

        },
        {
            'id_zamowienia': 19,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Radom',
            'adres': "Alternatywy 4"

        },
        {
            'id_zamowienia': 20,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'dostarczone',
			'oplacone': True,
            'czas_dostawy': 92,
            'czas_realizacji': 35,
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Gdynia',
            'adres': "Alternatywy 4"

        },
        {
            'id_zamowienia': 21,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'dostarczone',
			'oplacone': True,
            'czas_dostawy': 22,
            'czas_realizacji': 34,
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Gdynia',
            'adres': "Alternatywy 4"

        },
        {
            'id_zamowienia': 22,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Gdynia',
            'adres': "Alternatywy 4"

        },
        {
            'id_zamowienia': 23,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Warszawa',
            'adres': "Alternatywy 4"
        },
        {
            'id_zamowienia': 24,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Warszawa',
            'adres': "Alternatywy 4"
        },
        {
            'id_zamowienia': 25,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Gdynia',
            'adres': "Alternatywy 4"
        },
        {
            'id_zamowienia': 26,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'dostarczone',
			'oplacone': True,
            'czas_dostawy': 12,
            'czas_realizacji': 8,
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Radom',
            'adres': "Alternatywy 4"
        },
        {
            'id_zamowienia': 27,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Gdynia',
            'adres': "Alternatywy 4"
        },
        {
            'id_zamowienia': 28,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Warszawa',
            'adres': "Alternatywy 4"
        },
        {
            'id_zamowienia': 29,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'dostarczone',
			'oplacone': True,
            'czas_dostawy': 58,
            'czas_realizacji': 13,
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Warszawa',
            'adres': "Alternatywy 4"
        },
        {
            'id_zamowienia': 30,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Gdynia',
            'adres': "Alternatywy 4"
        },
{
            'id_zamowienia': 31,
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
            'ocena': 2,
            'miasto': 'Warszawa',
            'adres': "Grunwaldzka 13"
        },
        {
            'id_zamowienia': 32,
            'id_klienta': 2,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 59.88,
            'status': 'dostarczone',
			'oplacone': True,
            'czas_dostawy': 72,
            'czas_realizacji': 45,
            'data_zlozenia': '2018-06-11',
            'ocena': 4,
            'miasto': 'Gdynia',
            'adres': "Wolności 15"

        },
        {
            'id_zamowienia': 33,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Radom',
            'adres': "Alternatywy 4"

        },
        {
            'id_zamowienia': 34,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Radom',
            'adres': "Alternatywy 4"

        },
        {
            'id_zamowienia': 35,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'dostarczone',
			'oplacone': True,
            'czas_dostawy': 19,
            'czas_realizacji': 56,
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Gdynia',
            'adres': "Alternatywy 4"

        },
        {
            'id_zamowienia': 36,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'dostarczone',
			'oplacone': True,
            'czas_dostawy': 14,
            'czas_realizacji': 37,
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Gdynia',
            'adres': "Alternatywy 4"

        },
        {
            'id_zamowienia': 37,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Gdynia',
            'adres': "Alternatywy 4"

        },
        {
            'id_zamowienia': 38,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Warszawa',
            'adres': "Alternatywy 4"
        },
        {
            'id_zamowienia': 39,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Warszawa',
            'adres': "Alternatywy 4"
        },
        {
            'id_zamowienia': 40,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Gdynia',
            'adres': "Alternatywy 4"
        },
        {
            'id_zamowienia': 41,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'dostarczone',
			'oplacone': True,
            'czas_dostawy': 72,
            'czas_realizacji': 45,
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Radom',
            'adres': "Alternatywy 4"
        },
        {
            'id_zamowienia': 42,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Gdynia',
            'adres': "Alternatywy 4"
        },
        {
            'id_zamowienia': 43,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Warszawa',
            'adres': "Alternatywy 4"
        },
        {
            'id_zamowienia': 44,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'dostarczone',
			'oplacone': True,
            'czas_dostawy': 12,
            'czas_realizacji': 17,
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Warszawa',
            'adres': "Alternatywy 4"
        },
        {
            'id_zamowienia': 45,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'dostarczone',
			'oplacone': True,
            'czas_dostawy': 52,
            'czas_realizacji': 17,
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Gdynia',
            'adres': "Alternatywy 4"
        },
        {
            'id_zamowienia': 46,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 26.88,
            'status': 'dostarczone',
			'oplacone': True,
            'czas_dostawy': 18,
            'czas_realizacji': 38,
            'data_zlozenia': '2018-09-10',
            'ocena': 2,
            'miasto': 'Warszawa',
            'adres': "Grunwaldzka 13"
        },
        {
            'id_zamowienia': 47,
            'id_klienta': 2,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 59.88,
            'status': 'dostarczone',
			'oplacone': True,
            'czas_dostawy': 42,
            'czas_realizacji': 18,
            'data_zlozenia': '2018-06-11',
            'ocena': 4,
            'miasto': 'Gdynia',
            'adres': "Wolności 15"

        },
        {
            'id_zamowienia': 48,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Radom',
            'adres': "Alternatywy 4"

        },
        {
            'id_zamowienia': 49,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Radom',
            'adres': "Alternatywy 4"

        },
        {
            'id_zamowienia': 50,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'dostarczone',
			'oplacone': True,
            'czas_dostawy': 72,
            'czas_realizacji': 45,
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Gdynia',
            'adres': "Alternatywy 4"

        },
        {
            'id_zamowienia': 51,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'dostarczone',
			'oplacone': True,
            'czas_dostawy': 28,
            'czas_realizacji': 24,
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Gdynia',
            'adres': "Alternatywy 4"

        },
        {
            'id_zamowienia': 52,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Gdynia',
            'adres': "Alternatywy 4"

        },
        {
            'id_zamowienia': 53,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Warszawa',
            'adres': "Alternatywy 4"
        },
        {
            'id_zamowienia': 54,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Warszawa',
            'adres': "Alternatywy 4"
        },
        {
            'id_zamowienia': 55,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Gdynia',
            'adres': "Alternatywy 4"
        },
        {
            'id_zamowienia': 56,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'dostarczone',
			'oplacone': True,
            'czas_dostawy': 25,
            'czas_realizacji': 75,
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Radom',
            'adres': "Alternatywy 4"
        },
        {
            'id_zamowienia': 57,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Gdynia',
            'adres': "Alternatywy 4"
        },
        {
            'id_zamowienia': 58,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Warszawa',
            'adres': "Alternatywy 4"
        },
        {
            'id_zamowienia': 59,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'dostarczone',
			'oplacone': True,
            'czas_dostawy': 24,
            'czas_realizacji': 18,
            'data_zlozenia': '2018-12-16',
            'ocena': None,
            'miasto': 'Warszawa',
            'adres': "Alternatywy 4"
        },
        {
            'id_zamowienia': 60,
            'id_klienta': 1,
            'id_restauracji': 1,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'kwota': 43.80,
            'status': 'anulowane',
            'data_zlozenia': '2018-12-16',
            'ocena': 8,
            'miasto': 'Gdynia',
            'adres': "Alternatywy 4"
        },
    ]
}
zamowienia_interator = 60


@app.route('/dodaj_zamowienie_Z', methods=['POST'])
def dodaj_zamowienie_Z():
    try:
        rrequest = request.get_json()
        if rrequest['id_klienta'] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        id_klienta = int(rrequest['id_klienta'])

        if rrequest['id_restauracji'] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        id_restauracji = int(rrequest['id_restauracji'])

        if rrequest['lista_dan'] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        lista_dan = rrequest['lista_dan']

        if rrequest['kwota'] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        kwota = float(rrequest['kwota'])

        if rrequest['miasto'] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        miasto = str(rrequest['miasto'])

        if rrequest['adres'] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        adres = str(rrequest['adres'])
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp

    global zamowienia_interator
    zamowienia_interator +=1
    lista_zamowien_Z['lista_zamowien'].append({
        'id_zamowienia': zamowienia_interator,
        'lista_dan': lista_dan,
        'id_restauracji': id_restauracji,
        'id_klienta': id_klienta,
        'kwota': kwota,
        'status': 'oczekujące',
        'oplacone': False,
        'adres': adres,
        'miasto': miasto,
        'data_zlozenia': str(datetime.datetime.today().strftime('%Y-%m-%d'))
    })
    print('DODANO ZAM')
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp


@app.route('/oplac_zamowienie_Z', methods=['POST'])
def oplac_zamowienie_Z():
    try:
        if request.args.get("id_zamowienia") is None:
            resp = jsonify(success=False)
            resp.status_code = 403
            return resp
        id_zamowienia = request.args.get("id_zamowienia")
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 500
        return resp

    for zamowienie in lista_zamowien_Z['lista_zamowien']:
        if zamowienie['id_zamowienia'] == int(id_zamowienia):
            zamowienie['oplacone'] = True
            resp = jsonify(success=True)
            resp.status_code = 200
            return resp

    resp = jsonify(success=False)
    resp.status_code = 404
    return resp

# Edytuj_zamowienie(id_zamowienia:int, lista[id_dania:int,nazwa:string],kwota:double)
@app.route('/edytuj_zamowienie_Z', methods=['POST'])
def edytuj_zamowienie_Z():
    rrequest = request.get_json()
    try:
        if rrequest["id_zamowienia"] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp

    try:
        if rrequest["lista_dan"]:
            for zamowienie in lista_zamowien_Z['lista_zamowien']:
                if zamowienie['id_zamowienia'] == int(rrequest['id_zamowienia']):
                    zamowienie['lista_dan'] = str(rrequest['lista_dan'])
    except KeyError:
        pass

    try:
        if rrequest["kwota"]:
            for zamowienie in lista_zamowien_Z['lista_zamowien']:
                if zamowienie['id_zamowienia'] == int(rrequest['id_zamowienia']):
                    zamowienie['cena'] = int(rrequest['cena'])
    except KeyError:
        pass

    try:
        if rrequest["adres"]:
            for zamowienie in lista_zamowien_Z['lista_zamowien']:
                if zamowienie['id_zamowienia'] == int(rrequest['id_zamowienia']):
                    zamowienie['adres'] = int(rrequest['adres'])
    except KeyError:
        pass

    try:
        if rrequest["miasto"]:
            for zamowienie in lista_zamowien_Z['lista_zamowien']:
                if zamowienie['id_zamowienia'] == int(rrequest['id_zamowienia']):
                    zamowienie['miasto'] = int(rrequest['miasto'])
    except KeyError:
        pass

    print(lista_zamowien_Z)
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp


# Zmien_status_zamowienia(id_zamowienia:int, status:string)
@app.route('/zmien_status_zamowienia_Z', methods=['POST'])
def zmien_status_zamowienia_Z():
    rrequest = request.get_json()
    try:
        if rrequest["id_zamowienia"] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        id_zamowienia = int(rrequest['id_zamowienia'])
        if rrequest['status'] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        status = str(rrequest['status'])
        for zamowienie in lista_zamowien_Z['lista_zamowien']:
            if zamowienie['id_zamowienia'] == id_zamowienia:
                zamowienie['status'] = str(status)
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp
    print(lista_zamowien_Z)
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp


# Pobierz zamówienia -> przekopiuj z realizacji
@app.route('/pobierz_zamowienia_Z', methods=['GET'])
def pobierz_zamowienia_Z():
    return jsonify(lista_zamowien_Z)


# Pobierz_zamowienie(id_zamowienia:int) zwraca (id_klienta:int, id_restauracji:int, lista[id_dania:int,nazwa:string],
#                                                                                    kwota:double,data_zlozenia:string,status:string,ocena:int)

@app.route('/pobierz_zamowienie_Z', methods=['GET'])
def pobierz_zamowienie_Z():
    try:
        if request.args.get("id_zamowienia") is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        id_zamowienia = int(request.args.get("id_zamowienia"))
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp
    return jsonify(lista_zamowien_Z['lista_zamowien'][id_zamowienia])


@app.route('/dodaj_ocene_Z', methods=['POST'])
def dodaj_ocene_Z():
    rrequest = request.get_json()
    try:
        if rrequest["id_zamowienia"] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        id_zamowienia = int(rrequest['id_zamowienia'])
        if rrequest['ocena'] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        ocena = str(rrequest['ocena'])
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp

    for zamowienie in lista_zamowien_Z['lista_zamowien']:
        if zamowienie['id_zamowienia'] == id_zamowienia:
            print(zamowienie)
            zamowienie.update({'ocena': str(ocena)})

    print(zamowienie)
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp


if __name__ == '__main__':
    app.run()
