from flask import Blueprint, render_template, request
from flask_cors import cross_origin

formularz_potrawy_restauracji = Blueprint('formularz_potrawy_restauracji', __name__)


@formularz_potrawy_restauracji.route('/formularz_potrawy_restauracji', defaults={'restaurant_id': 1}, methods=['GET'])
@formularz_potrawy_restauracji.route('/formularz_potrawy_restauracji/<restaurant_id>', methods=['GET'])
@cross_origin()
def wyswietl_formularz(restaurant_id):
    return render_template('formularz_potrawy_restauracji.html', restaurant_id=restaurant_id)


@formularz_potrawy_restauracji.route('/edycja_potrawy_restauracji', methods=['POST'])
@cross_origin()
def wyswietl_edycja():
    restaurant_id = request.form['restaurant_id']
    dish_id = request.form['dish_id']
    dish_name = request.form['dish_name']
    dish_price = request.form['dish_price']
    dish_desc = request.form['dish_desc']
    return render_template('edycja_potrawy_restauracji.html',
                           restaurant_id=restaurant_id, dish_id=dish_id, dish_name=dish_name, dish_price=dish_price, dish_desc=dish_desc)
