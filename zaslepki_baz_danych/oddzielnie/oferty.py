from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def main_site():
    return 404


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

restaurant_menu_1 = {
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


restaurant_menu_2 = {
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
                'id_dania': 4,
                'nazwa': 'Chleb',
                'cena': 0.99,
                'opis': 'Dobry chlebek'
            }
        ]
    }

id_dania_iterator = 4

@app.route('/pobierz_menu_restauracji', methods=['GET'])
def pobierz_menu_restauracji():
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
    rrequest = request.get_json()
    try:
        if rrequest["miasto"] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        miasto = int(request["miasto"])
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
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp
    id_restauracji = rrequest['id_restauracji']
    id_dania_iterator =+ 1
    if id_restauracji == 1:
        restaurant_menu_1['lista'].append({
                'id_dania': id_dania_iterator,
                'nazwa': 'Ciastko',
                'cena': 29.99,
                'opis': 'Pycha ciacho'

            })
    elif id_restauracji == 2:
        restaurant_menu_2['lista'].append({
                'id_dania': id_dania_iterator,
                'nazwa': 'Ciastko',
                'cena': 29.99,
                'opis': 'Pycha ciacho'

            })
    else:
        resp = jsonify('nie ma takiej restuaracji')
        resp.status_code = 404
        return resp


# Usun_danie(id_dania:int) <- usuwa danie z oferty sieci
@app.route('/usun_danie', methods=['POST'])
def usun_danie():
    rrequest = request.get_json()
    try:
        if rrequest["id_dania"] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp
    id_dania = rrequest['id_dania']
    if id_dania == 1:
        network_menu['lista'].pop(0)
    else:
        network_menu['lista'].pop(1)


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
    id_restauracji = rrequest['id_restauracji']
    if id_restauracji != 1 or id_restauracji != 2:
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
    id_dania = rrequest['id_dania']


    try:
        if rrequest["nazwa"]:
            if id_restauracji == 1 :
                for danie in restaurant_menu_1['lista']:
                    if danie['id_dania'] == id_dania:
                        danie['nazwa'] = str(rrequest['nazwa'])
            else:
                for danie in restaurant_menu_2['lista']:
                    if danie['id_dania'] == id_dania:
                        danie['nazwa'] = str(rrequest['nazwa'])
    except KeyError:
        pass

    try:
        if rrequest["cena"]:
                for danie in restaurant_menu_1['lista']:
                    if danie['id_dania'] == id_dania:
                        danie['cena'] = int(rrequest['cena'])
        else:
            for danie in restaurant_menu_2['lista']:
                if danie['id_dania'] == id_dania:
                    danie['cena'] = int(rrequest['cena'])
    except KeyError:
        pass

    try:
        if rrequest["opis"]:
            for danie in restaurant_menu_1['lista']:
                if danie['id_dania'] == id_dania:
                    danie['opis'] = str(rrequest['opis'])
        else:
            for danie in restaurant_menu_2['lista']:
                if danie['id_dania'] == id_dania:
                    danie['opis'] = str(rrequest['opis'])
    except KeyError:
        pass

    resp = jsonify(success=True)
    resp.status_code = 200
    return resp


if __name__ == '__main__':
    app.run()
