from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def main_site():
    return 404


# Pobierz_pracownika(id_pracownika: string) zwraca string:login, string:hasło oraz string:stanowisko
@app.route('/pobierz_pracownika', methods=['GET'])
def pobierz_pracownika():
    rrequest = request.get_json()
    try:
        if rrequest["id_pracownika"] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        id_pracownika = int(request["id_pracownika"])
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp

    employee_list = {
        'lista': [
            {
                'login': 'jusepe',
                'hasło': 'wodjfoph35vg',
                'stanowisko': 'Kucharz'

            },
            {
                'login': 'jadeSzybko12',
                'hasło': 'epivrugoi',
                'stanowisko': 'Dostawca'
            },
            {
                'login': 'hania_87',
                'hasło': 'wr98cyeui',
                'stanowisko': 'Sprzątaczka'
            }
        ]
    }
    if id_pracownika == 0:
        return jsonify(employee_list['lista'][0])
    elif id_pracownika == 1:
        return jsonify(employee_list['lista'][1])
    else:
        return jsonify(employee_list['lista'][2])


# Pobierz_klienta(id_klienta:string) zwraca string:login, string:hasło
@app.route('/pobierz_klienta', methods=['GET'])
def pobierz_pracownika():
    rrequest = request.get_json()
    try:
        if rrequest["id_klienta"] is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        id_klienta = int(request["id_klienta"])
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp

    client_list = {
        'lista': [
            {
                'login': 'hydroMen',
                'hasło': 'sdhvgo'

            },
            {
                'login': 'Grunwald44',
                'hasło': 'spwwocihpf'
            },
            {
                'login': 'rysio99',
                'hasło': 'tesy54pipoyr'
            }
        ]
    }
    if id_klienta == 0:
        return jsonify(client_list['lista'][0])
    elif id_klienta == 1:
        return jsonify(client_list['lista'][1])
    else:
        return jsonify(client_list['lista'][2])


if __name__ == '__main__':
    app.run()
