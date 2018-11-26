import json
import requests


def pobierz_menu_restauracji(id_restauracji):
    menu_restauracji = requests.get(f'http://localhost:5000/pobierz_menu_restauracji?id_restauracji={id_restauracji}')
    return json.loads(menu_restauracji.text)

def dodaj_danie_dla_restauracji(danie):
    danie['cena'] = float(danie['cena'].replace(',', '.'))
    url = 'http://localhost:5000/dodaj_danie'
    response_db = requests.post(url, json=danie)
    return "OK"
    # return response_db # KURWA TO JE RESPONSE, tego sie nie da zwrocic :P
