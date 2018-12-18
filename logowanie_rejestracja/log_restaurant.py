# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, escape, g ,render_template, url_for, redirect, request, flash, session
from flask_jwt import JWT, jwt_required
from security import authenticate, userrole_mapping, username_mapping
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
        if authenticate(login, password):
            session['user'] = request.form['login']
            if username_mapping.get(str(request.form['login'])).role == "Pracownik kuchni":
                return redirect(url_for("kucharz"))
            elif username_mapping.get(str(request.form['login'])).role == "Klient":
                return redirect(url_for("klient"))
            elif username_mapping.get(str(request.form['login'])).role == "Dostawca":
                return redirect(url_for("dostawca"))
            else:
                return redirect(url_for("menadzer"))
    return render_template('login.html')


@app.route('/widok_klient')
def klient():
    if g.user:
        return render_template('results_client.html')
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
