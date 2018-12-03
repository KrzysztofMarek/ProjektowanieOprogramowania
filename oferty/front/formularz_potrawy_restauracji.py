from flask import Blueprint, render_template
from flask_cors import cross_origin

formularz_potrawy_restauracji = Blueprint('formularz_potrawy_restauracji', __name__)

@formularz_potrawy_restauracji.route('/formularz_potrawy_restauracji', defaults={'restaurant_id': 1}, methods=['GET'])
@formularz_potrawy_restauracji.route('/formularz_potrawy_restauracji/<restaurant_id>', methods=['GET'])
@cross_origin()
def wyswietl_formularz(restaurant_id):
    return render_template('formularz_potrawy_restauracji.html', restaurant_id=restaurant_id)