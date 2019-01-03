from pip._vendor import requests
from werkzeug.security import safe_str_cmp
from user import User


#
# users = [
#   #  User(1, 'Kubica', 'formula1', "Radom", "51240149102", "robert@kwp.pl", "Dostawca"),
#   #  User(2, 'Klient', 'password', "Warszawa", "512412412", "kowalskit@kwp.pl", "Klient"),
#   #  User(3, 'Gessler', 'jedzenie', "Krakow", "742121392", "kucharka@gmail.com", "Pracownik kuchni"),
#   #  User(4, 'Boss', 'haslo', "Krakow", "313514125", "menadzer@gmail.com", "Menadżer restauracji")
#     User('janPan', 1, 'Jan', 'Nowak', '123456789', 'pracownik kuchni', 'soicrupogi'),
#     User('AAmen', 2, 'Andrzej', 'Adrianowski', '777888999', 'dostawca', '39084utco'),
#     User('KNow', 4, 'Kasia', 'Nowak', '333444555', 'menadzer restauracji', 'kKdPS'),
#
# ]
#
#
# username_mapping = {u.imie: u for u in users}
# userid_mapping = {u.id_pracownika: u for u in users}
# userrole_mapping = {u.stanowisko: u for u in users}


def authenticate(login, password, id_pracownika, haslo):
    if safe_str_cmp(login, id_pracownika) and safe_str_cmp(password, haslo):
        return True
    else:
        return False


