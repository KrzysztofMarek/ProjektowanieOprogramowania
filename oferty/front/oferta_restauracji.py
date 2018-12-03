from flask import Blueprint, render_template
from flask_cors import cross_origin

oferta_restauracji = Blueprint('oferta_restauracji', __name__)

@oferta_restauracji.route('/oferta_restauracji', defaults={'restaurant_id': 1}, methods=['GET'])
@oferta_restauracji.route('/oferta_restauracji/<restaurant_id>', methods=['GET'])
@cross_origin()
def wyswietl_oferte_restauracji(restaurant_id):
    return render_template('oferta_restauracji.html', restaurant_id=restaurant_id)