# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)


@app.route('/')
def main_site():
    return 404


klienci = {'lista': [
    {
        'id_klienta': 'heheszek',
        'imie': 'Jan',
        'nazwisko': 'Kowalski',
        'telefon': '333444555',
        'haslo': 'wdjfh',
        'email': 'jan@jan.pl',
        'adres': 'Konwaliowa 3',
        'punkty': 3
    },
    {
        'id_klienta': 'silacz',
        'imie': 'Arnold',
        'nazwisko': 'Czarny',
        'telefon': '333444555',
        'haslo': 'wdjfh',
        'email': 'get@tothe.chopper',
        'adres': 'Terminowa 2',
        'punkty': 0
    },
    {
        'id_klienta': 'SyLweK',
        'imie': 'Sykwester',
        'nazwisko': 'Stalowy',
        'telefon': '333444555',
        'haslo': 'wdjfh',
        'email': 'ramob@bumbum.rpg',
        'adres': 'Wybuchowa 4',
        'punkty': 16
    }
]}


@app.route('/pobierz_klientow', methods=['GET'])
def pobierz_klientow():
    return jsonify(klienci)


@app.route('/dodaj_punkty', methods=['POST'])
def dodaj_punkty():
    try:
        rrequest = request.get_json()
        if rrequest['id_klienta'] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        id_klienta = rrequest['id_klienta']

        if rrequest['punkty'] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        punkty = int(rrequest['punkty'])
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp

    for klient in klienci['lista']:
        if klient['id_klienta'] == id_klienta:
            klient['punkty'] += punkty

    print(klienci)
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp


@app.route('/pobierz_punkty_klienta', methods=['GET'])
def pobierz_punkty_klienta():
    try:
        if request.args.get("id_klienta") is None:
            resp = jsonify(success=False)
            resp.status_code = 403
            return resp
        id_klienta = request.args.get("id_klienta")
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 500
        return resp

    for klient in klienci['lista']:
        if klient['id_klienta'] == id_klienta:
            resp = jsonify(int(klient['punkty']))
            resp.status_code = 200
            return resp

    resp = jsonify(success=False)
    resp.status_code = 404
    return resp


@app.route('/usun_punkty', methods=['POST'])
def usun_punkty():
    try:
        rrequest = request.get_json()
        if rrequest['id_klienta'] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        id_klienta = rrequest['id_klienta']

        if rrequest['punkty'] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        punkty = int(rrequest['punkty'])
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp

    for klient in klienci['lista']:
        if klient['id_klienta'] == id_klienta:
            klient['punkty'] -= punkty

    print(klienci)
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp


# Pobierz_pracownika(id_pracownika: string) zwraca string:login, string:hasło oraz string:stanowisko
@app.route('/pobierz_pracownika', methods=['GET'])
def pobierz_pracownika():
    try:
        if request.args.get("id_pracownika") is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        id_pracownika = str(request.args.get("id_pracownika"))
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp

    employee_list = {
        'lista': [
            {
                'login': 'jusepe',
                'hasło': 'wodjfoph35vg',
                'stanowisko': 'Pracownik kuchni'

            },
            {
                'login': 'jadeSzybko12',
                'hasło': 'epivrugoi',
                'stanowisko': 'Dostawca'
            },
            {
                'login': 'hania_87',
                'hasło': 'wr98cyeui',
                'stanowisko': 'Sprzątaczka'
            }
        ]
    }
    for pracownik in employee_list['lista']:
        if pracownik['login'] == id_pracownika:
            return jsonify(pracownik)

    resp = jsonify(success=False)
    resp.status_code = 404
    return resp


# Pobierz_klienta(id_klienta:string) zwraca string:login, string:hasło
@app.route('/pobierz_klienta', methods=['GET'])
def pobierz_klienta():
    try:
        if request.args.get("id_klienta") is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        id_klienta = str(request.args.get("id_klienta"))
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp

    client_list = {
        'lista': [
            {
                'login': 'hydroMen',
                'hasło': 'sdhvgo'

            },
            {
                'login': 'Grunwald44',
                'hasło': 'spwwocihpf'
            },
            {
                'login': 'rysio99',
                'hasło': 'tesy54pipoyr'
            }
        ]
    }
    for klient in client_list['lista']:
        if klient['login'] == id_klienta:
            return jsonify(klient)

    resp = jsonify(success=False)
    resp.status_code = 404
    return resp


