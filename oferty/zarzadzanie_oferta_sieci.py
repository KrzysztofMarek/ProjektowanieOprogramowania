
import requests

from flask import Blueprint, jsonify
from flask_cors import cross_origin


from oferty import zarzadzanie_siecia_model as model_zs


zarzadzanie_oferta_sieci = Blueprint('zarzadzanie_oferta_sieci', __name__)


@zarzadzanie_oferta_sieci.route('/pobierz_menu_sieci', methods=['GET'])
@cross_origin()
def pobierz_menu_sieci():
    menu_sieci = model_zs.pobierz_menu_sieci()
    return jsonify(menu_sieci)

