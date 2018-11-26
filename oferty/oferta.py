from flask import Flask
from flask_cors import CORS


from zarzadzanie_oferta_restauracji import zarzadzanie_oferta_restauracji
from zarzadzanie_oferta_sieci import zarzadzanie_oferta_sieci

app = Flask(__name__)
cors = CORS(app)

app.register_blueprint(zarzadzanie_oferta_restauracji)
app.register_blueprint(zarzadzanie_oferta_sieci)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
