from flask import Blueprint, jsonify, request
from flask_cors import cross_origin

import oferty_model

oferta = Blueprint('oferta', __name__)


@oferta.route('/pobierz_miasta', methods=['GET'])
@cross_origin()
def pobierz_miasta():
    cities = oferty_model.get_cities()
    return jsonify(cities)


@oferta.route('/pobierz_restauracje_z_miasta', methods=['GET'])
@cross_origin()
def pobierz_restauracje():
    if request.args.get("miasto") is None:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp
    id_restauracji = request.args.get("miasto")
    menu_restauracji = oferty_model.pobierz_restauracje(id_restauracji)
    return jsonify(menu_restauracji)


@oferta.route('/pobierz_menu_restauracji', methods=['GET'])
@cross_origin()
def pobierz_oferte():
    if request.args.get("id_restauracji") is None:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp
    id_restauracji = int(request.args.get("id_restauracji"))
    menu_restauracji = oferty_model.pobierz_menu_restauracji(id_restauracji)
    return jsonify(menu_restauracji)

