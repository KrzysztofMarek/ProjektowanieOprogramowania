from user import User
from werkzeug.security import safe_str_cmp

users = [
    User(1, 'Kubica', 'formula1', "Radom", "51240149102", "robert@kwp.pl", "Dostawca"),
    User(2, 'Klient', 'password', "Warszawa", "512412412", "kowalskit@kwp.pl", "Klient"),
    User(3, 'Gessler', 'jedzenie', "Krakow", "742121392", "kucharka@gmail.com", "Pracownik kuchni"),
    User(4, 'Boss', 'haslo', "Krakow", "313514125", "menadzer@gmail.com", "Menadżer restauracji")
]


username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}
userrole_mapping = {u.role: u for u in users}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return True



