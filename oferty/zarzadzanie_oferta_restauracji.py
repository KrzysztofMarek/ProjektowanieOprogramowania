import re
import requests
import string

from flask import Blueprint, request, jsonify
from flask_cors import cross_origin

from Constants import Constants
from zarzadzanie_restauracja_model import pobierz_menu_model_rest, dodaj_danie_dla_restauracji, modyfikuj_d, usun_d


zarzadzanie_oferta_restauracji = Blueprint('zarzadzanie_oferta_restauracji', __name__)


@zarzadzanie_oferta_restauracji.route('/pobierz_menu_restauracji', methods=['GET'])
@cross_origin()
def pobierz_menu_restauracji():
    if request.args.get("id_restauracji") is None:
        resp = jsonify(success=False)
        resp.status_code = 404
        return resp
    id_restauracji = int(request.args.get("id_restauracji"))
    menu_restauracji = pobierz_menu_model_rest(id_restauracji)
    return jsonify(menu_restauracji)


@zarzadzanie_oferta_restauracji.route('/dodaj_danie_restauracja', methods=['POST'])
@cross_origin()
def dodaj_danie():
    danie = request.json
    if waliduj_danie(danie):
        return dodaj_danie_dla_restauracji(danie)
    resp = jsonify(success=False)
    resp.status_code = 404
    return resp


@zarzadzanie_oferta_restauracji.route('/modyfikuj_danie', methods=['POST'] )
@cross_origin()
def modyfikuj_danie():
    danie = request.json
    print(danie)
    if waliduj_danie(danie):
        return modyfikuj_d(danie)
    resp = jsonify(success=False)
    resp.status_code = 404
    return resp

@zarzadzanie_oferta_restauracji.route('/usun_danie', methods=['GET'] )
@cross_origin()
def usun_danie():
    id_dania = int(request.args.get("id_dania"))
    id_restauracji = int(request.args.get("id_restauracji"))
    usun_d(id_dania, id_restauracji)
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp

def waliduj_danie(danie: dict):
    elementy_dania = ["nazwa", "cena", "opis", "id_restauracji"]
    for element in elementy_dania:
        if element not in danie:
            return False
    return waliduj_nazwe(danie['nazwa']) and waliduj_cene(danie['cena']) and waliduj_opis(danie['opis'])


def waliduj_nazwe(nazwa):
    if len(nazwa) > 30:
        return False
    if nazwa[0] not in string.ascii_uppercase:
        return False
    for letter in nazwa[1:]:
        if letter not in string.whitespace and letter not in string.ascii_lowercase and letter not in string.ascii_uppercase and letter != '-':
            return False
    return True


def waliduj_cene(cena):
    if ',' in cena:
        if re.search(r'^\d{1,3}\,?\d{1,2}?$', cena):
            return True
    elif 0 < len(cena) < 4:
        return True
    return False


def waliduj_opis(opis):
    for letter in Constants.NIEPOPRAWNE_ZNAKI:
        if letter in opis:
            return False
    return len(opis) < 300
