from flask import Flask, jsonify, request
app = Flask(__name__)

import oferty_db_mock


@app.route('/cities', methods=['GET'])
def get_cities():
    cities = oferty_db_mock.get_cities()
    return jsonify({"cities": cities})


@app.route('/cities/offer', methods=['GET'])
def get_offer():
    city_id = request.form["city"]
    if city_id:
        return jsonify({"offers": oferty_db_mock.get_restaurants_from_city(city_id)})


@app.route('/cities/offer/restaurant', methods=['GET'])
def get_restaurants():
    restaurant_id = request.form["restaurant_id"]
    if restaurant_id:
        return jsonify({"menu": oferty_db_mock.get_restaurant_menu(restaurant_id)})


if __name__ == "__main__":
    app.run(debug=True)