import json
import requests


def pobierz_menu_restauracji(id_restauracji):
    menu_restauracji = requests.get(f'http://0.0.0.0:5000/pobierz_menu_restauracji?id_restauracji={id_restauracji}')
    return json.loads(menu_restauracji.text)


def pobierz_miasta():
    miasta = requests.get(f'http://0.0.0.0:5000/pobierz_miasta')
    return json.loads(miasta.text)


def pobierz_restauracje(id_miasta: int):
    miasta = requests.get(f'http://0.0.0.0:5000/pobierz_restauracje?id_miasta={id_miasta}')
    return json.loads(miasta.text)