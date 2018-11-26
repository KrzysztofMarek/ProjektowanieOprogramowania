import json
import re
import requests
import string

from flask import Blueprint, jsonify,request
from flask_cors import cross_origin


import zarzadzanie_siecia_model as model_zs


zarzadzanie_oferta_sieci = Blueprint('zarzadzanie_oferta_sieci', __name__)


@zarzadzanie_oferta_sieci.route('/pobierz_menu_sieci', methods=['GET'])
@cross_origin()
def pobierz_menu_sieci():
    menu_sieci = model_zs.pobierz_menu_sieci()
    return jsonify(menu_sieci)


@zarzadzanie_oferta_sieci.route('/dodaj_danie_siec', methods=['POST'])
@cross_origin()
def dodaj_danie():
    danie = request.json
    if waliduj_danie(danie):
        return model_zs.dodaj_danie_dla_sieci(danie)
    return "Danie nie jest poprawne. Sprawdz wszystkie pola"


def waliduj_danie(danie: dict):
    elementy_dania = ["nazwa", "cena", "opis"]
    for element in danie:
        if element not in elementy_dania:
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
    for letter in opis:
        if letter in "!@#$^%*&":
            return False
    return len(opis) < 300
