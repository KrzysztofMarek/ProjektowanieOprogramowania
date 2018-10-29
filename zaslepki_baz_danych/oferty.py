from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route('/')
def main_site():
    return 404


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
    restaurant_menu= {
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
        #response = app.response_class(
        #response=json.dumps(network_menu),
        #status=200,
        #mimetype='application/json')
        #return response
    else:
        return jsonify(restaurant_menu)


@app.route('/dodaj_danie', methods=['POST'])
def dodaj_danie():
    if request.form['id_restauracji'] is None:
        return 404
    id_restauracji = int(request.form['id_restauracji'])

    if request.form['id_dania'] is None:
        return 404
    id_dania = int(request.form['id_dania'])

    if request.form['nazwa'] is None:
        return 404
    nazwa = str(request.form['nazwa'])

    if request.form['cena'] is None:
        return 404
    cena = float(request.form['cena'])

    if request.form['opis'] is None:
        return 404
    opis = str(request.form['opis'])

    return 200


@app.route('/modyfikuj_danie', methods=['POST'])
def modyfikuj_danie():
    if request.form['id_restauracji'] is None:
        return 404
    id_restauracji = int(request.form['id_restauracji'])

    if request.form['id_dania'] is None:
        return 404
    id_dania = int(request.form['id_dania'])

    if request.form['nazwa'] is None:
        return 404
    nazwa = str(request.form['nazwa'])

    if request.form['cena'] is None:
        return 404
    cena = float(request.form['cena'])

    if request.form['opis'] is None:
        return 404
    opis = str(request.form['opis'])

    return 200


@app.route('/usun_danie', methods=['POST'])
def usun_danie():
    if request.form['id_dania'] is None:
        return 404
    id_dania = int(request.form['id_dania'])
    return 200


if __name__ == '__main__':
    app.run()
