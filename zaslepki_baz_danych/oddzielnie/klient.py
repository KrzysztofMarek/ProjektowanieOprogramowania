from flask import Flask, request, jsonify

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


if __name__ == '__main__':
    app.run()
