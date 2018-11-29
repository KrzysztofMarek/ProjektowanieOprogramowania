from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)


@app.route('/')
def main_site():
    return 404


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
zamowienia_interator = 4


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
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp

    global zamowienia_interator
    zamowienia_interator +=1
    lista_zamowien['lista_zamowien'].append({
        'id_zamowienia': zamowienia_interator,
        'lista_dan': lista_dan,
        'id_restauracji': id_restauracji,
        'id_klienta': id_klienta,
        'kwota': kwota,
        'status': 'oczekujace',
        'data_zlozenia': str(datetime.datetime.today().strftime('%Y-%m-%d'))
    })
    print(lista_zamowien)
    resp = jsonify(success=True)
    resp.status_code = 200
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
            for zamowienie in lista_zamowien['lista_zamowien']:
                if zamowienie['id_zamowienia'] == int(rrequest['id_zamowienia']):
                    zamowienie['lista_dan'] = str(rrequest['lista_dan'])
    except KeyError:
        pass

    try:
        if rrequest["kwota"]:
            for zamowienie in lista_zamowien['lista_zamowien']:
                if zamowienie['id_zamowienia'] == int(rrequest['id_zamowienia']):
                    zamowienie['cena'] = int(rrequest['cena'])
    except KeyError:
        pass

    print(lista_zamowien)
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
        for zamowienie in lista_zamowien['lista_zamowien']:
            if zamowienie['id_zamowienia'] == id_zamowienia:
                zamowienie['status'] = str(status)
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp
    print(lista_zamowien)
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp


<<<<<<< HEAD
# Pobierz zamowienia -> przekopiuj z realizacji
@app.route('/pobierz_zamowienia', methods=['GET'])
def pobierz_zamowienia():
    rrequest = request.get_json()
=======
# Pobierz zamówienia -> przekopiuj z realizacji
@app.route('/pobierz_zamowienia_Z', methods=['GET'])
def pobierz_zamowienia_Z():
>>>>>>> master
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


# Czy to ma sens? : Pobierz_zamowienie(id_zamowienia:int) zwraca (id_klienta:int, id_restauracji:int, lista[id_dania:int,nazwa:string],
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
    return jsonify(lista_zamowien['lista_zamowien'][id_zamowienia])


if __name__ == '__main__':
    app.run()
