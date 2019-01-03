# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, escape, g ,render_template, url_for, redirect, request, flash, session
from flask_jwt import JWT, jwt_required
import requests
from security import authenticate
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.secret_key = "key"


@app.route('/', methods=['GET','POST'])
def rejestruj():
    return render_template('register.html')


@app.route('/login', methods=['GET','POST'])
def waliduj():
    if request.method == 'POST':
        session.pop('user', None)
        login = request.form['login']
        password = request.form['password']
        parameters = {"id_pracownika": login}
        response = requests.get("http://127.0.0.1:5000/pobierz_pracownika", params=parameters)
        data = response.json()
        if "success" not in data:
            if authenticate(login, password, data["login"], data["hasło"]):
                session['user'] = request.form['login']
                if data['stanowisko'] == "Pracownik kuchni":
                    return redirect(url_for("kucharz"))
                elif data['stanowisko'] == 'Dostawca':
                    return redirect(url_for("dostawca"))
                else:
                    return redirect(url_for("menadzer"))
        parameters_2 = {"id_klienta": login}
        response_2 = requests.get("http://127.0.0.1:5000/pobierz_klienta", params=parameters_2)
        data_2 = response_2.json()
        if "success" not in data_2:
            if authenticate(login, password, data_2["login"], data_2["hasło"]):
                session['user'] = request.form['login']
                return redirect(url_for("klient"))

    return render_template('login.html')


@app.route('/widok_klient')
def klient():
    if g.user:
        return render_template('results_client.html',the_login=session['user'])
    return redirect(url_for('waliduj'))


@app.route('/widok_dostawca')
def dostawca():
    if g.user:
        return render_template('results_worker.html', the_login=session['user'], the_title="Witaj dostawco!")
    return redirect(url_for('waliduj'))


@app.route('/widok_pracownik_kuchni')
def kucharz():
    if g.user:
        return render_template('results_worker.html', the_login=session['user'], the_title="Witaj pracowniku kuchni!")
    return redirect(url_for('waliduj'))


@app.route('/protected_menadzer_restauracji')
def menadzer():
    if g.user:
        return render_template('results_worker.html', the_login=session['user'], the_title="Witaj menadżerze restauracji!")
    return redirect(url_for('waliduj'))



@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']


@app.route('/sesja')
def getsession():
    if 'user' in session:
        return session['user']
    return 'Not logged in!'


@app.route('/usunsesje')
def dropsession():
    session.pop('user', None)
    return 'Session dropped!'



if __name__ == '__main__':
   app.run(debug=True, port=7777)
