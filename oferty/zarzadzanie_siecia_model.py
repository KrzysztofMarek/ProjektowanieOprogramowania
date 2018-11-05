import json
import requests


def pobierz_menu_sieci():
    menu_sieci = requests.get('http://0.0.0.0:5000/pobierz_menu_restauracji?id_restauracji=0')
    return json.loads(menu_sieci.text)
