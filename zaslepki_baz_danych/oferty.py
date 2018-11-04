from flask import Flask, request, jsonify

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


if __name__ == '__main__':
    app.run()
