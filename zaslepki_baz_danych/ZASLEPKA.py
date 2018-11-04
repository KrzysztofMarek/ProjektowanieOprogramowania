from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def main_site():
    return "Hello there"


@app.route('/pobierz_menu_restauracji', methods=['GET'])
def pobierz_menu_restauracji():
    network_menu = {
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

    if request.args.get("id_restauracji") is None:
        return 404
    id_restauracji = int(request.args.get("id_restauracji"))
    if id_restauracji == 0:
        return jsonify(network_menu)
    else:
        return jsonify(restaurant_menu)


# Pobierz_restauracje(miasto:string) zwraca (lista[id_restauracji:int, nazwa:string, adres:string])
@app.route('/pobierz_restauracje', methods=['GET'])
def pobierz_resturacje():
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
    if request.args.get("id_restauracji") is None:
        return 404
    miasto = int(request.args.get("miasto"))
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


lista_zamowien = {
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


@app.route('/zmien_status_zamowienia', methods=['POST'])
def zmien_status_zamowienia():
    if request.form['id_zamowienia'] is None:
        return 404
    id_zamowienia = int(request.form['id_zamowienia'])
    if request.form['status'] is None:
        return 404
    status = str(request.form['status'])
    for zamowienie in lista_zamowien['lista_zamowien']:
        if zamowienie['id_zamowienia'] == id_zamowienia:
            zamowienie['status'] = str(status)

    resp = jsonify(success=True)
    resp.status_code = 200
    return resp


@app.route('/pobierz_zamowienia', methods=['GET'])
def pobierz_zamowienia():
    if request.args.get("id_restauracji") is None:
        return 404
    id_restauracji = int(request.args.get("id_restauracji"))
    return jsonify(lista_zamowien)


@app.route('/dodaj_zamowienie', methods=['POST'])
def dodaj_zamowienie():
    if request.form['id_klienta'] is None:
        return 404
    id_klienta = int(request.form['id_klienta'])

    if request.form['id_restauracji'] is None:
        return 404
    id_restauracji = int(request.form['id_restauracji'])

    if request.form['lista_dan'] is None:
        return 404
    lista_dan = request.form['lista_dan']

    if request.form['kwota'] is None:
        return 404
    kwota = float(request.form['kwota'])

    resp = jsonify(success=True)
    resp.status_code = 200
    return resp


@app.route('/dodaj_pracownika', methods=['POST'])
def dodaj_pracownika():
    if request.form['id_restauracji'] is None:
        return 404
    id_restauracji = int(request.form['id_restauracji'])

    if request.form['imie'] is None:
        return 404
    imie = str(request.form['imie'])

    if request.form['nazwisko'] is None:
        return 404
    nazwisko = str(request.form['nazwisko'])

    if request.form['telefon'] is None:
        return 404
    telefon = str(request.form['telefon'])

    if request.form['stanowisko'] is None:
        return 404
    stanowisko = str(request.form['stanowisko'])

    if request.form['login'] is None:
        return 404
    login = str(request.form['login'])

    if request.form['haslo'] is None:
        return 404
    haslo = str(request.form['haslo'])

    resp = jsonify(success=True)
    resp.status_code = 200
    return resp


if __name__ == '__main__':
    app.run()
