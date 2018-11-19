import requests

# TEST pobierz_menu_restauracji
r1 = requests.get("http://127.0.0.1:5000/pobierz_menu_restauracji", json={'id_restauracji': 0})
print(r1.text)
print(r1.json())

