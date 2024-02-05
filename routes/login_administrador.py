from flask import render_template, redirect, url_for, request
from . import app_routes

@app_routes.route('/inicio-de-sesion', methods=['GET', 'POST'])
def login_administrador():
    if request.method == 'POST':
        print(request.form['username'])
        print(request.form['password'])
        return render_template('administrador.html')
    else:
        return render_template('login.html')
