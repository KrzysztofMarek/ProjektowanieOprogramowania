from flask import Blueprint, request, jsonify
from flask_cors import cross_origin

from oferty.zarzadzanie_restauracja_model import pobierz_menu_restauracji as pobierz_mr

zarzadzanie_oferta_restauracji = Blueprint('zarzadzanie_oferta_restauracji', __name__)


@zarzadzanie_oferta_restauracji.route('/pobierz_menu_restauracji', methods=['GET'])
@cross_origin()
def pobierz_menu_restauracji():
    print(request.args.get('id_restauracji'))
    if request.args.get("id_restauracji") is None:
        return 404
    id_restauracji = int(request.args.get("id_restauracji"))
    menu_restauarcji = pobierz_mr(id_restauracji)
    return jsonify(menu_restauarcji)