network_menu = {
    'lista': [
        {
            'id_dania': 1,
            'nazwa': 'Ciastko',
            'cena': 29.99,
            'opis': 'Pycha ciacho',
            'typ': 'menu_sieci'

        },
        {
            'id_dania': 2,
            'nazwa': 'Kawa',
            'cena': 5.99,
            'opis': 'Dobra kawusia',
            'typ': 'menu_sieci'
        }
    ]
}

restaurant_menu_1 = {
    'lista': [
        {
            'id_dania': 1,
            'nazwa': 'Ciastko',
            'cena': 29.99,
            'opis': 'Pycha ciacho',
            'typ': 'menu_sieci'

        },
        {
            'id_dania': 2,
            'nazwa': 'Kawa',
            'cena': 5.99,
            'opis': 'Dobra kawusia',
            'typ': 'menu_sieci'
        },
        {
            'id_dania': 3,
            'nazwa': 'Bułka',
            'cena': 2.99,
            'opis': 'Duża buła',
            'typ': 'menu_rest'
        }
    ]
}

restaurant_menu_2 = {
    'lista': [
        {
            'id_dania': 1,
            'nazwa': 'Ciastko',
            'cena': 29.99,
            'opis': 'Pycha ciacho',
            'typ': 'menu_sieci'

        },
        {
            'id_dania': 2,
            'nazwa': 'Kawa',
            'cena': 5.99,
            'opis': 'Dobra kawusia',
            'typ': 'menu_sieci'
        },
        {
            'id_dania': 4,
            'nazwa': 'Chleb',
            'cena': 0.99,
            'opis': 'Dobry chlebek',
            'typ': 'menu_rest'
        }
    ]
}

id_dania_iterator = 4


@app.route('/pobierz_menu_restauracji', methods=['GET'])
def pobierz_menu_restauracji():
    try:
        if request.args.get("id_restauracji") is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        id_restauracji = int(request.args.get("id_restauracji"))
        if id_restauracji == 0:
            return jsonify(network_menu)
        elif id_restauracji == 1:
            return jsonify(restaurant_menu_1)
        elif id_restauracji == 2:
            return jsonify(restaurant_menu_2)
        else:
            resp = jsonify('nie ma takiej restuaracji')
            resp.status_code = 404
            return resp
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp


# Pobierz_restauracje(miasto:string) zwraca (lista[id_restauracji:int, nazwa:string, adres:string])
@app.route('/pobierz_restauracje_z_miasta', methods=['GET'])
def pobierz_resturacje_z_miasta():
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
    try:
        if request.args.get("miasto") is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        miasto = str(request.args.get("miasto"))
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp
    return jsonify(restaurant_list)


# Pobierz_miasta() zwraca (lista[miasto:string])
@app.route('/pobierz_miasta', methods=['GET'])
def pobierz_miasta():
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
    return jsonify(cities_list)


# Dodaj_danie(id_restauracji:int, nazwa:string,cena:double,opis:string)
@app.route('/dodaj_danie', methods=['POST'])
def dodaj_danie():
    rrequest = request.get_json()
    try:
        if rrequest["id_restauracji"] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        id_restauracji = rrequest["id_restauracji"]
        if rrequest["nazwa"] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        nazwa = rrequest["nazwa"]
        if rrequest["opis"] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        opis = rrequest["opis"]
        if rrequest["cena"] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        cena = rrequest["cena"]
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp
    global id_dania_iterator
    id_dania_iterator += 1
    if id_restauracji == 1:
        restaurant_menu_1['lista'].append({
            'id_dania': id_dania_iterator,
            'nazwa': nazwa,
            'cena': cena,
            'opis': opis,
            'typ': 'menu_rest'

        })
        print(restaurant_menu_1)
    elif id_restauracji == 2:
        restaurant_menu_2['lista'].append({
            'id_dania': id_dania_iterator,
            'nazwa': nazwa,
            'cena': cena,
            'opis': opis,
            'typ': 'menu_rest'

        })
        print(restaurant_menu_2)
    elif id_restauracji == 0:
        network_menu['lista'].append({
            'id_dania': id_dania_iterator,
            'nazwa': nazwa,
            'cena': cena,
            'opis': opis,
            'typ': 'menu_sieci'

        })
        restaurant_menu_1['lista'].append({
            'id_dania': id_dania_iterator,
            'nazwa': nazwa,
            'cena': cena,
            'opis': opis,
            'typ': 'menu_sieci'

        })
        restaurant_menu_2['lista'].append({
            'id_dania': id_dania_iterator,
            'nazwa': nazwa,
            'cena': cena,
            'opis': opis,
            'typ': 'menu_sieci'

        })
        print(network_menu)
    else:
        resp = jsonify('nie ma takiej restuaracji')
        resp.status_code = 404
        return resp

    resp = jsonify(success=True)
    resp.status_code = 200
    return resp


