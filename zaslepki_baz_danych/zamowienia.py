from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def main_site():
    return 404


@app.route('/dodaj_zamowienie', methods=['POST'])
def dodaj_zamowienie():
    if request.form['id_klienta'] is None:
        return 404
    id_klienta = int(request.form['id_klienta'])

    if request.form['id_restauracji'] is None:
        return 404
    id_restauracji = int(request.form['id_restauracji'])

    if request.form['lista_dan'] is None:
        return 404
    lista_dan = request.form['lista_dan']

    if request.form['kwota'] is None:
        return 404
    kwota = float(request.form['kwota'])

    resp = jsonify(success=True)
    resp.status_code = 200
    return resp


if __name__ == '__main__':
    app.run()
