# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, escape, g ,render_template, url_for, redirect, request, flash, session
from flask_jwt import JWT, jwt_required

from security import authenticate, userrole_mapping, username_mapping

app = Flask(__name__)
app.secret_key = "key"


@app.route('/', methods=['GET','POST'])
def register():
    return render_template('register.html')


@app.route('/login', methods=['GET','POST'])
def index():
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


@app.route('/protected_klient')
def klient():
    if g.user:
        return render_template('results_client.html')
    return redirect(url_for('index'))


@app.route('/protected_dostawca')
def dostawca():
    if g.user:
        return render_template('results_worker.html', the_login=session['user'], the_title="Witaj dostawco!")
    return redirect(url_for('index'))


@app.route('/protected_pracownik_kuchni')
def kucharz():
    if g.user:
        return render_template('results_worker.html', the_login=session['user'], the_title="Witaj pracowniku kuchni!")
    return redirect(url_for('index'))

@app.route('/protected_menadzer_restauracji')
def menadzer():
    if g.user:
        return render_template('results_worker.html', the_login=session['user'], the_title="Witaj menadżerze restauracji!")
    return redirect(url_for('index'))



@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']


@app.route('/getsession')
def getsession():
    if 'user' in session:
        return session['user']
    return 'Not logged in!'


@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return 'Session dropped!'



if __name__ == '__main__':
   app.run(debug=True)
