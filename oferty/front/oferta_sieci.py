from flask import Blueprint, render_template
from flask_cors import cross_origin

oferta_sieci = Blueprint('oferta_sieci', __name__)

@oferta_sieci.route('/oferta_sieci', methods=['GET'])
@cross_origin()
def wyswietl_oferte_sieci():
    return render_template('oferta_sieci.html')