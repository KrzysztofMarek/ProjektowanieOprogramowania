from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)

import oferty_db_mock


@app.route('/cities', methods=['GET'])
@cross_origin()
def get_cities():
    cities = oferty_db_mock.get_cities()
    return jsonify({"cities": cities})


@app.route('/cities/<city_id>', methods=['GET'])
@cross_origin()
def get_restaurants(city_id):
    if isinstance(city_id, int):
        restaurants = oferty_db_mock.get_restaurants_from_city(city_id)
        return jsonify({"restaurants": restaurants})
    return "City id is not int"


@app.route('/restaurant-offer/<restaurant_id>', methods=['GET'])
@cross_origin()
def get_offer(restaurant_id):
    if isinstance(restaurant_id, int):
        menu = oferty_db_mock.get_restaurant_menu(restaurant_id)
        return jsonify({"menu": menu})
    return "Restaurant id is not int"


if __name__ == "__main__":
    app.run(debug=True)