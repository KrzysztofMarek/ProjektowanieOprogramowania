from flask import Flask, request, jsonify

app = Flask(__name__)


lista_zamowien = {
        'lista_zamowien': [
            {
                'id_zamowienia': 1,
                'lista_dan': [
                    {'id_dania': 1, 'nazwa': 'Kawa'},
                    {'id_dania': 2, 'nazwa': 'Ciastko'},
                    {'id_dania': 3, 'nazwa': 'Bulka'}
                ],
                'status': 'oczekujace',
            },
            {
                'id_zamowienia': 2,
                'lista_dan': [
                    {'id_dania': 1, 'nazwa': 'Kawa'},
                    {'id_dania': 2, 'nazwa': 'Ciastko'},
                    {'id_dania': 3, 'nazwa': 'Bulka'}
                ],
                'status': 'przygotowywane',

            },
            {
                'id_zamowienia': 3,
                'lista_dan': [
                    {'id_dania': 1, 'nazwa': 'Kawa'},
                    {'id_dania': 2, 'nazwa': 'Ciastko'},
                    {'id_dania': 3, 'nazwa': 'Bulka'}
                ],
                'status': 'w_drodze',

            }
        ]
    }


@app.route('/')
def main_site():
    return 404


@app.route('/zmien_status_zamowienia', methods=['POST'])
def zmien_status_zamowienia():
    if request.form['id_zamowienia'] is None:
        return 404
    id_zamowienia = int(request.form['id_zamowienia'])
    if request.form['status'] is None:
        return 404
    status = str(request.form['status'])
    for zamowienie in lista_zamowien['lista_zamowien']:
        if zamowienie['id_zamowienia'] == id_zamowienia:
            zamowienie['status'] = str(status)

    resp = jsonify(success=True)
    resp.status_code = 200
    return resp


@app.route('/pobierz_zamowienia', methods=['GET'])
def pobierz_zamowienia():
    if request.args.get("id_restauracji") is None:
        return 404
    id_restauracji = int(request.args.get("id_restauracji"))
    return jsonify(lista_zamowien)


#TODO
@app.route('/pobierz_kontakt', methods=['GET'])
def pobierz_kontakt():
    lista_zamowien = [[1, "Ciastko"],
                      [2, "Kawa"],
                      [3, "Bułka"]]

    if request.args.get("id_zamowienia") is None:
        return 404
    id_restauracji = int(request.args.get("id_zamowienia"))

    tmp = ["Jan", "Nowak", "123456789", "Bulimiii 15"]
    return jsonify(tmp)


if __name__ == '__main__':
    app.run()
