import json
import requests


def pobierz_menu_model_siec():
    menu_sieci = requests.get('http://localhost:5000/pobierz_menu_restauracji?id_restauracji=0')
    return menu_sieci.json()


def dodaj_danie_dla_sieci(danie):
    danie["id_restauracji"] = 0
    danie['cena'] = float(danie['cena'].replace(',', '.'))
    url = 'http://localhost:5000/dodaj_danie'
    response_db = requests.post(url, json=danie)
    return "OK"
