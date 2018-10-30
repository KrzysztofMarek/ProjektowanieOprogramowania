


def pobierz_menu_restauracji(restaurant_id):
    menu = {"danie1": ["ładny opis", "20.01 zł"], "danie2": ["smaczne i zdrowe", "120.00 zł"]}
    return menu


def pobierz_miasta():
    return {"Warszawa": 1, "Sierpc": 3, "Radom": 2}


def pobierz_restauracje(city_id):
    if city_id == '1':
        return ["Warszawska restauracja 1", "Warszawska restauracja 2"]
    elif city_id == '2':
        return ["Radomska restauracja 1", "Radomska restauracja 2"]
    elif city_id == '3':
        return ["Sierpcowe zakamarki", "Sierpcowe jadło"]