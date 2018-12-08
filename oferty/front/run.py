from flask import Flask, render_template
from flask_cors import CORS, cross_origin

from config import Config
from oferta_sieci import oferta_sieci
from oferta_restauracji import oferta_restauracji
from formularz_potrawy_sieci import formularz_potrawy_sieci
from formularz_potrawy_restauracji import formularz_potrawy_restauracji

app = Flask(__name__)
app.config.from_object(Config)
cors = CORS(app)

app.register_blueprint(oferta_sieci)
app.register_blueprint(oferta_restauracji)
app.register_blueprint(formularz_potrawy_sieci)
app.register_blueprint(formularz_potrawy_restauracji)

if __name__ == '__main__':
    app.run(host=Config.FRONT_HOST, port=Config.FRONT_PORT)