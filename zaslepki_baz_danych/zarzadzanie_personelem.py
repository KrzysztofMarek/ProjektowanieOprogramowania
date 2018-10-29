from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def main_site():
    return 404


@app.route('/dodaj_pracownika', methods=['POST'])
def dodaj_pracownika():
    if request.form['id_restauracji'] is None:
        return 404
    id_restauracji = int(request.form['id_restauracji'])

    if request.form['imie'] is None:
        return 404
    imie = str(request.form['imie'])

    if request.form['nazwisko'] is None:
        return 404
    nazwisko = str(request.form['nazwisko'])

    if request.form['telefon'] is None:
        return 404
    telefon = str(request.form['telefon'])

    if request.form['stanowisko'] is None:
        return 404
    stanowisko = str(request.form['stanowisko'])

    if request.form['login'] is None:
        return 404
    login = str(request.form['login'])

    if request.form['haslo'] is None:
        return 404
    haslo = str(request.form['haslo'])

    return 200


@app.route('/usun_pracownika', methods=['POST'])
def usun_pracownika():
    if request.form['id_pracownika'] is None:
        return 404
    id_pracownika = int(request.form['id_pracownika'])
    return 200


@app.route('/pobierz_pracownikow', methods=['GET'])
def pobierz_pracownikow():
    lista_pracownikow = [[1, "Jan", "Kek", "123456789", "Kucharz", "JanKe"],
                         [2, "Piotr", "Ptak", "123456789", "Menadzer", "Duzy_Ptak12"],
                         [3, "Adrian", "Hasz", "123456789", "Kucharz", "haszImasz"]]

    if request.args.get("id_restauracji") is None:
        return 404
    id_restauracji = int(request.args.get("id_restauracji"))

    return jsonify(lista_pracownikow)



if __name__ == '__main__':
    app.run()
