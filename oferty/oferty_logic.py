from flask import Blueprint, jsonify, request
from flask_cors import cross_origin

from oferty import oferty_model

oferta = Blueprint('oferta', __name__)


@oferta.route('/pobierz_miasta', methods=['GET'])
@cross_origin()
def pobierz_miasta():
    cities = oferty_model.get_cities()
    return jsonify({"cities": cities})


@oferta.route('/cities/<city_id>', methods=['GET'])
@cross_origin()
def pobierz_restauracje():
    if request.args.get("id_restauracji") is None:
        return 404
    id_restauracji = int(request.args.get("id_restauracji"))
    menu_restauracji = oferty_model.pobierz_menu_restauracji(id_restauracji)
    return jsonify(menu_restauracji)


@oferta.route('/restaurant-offer/<restaurant_id>', methods=['GET'])
@cross_origin()
def pobierz_oferte():
    if request.args.get("id_restauracji") is None:
        return 404
    id_restauracji = int(request.args.get("id_restauracji"))
    menu_restauracji = oferty_model.pobierz_restauracje(id_restauracji)
    return jsonify(menu_restauracji)

