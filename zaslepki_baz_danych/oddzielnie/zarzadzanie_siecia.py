from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def main_site():
    return 404


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
            'id_restauracji': restauracje_iterator ,
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
# ah jo
