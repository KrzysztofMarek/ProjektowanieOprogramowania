import json
import requests


def pobierz_menu_sieci():
    menu_sieci = requests.get('http://localhost:5000/pobierz_menu_restauracji?id_restauracji=0')
    return json.loads(menu_sieci.text)


def dodaj_danie_dla_sieci(danie):
    danie["id_sieci"] = 0
    danie['cena'] = float(danie['cena'].replace(',', '.'))
    url = 'http://localhost:5000/dodaj_danie'
    response_db = requests.post(url, json=danie)
    return "OK"
    # return response_db # KURWA TO JE RESPONSE, tego sie nie da zwrocic :P