# Usun_danie(id_dania:int, id_restauracji:int) <- usuwa danie z oferty sieci lub restauracji
@app.route('/usun_danie', methods=['GET'])
def usun_danie():
    try:
        if request.args.get("id_dania") is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        if request.args.get("id_restauracji") is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp
    id_dania = int(request.args.get("id_dania"))
    id_restauracji = int(request.args.get("id_restauracji"))

    k = 0
    if id_restauracji == 0:
        for danie in network_menu['lista']:
            if danie['id_dania'] == id_dania:
                network_menu['lista'].pop(k)
            k += 1
        k = 0
        for danie in restaurant_menu_1['lista']:
            if danie['id_dania'] == id_dania:
                restaurant_menu_1['lista'].pop(k)
            k += 1
        k = 0
        for danie in restaurant_menu_2['lista']:
            if danie['id_dania'] == id_dania:
                restaurant_menu_2['lista'].pop(k)
            k += 1
    elif id_restauracji == 1:
        for danie in restaurant_menu_1['lista']:
            if danie['id_dania'] == id_dania:
                restaurant_menu_1['lista'].pop(k)
            k += 1
    else:
        for danie in restaurant_menu_2['lista']:
            if danie['id_dania'] == id_dania:
                restaurant_menu_2['lista'].pop(k)
            k += 1
    print(network_menu)
    print(restaurant_menu_1)
    print(restaurant_menu_2)
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp


# Modyfikuj_danie(id_dania:int, id_restauracji:int, nazwa:string, cena:double, opis:string)
@app.route('/modyfikuj_danie', methods=['POST'])
def modyfikuj_danie():
    rrequest = request.get_json()
    try:
        if rrequest["id_restauracji"] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp
    id_restauracji = int(rrequest['id_restauracji'])
    if id_restauracji != 0 and id_restauracji != 1 and id_restauracji != 2:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp
    try:
        if rrequest["id_dania"] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp
    id_dania = int(rrequest['id_dania'])
    try:
        if rrequest["nazwa"]:
            if id_restauracji == 1:
                for danie in restaurant_menu_1['lista']:
                    if danie['id_dania'] == id_dania:
                        danie['nazwa'] = str(rrequest['nazwa'])
            elif id_restauracji == 2:
                for danie in restaurant_menu_2['lista']:
                    if danie['id_dania'] == id_dania:
                        danie['nazwa'] = str(rrequest['nazwa'])
            else:
                for danie in network_menu['lista']:
                    if danie['id_dania'] == id_dania:
                        danie['nazwa'] = str(rrequest['nazwa'])
    except KeyError:
        pass

    try:
        if rrequest["cena"]:
            if id_restauracji == 1:
                for danie in restaurant_menu_1['lista']:
                    if danie['id_dania'] == id_dania:
                        danie['cena'] = float(rrequest['cena'])
            elif id_restauracji == 2:
                for danie in restaurant_menu_2['lista']:
                    if danie['id_dania'] == id_dania:
                        danie['cena'] = float(rrequest['cena'])
            else:
                for danie in network_menu['lista']:
                    if danie['id_dania'] == id_dania:
                        danie['cena'] = float(rrequest['cena'])
    except KeyError:
        pass

    try:
        if rrequest["opis"]:
            if id_restauracji == 1:
                for danie in restaurant_menu_1['lista']:
                    if danie['id_dania'] == id_dania:
                        danie['opis'] = str(rrequest['opis'])
            elif id_restauracji == 2:
                for danie in restaurant_menu_2['lista']:
                    if danie['id_dania'] == id_dania:
                        danie['opis'] = str(rrequest['opis'])
            else:
                for danie in network_menu['lista']:
                    if danie['id_dania'] == id_dania:
                        danie['opis'] = str(rrequest['opis'])
    except KeyError:
        pass

    try:
        if rrequest["typ"]:
            if id_restauracji == 1:
                for danie in restaurant_menu_1['lista']:
                    if danie['id_dania'] == id_dania:
                        danie['typ'] = str(rrequest['typ'])
            elif id_restauracji == 2:
                for danie in restaurant_menu_2['lista']:
                    if danie['id_dania'] == id_dania:
                        danie['typ'] = str(rrequest['typ'])
            else:
                for danie in network_menu['lista']:
                    if danie['id_dania'] == id_dania:
                        danie['typ'] = str(rrequest['typ'])
    except KeyError:
        pass

    print(network_menu)
    print(restaurant_menu_1)
    print(restaurant_menu_2)
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp


