def add_dish(restaurant_id, name, price, description):
    pass


def modify_dish(dish_id, restaurant_id, name, price, description):
    pass


def remove_dish(dish_id):
    pass


def get_restaurant_menu(restaurant_id):
    menu = {"danie1": ["ładny opis", "20.01 zł"], "danie2": ["smaczne i zdrowe", "120.00 zł"]}
    return menu


def get_cities():
    return {"Warszawa": 1, "Sierpc": 2, "Radom": 3}


def get_restaurants_from_city(city_id):
    if city_id == 1:
        return ["Warszawska_restauracja 1", "Warszawska restauracja 2"]
    elif city_id == 2:
        return ["Radomska_restauracja 1", "Radomska restauracja 2"]
    elif city_id == 3:
        return ["Sierpcowe_zakamarki", "Sierpcowe jadło"]