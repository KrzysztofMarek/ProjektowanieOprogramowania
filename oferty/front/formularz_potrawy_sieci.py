from flask import Blueprint, render_template
from flask_cors import cross_origin

formularz_potrawy_sieci = Blueprint('formularz_potrawy_sieci', __name__)

@formularz_potrawy_sieci.route('/formularz_potrawy_sieci', methods=['GET'])
@cross_origin()
def wyswietl_formularz():
    return render_template('formularz_potrawy_sieci.html')