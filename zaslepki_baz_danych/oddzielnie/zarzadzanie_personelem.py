from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def main_site():
    return 404


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


# TODO
@app.route('/usun_pracownika', methods=['POST'])
def usun_pracownika():
    if request['id_pracownika'] is None:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp
    id_pracownika = int(request['id_pracownika'])
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp


# TODO
@app.route('/pobierz_pracownikow', methods=['GET'])
def pobierz_pracownikow():
    lista_pracownikow = [[1, "Jan", "Kek", "123456789", "Kucharz", "JanKe"],
                         [2, "Piotr", "Ptak", "123456789", "Menadzer", "Duzy_Ptak12"],
                         [3, "Adrian", "Hasz", "123456789", "Kucharz", "haszImasz"]]

    if request["id_restauracji"] is None:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp
    id_restauracji = int(request["id_restauracji"])

    return jsonify(lista_pracownikow)


if __name__ == '__main__':
    app.run()
