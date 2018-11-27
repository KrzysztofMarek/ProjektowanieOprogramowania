from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def main_site():
    return 404


# Pobierz_pracownika(id_pracownika: string) zwraca string:login, string:hasło oraz string:stanowisko
@app.route('/pobierz_pracownika', methods=['GET'])
def pobierz_pracownika():
    try:
        if request.args.get("id_pracownika") is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        id_pracownika = str(request.args.get("id_pracownika"))
    except KeyError:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp

    employee_list = {
        'lista': [
            {
                'login': 'jusepe',
                'hasło': 'wodjfoph35vg',
                'stanowisko': 'Pracownik kuchni'

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
    for pracownik in employee_list['lista']:
        if pracownik['login'] == id_pracownika:
            return jsonify(pracownik)

    resp = jsonify(success=False)
    resp.status_code = 404
    return resp


# Pobierz_klienta(id_klienta:string) zwraca string:login, string:hasło
@app.route('/pobierz_klienta', methods=['GET'])
def pobierz_klienta():
    try:
        if request.args.get("id_klienta") is None:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        id_klienta = str(request.args.get("id_klienta"))
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
    for klient in client_list['lista']:
        if klient['login'] == id_klienta:
            return jsonify(klient)

    resp = jsonify(success=False)
    resp.status_code = 404
    return resp


if __name__ == '__main__':
    app.run()
