from flask import render_template, Blueprint, redirect, url_for, request
from models import Administrador

login_administrador_bp = Blueprint('login_administrador_bp', __name__)

@login_administrador_bp.route('/inicio-de-sesion', methods=['GET', 'POST'])
def login_administrador():
    if request.method == 'POST':
        ID_admin = request.form['ID_admin']
        password = request.form['password']

        administrador = Administrador.query.filter_by(ID_admin=ID_admin).first()

        if administrador and administrador.check_password(password):
            return redirect(url_for('ruta_de_administrador'))
        else:
            error_message = "Número de identificación o contraseña incorrectos. Por favor, inténtalo de nuevo."
            return render_template('login.html', error_message=error_message)
    else:
        return render_template('login.html')
