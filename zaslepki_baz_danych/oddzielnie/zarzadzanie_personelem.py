from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def main_site():
    return 404


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


if __name__ == '__main__':
    app.run()
