from flask import Blueprint, render_template, request
from flask_cors import cross_origin

formularz_potrawy_sieci = Blueprint('formularz_potrawy_sieci', __name__)

@formularz_potrawy_sieci.route('/formularz_potrawy_sieci', methods=['GET'])
@cross_origin()
def wyswietl_formularz():
    return render_template('formularz_potrawy_sieci.html')


@formularz_potrawy_sieci.route('/edycja_potrawy_sieci', methods=['POST'])
@cross_origin()
def wyswietl_edycja():
    dish_id = request.form['dish_id']
    dish_name = request.form['dish_name']
    dish_price = request.form['dish_price']
    dish_desc = request.form['dish_desc']
    return render_template('edycja_potrawy_sieci.html', dish_id=dish_id, dish_name=dish_name, dish_price=dish_price, dish_desc=dish_desc)
