import json
import requests


def pobierz_menu_restauracji(id_restauracji):
    menu_restauracji = requests.get(f'http://0.0.0.0:5000/pobierz_menu_restauracji?id_restauracji={id_restauracji}')
    return menu_restauracji.json()


def pobierz_miasta():
    miasta = requests.get(f'http://0.0.0.0:5000/pobierz_miasta')
    return miasta.json()


def pobierz_restauracje(miasto):
    restauracje = requests.get(f'http://0.0.0.0:5000/pobierz_restauracje_z_miasta?miasto={miasto}')
    return restauracje.json()
