import json
import requests
from flask import jsonify


def pobierz_menu_model_rest(id_restauracji):
    url = f'http://localhost:5000/pobierz_menu_restauracji?id_restauracji={id_restauracji}'
    menu_restauracji = requests.get(url)
    return menu_restauracji.json()


def dodaj_danie_dla_restauracji(danie):
    danie['cena'] = float(danie['cena'].replace(',', '.'))
    danie['id_restauracji'] = int(danie['id_restauracji'])
    url = 'http://localhost:5000/dodaj_danie'
    response_db = requests.post(url, json=danie)
    return "OK"


def modyfikuj_d(danie):
    danie['cena'] = float(danie['cena'].replace(',', '.'))
    danie['id_restauracji'] = int(danie['id_restauracji'])
    url = 'http://localhost:5000/modyfikuj_danie'
    response_db = requests.post(url, json=danie)
    return "OK"


def usun_d(id_dania, id_restauracji):
    url = f'http://localhost:5000/usun_danie?id_restauracji={id_restauracji}&id_dania={id_dania}'
    response_db = requests.get(url)
    return "OK"
