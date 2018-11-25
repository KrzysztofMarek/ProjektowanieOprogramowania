from flask import Flask, request, jsonify

app = Flask(__name__)


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


@app.route('/')
def main_site():
    return 404


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


lista_zamowien_z_kontaktem = {
        'lista_zamowien': [
            {
                'id_zamowienia': 1,
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
                'kontakt': {'imie': 'Andrzej', 'nazwisko': 'Adrianowski', 'telefon': '123456789', 'adres': 'Cicha 3'}

            }
        ]
    }


@app.route('/pobierz_zamowienia_z_kontaktem', methods=['GET'])
def pobierz_zamowienia_z_kontaktem():
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
    return jsonify(lista_zamowien_z_kontaktem)


if __name__ == '__main__':
    app.run()