lista_zamowien = {
    'lista_zamowien': [
        {
            'id_zamowienia': 1,
            'id_restauracji': 1,
            'kwota': 23.99,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'status': 'oczekujace',
            'kontakt': {'imie': 'Jan', 'nazwisko': 'Kowalski', 'telefon': '123456789', 'adres': 'Konwaliowa 3'}
        },
        {
            'id_zamowienia': 2,
            'id_restauracji': 2,
            'kwota': 25.77,
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
            'id_restauracji': 3,
            'kwota': 30.57,
            'lista_dan': [
                {'id_dania': 1, 'nazwa': 'Kawa'},
                {'id_dania': 2, 'nazwa': 'Ciastko'},
                {'id_dania': 3, 'nazwa': 'Bulka'}
            ],
            'status': 'w_drodze',
            'kontakt': {'imie': 'Andrzej', 'nazwisko': 'Adrianowski', 'telefon': '123456789', 'adres': 'Cicha 3'}
        }
    ]
}


@app.route('/zmien_status_zamowienia', methods=['POST'])
def zmien_status_zamowienia():
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
        for zamowienie in lista_zamowien['lista_zamowien']:
            if zamowienie['id_zamowienia'] == id_zamowienia:
                zamowienie['status'] = str(status)
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp


@app.route('/pobierz_zamowienia', methods=['GET'])
def pobierz_zamowienia():
    try:
        if request.args.get("id_restauracji") is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        id_restauracji = int(request.args.get("id_restauracji"))
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp
    return jsonify(lista_zamowien)


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
    zamowienia_interator += 1
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
            'id_restauracji': 1,
            'imie': 'Kasia',
            'nazwisko': 'Nowak',
            'telefon': '333444555',
            'stanowisko': 'menadzer restauracji',
            'haslo': 'kKdPS'

        },
        {
            'id_pracownika': 'rahim',
            'id_restauracji': 2,
            'imie': 'Rahim',
            'nazwisko': 'bin Amdel',
            'telefon': '333444555',
            'stanowisko': 'menadzer restauracji',
            'haslo': 'wdjfh'

        },
        {
            'id_pracownika': 'gracia12',
            'id_restauracji': 3,
            'imie': 'Grażyna',
            'nazwisko': 'Nowak',
            'telefon': '333444555',
            'stanowisko': 'menadzer restauracji',
            'haslo': 'pjdp'

        },
        {
            'id_pracownika': 'lubDum',
            'id_restauracji': 4,
            'imie': 'Robert',
            'nazwisko': 'Kowalak',
            'telefon': '333444555',
            'stanowisko': 'menadzer restauracji',
            'haslo': 'alkdjflk'

        }
    ]
}


@app.route('/dodaj_pracownika', methods=['POST'])
def dodaj_pracownika():
    try:
        rrequest = request.get_json()
        if rrequest['id_pracownika'] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        id_pracownika = rrequest['id_pracownika']

        if rrequest['id_restauracji'] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        id_restauracji = int(rrequest['id_restauracji'])

        if rrequest['imie'] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        imie = str(rrequest['imie'])

        if rrequest['nazwisko'] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        nazwisko = str(rrequest['nazwisko'])

        if rrequest['telefon'] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        telefon = str(rrequest['telefon'])

        if rrequest['stanowisko'] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        stanowisko = str(rrequest['stanowisko'])

        if rrequest['haslo'] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        haslo = str(rrequest['haslo'])
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp

    lista_pracownikow['lista_pracownikow'].append({
        'id_pracownika': id_pracownika,
        'id_restauracji': id_restauracji,
        'imie': imie,
        'nazwisko': nazwisko,
        'telefon': telefon,
        'stanowisko': stanowisko,
        'haslo': haslo
    })

    print(lista_pracownikow)
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp


