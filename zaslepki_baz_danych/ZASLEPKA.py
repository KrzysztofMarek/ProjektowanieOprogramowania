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

    rrequest = request.get_json()
    print(rrequest)
    try:
        if rrequest["id_restauracji"] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        id_restauracji = int(rrequest["id_restauracji"])
        if id_restauracji == 0:
            return jsonify(network_menu)
        else:
            return jsonify(restaurant_menu)
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp


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
    try:
        if request.args.get("id_restauracji") is None:
            return 404
        miasto = int(request.args.get("miasto"))
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp
    return jsonify(restaurant_list)


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
    rrequest = request.get_json()
    try:
        if rrequest["id_restauracji"] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        id_restauracji = int(rrequest["id_restauracji"])
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp
    return jsonify(lista_zamowien)


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


@app.route('/dodaj_zamowienie', methods=['POST'])
def dodaj_zamowienie():
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
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp

    resp = jsonify(success=True)
    resp.status_code = 200
    return resp


@app.route('/dodaj_pracownika', methods=['POST'])
def dodaj_pracownika():
    try:
        rrequest = request.get_json()
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

        if rrequest['login'] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        login = str(rrequest['login'])

        if rrequest['haslo'] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        haslo = str(rrequest['haslo'])
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp

    resp = jsonify(success=True)
    resp.status_code = 200
    return resp


if __name__ == '__main__':
    app.run()
