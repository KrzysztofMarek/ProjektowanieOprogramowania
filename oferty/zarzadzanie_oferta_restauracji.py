import re
import requests
import string

from flask import Blueprint, request, jsonify
from flask_cors import cross_origin

from oferty.Constants import Constants
from oferty.zarzadzanie_restauracja_model import pobierz_menu_restauracji, dodaj_danie_dla_restauracji


zarzadzanie_oferta_restauracji = Blueprint('zarzadzanie_oferta_restauracji', __name__)


@zarzadzanie_oferta_restauracji.route('/pobierz_menu_restauracji', methods=['GET'])
@cross_origin()
def pobierz_menu_restauracji():
    if request.args.get("id_restauracji") is None:
        return 404
    id_restauracji = int(request.args.get("id_restauracji"))
    menu_restauarcji = pobierz_menu_restauracji(id_restauracji)
    return jsonify(menu_restauarcji)


@zarzadzanie_oferta_restauracji.route('/dodaj_danie_restauracja', methods=['POST'])
@cross_origin()
def dodaj_danie():
    danie = request.json()
    if waliduj_danie(danie):
        dodaj_danie_dla_restauracji(danie)
    return "Danie nie jest poprawne. Sprawdz wszystkie pola"


def waliduj_danie(danie: dict):
    elementy_dania = ["nazwa", "cena", "opis", "id_restauracji"]
    for element in elementy_dania:
        if element not in elementy_dania:
            return False
    return waliduj_nazwe(danie.nazwa) and waliduj_cene(danie.cena) and waliduj_opis(danie.opis)


def waliduj_nazwe(nazwa):
    if len(nazwa) > 30:
        return False
    if nazwa[0] not in string.ascii_uppercase:
        return False
    for letter in nazwa[1:]:
        if letter not in string.whitespace or letter not in string.ascii_lowercase:
            return False
    return True


def waliduj_cene(cena):
    if re.search(r'^\d{1, 3}[,]\d{0,2}', cena):
        return True
    return False


def waliduj_opis(opis):
    for letter in Constants.NIEPOPRAWNE_ZNAKI:
        if letter in opis:
            return False
    return len(opis) < 300