@app.route('/usun_pracownika', methods=['GET'])
def usun_pracownika():
    try:
        if request.args.get('id_pracownika') is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        id_pracownika = request.args.get('id_pracownika')
        k = 0
        for pracownik in lista_pracownikow['lista_pracownikow']:
            if pracownik['id_pracownika'] == id_pracownika:
                lista_pracownikow['lista_pracownikow'].pop(k)
            k += 1

        print(lista_pracownikow)
        resp = jsonify(success=True)
        resp.status_code = 200
        return resp
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp


@app.route('/pobierz_pracownikow', methods=['GET'])
def pobierz_pracownikow():
    return jsonify(lista_pracownikow)


@app.route('/przydziel_menadzera', methods=['POST'])
def przydziel_menadzera():
    try:
        rrequest = request.get_json()
        if rrequest['id_pracownika'] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        id_pracownika = rrequest['id_pracownika']

        if rrequest['id_restauracji'] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        id_restauracji = int(rrequest['id_restauracji'])

    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp

    for pracownik in lista_pracownikow['lista_pracownikow']:
        if pracownik['stanowisko'] != 'menadzer restauracji':
            resp = jsonify('Pracownik o id: ' + str(id_restauracji) + " nie jest menadzerem")
            resp.status_code = 404
            return resp
        if pracownik['id_pracownika'] == id_pracownika:
            pracownik['id_restauracji'] = id_restauracji

        resp = jsonify(success=True)
        resp.status_code = 200
        return resp


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
            'nazwa': 'Zew Mięsa',
            'id_restauracji': 4,
            'adres': 'Mięsna 35'
        },
        {
            'nazwa': 'Piwowo',
            'id_restauracji': 5,
            'adres': 'Browarna 46'
        }
    ]
}
restauracje_iterator = 3


# a) Dodaj_restauracje(nazwa:string,adres:string)
@app.route('/dodaj_restauracje', methods=['POST'])
def dodaj_restauracje():
    try:
        rrequest = request.get_json()
        if rrequest['nazwa'] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        nazwa = str(rrequest['nazwa'])

        if rrequest['adres'] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        adres = str(rrequest['adres'])

    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp

    global restauracje_iterator
    restauracje_iterator += 1
    lista_restauracji['lista_restauracji'].append({
        'nazwa': nazwa,
        'id_restauracji': restauracje_iterator,
        'adres': adres
    })
    print(lista_restauracji)
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp


# b) Usuń_restauracje(id_restauracji:int)
@app.route('/usun_restauracje', methods=['GET'])
def usun_restauracje():
    try:
        if request.args.get('id_restauracji') is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        id_restauracji = int(request.args.get('id_restauracji'))
        k = 0
        for restauracja in lista_restauracji['lista_restauracji']:
            if restauracja['id_restauracji'] == id_restauracji:
                lista_restauracji['lista_restauracji'].pop(k)
            k += 1

        print(lista_restauracji)
        resp = jsonify(success=True)
        resp.status_code = 200
        return resp
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp


# c) Pobierz_restauracje() zwraca (lista[id_restauracji:int,nazwa:string,adres:string)
@app.route('/pobierz_restauracje', methods=['GET'])
def pobierz_restauracje():
    return jsonify(lista_restauracji)


@app.route('/restauracja_istnieje', methods=['GET'])
def restauracja_istnieje():
    try:
        if request.args.get('id_restauracji') is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp
    id_restauracji = int(request.args.get('id_restauracji'))
    for restauracja in lista_restauracji['lista_restauracji']:
        if restauracja['id_restauracji'] == id_restauracji:
            resp = jsonify(success=True)
            resp.status_code = 200
            return resp

    resp = jsonify('Restauracja nie znaleziona')
    resp.status_code = 404
    return resp


if __name__ == '__main__':
    app.run()
