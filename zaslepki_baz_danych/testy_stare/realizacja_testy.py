import requests


# TEST zmien_status zamowienia
r1 = requests.post("http://127.0.0.1:5000/zmien_status_zamowienia", json={'id_zamowienia': 1, 'status': "Anulowane"})
print(r1.text)
