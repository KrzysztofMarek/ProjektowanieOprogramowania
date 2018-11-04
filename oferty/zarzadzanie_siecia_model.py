from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

from oferty import oferty_model

app = Flask(__name__)
cors = CORS(app)


@app.route('/cities', methods=['GET'])
@cross_origin()
def pobierz_menu_sieci():
    cities = oferty_model.get_cities()
    return jsonify({"cities": cities})


@app.route('/cities/<city_id>', methods=['GET'])
@cross_origin()
def dodaj_danie(nazwa, cena, opis):
    return "City id is not int"


@app.route('/cities/<city_id>', methods=['GET'])
@cross_origin()
def modyfikuj_danie(danie_id, nazwa, cena, opis):
    return "City id is not int"


@app.route('/restaurant-offer/<restaurant_id>', methods=['GET'])
@cross_origin()
def usun_danie(danie_id):
    return "Restaurant id is not int"


if __name__ == "__main__":
    app.run(debug=True)
