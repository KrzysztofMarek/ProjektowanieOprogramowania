import json
import requests


def pobierz_menu_restauracji(id_restauracji):
    menu_restauracji = requests.get(f'http://localhost:5000/pobierz_menu_restauracji?id_restauracji={id_restauracji}')
    return json.loads(menu_restauracji.text)
