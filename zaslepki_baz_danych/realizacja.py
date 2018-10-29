from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


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

    return 200


@app.route('/pobierz_zamowienia', methods=['GET'])
def pobierz_zamowienia():
    lista_zamowien = [[1, "Ciastko"],
                      [2, "Kawa"],
                      [3, "Bulka"]]

    if request.args.get("id_restauracji") is None:
        return 404
    id_restauracji = int(request.args.get("id_restauracji"))

    tmp = [[1, lista_zamowien, "Gotowe"], [2, lista_zamowien, "Oczekujace"],
           [3, lista_zamowien, "Anulowane"]]
    return jsonify(tmp)


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