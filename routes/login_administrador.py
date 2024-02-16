from flask import render_template, Blueprint, redirect, url_for, request
from models.usuario import Usuario
from config import db

login_administrador_bp = Blueprint('login_administrador_bp', __name__)

@login_administrador_bp.route('/inicio-de-sesion', methods=['GET', 'POST'])
def login_administrador():
    
    error_message = None

    if request.method == 'POST':
        ID_admin = request.form['ID_admin']
        password = request.form['password']

        if not ID_admin or not password:
            error_message = "Por favor, completa todos los campos."
            return render_template('login.html', error_message=error_message)

        administrador = db.session.query(Usuario).filter_by(id_usuario=ID_admin).first()

        if administrador and administrador.check_password(password):
            print('Autenticación exitosa.')
            return redirect(url_for('administrador_bp'))
        else:
            error_message = "Número de identificación o contraseña incorrectos. Por favor, inténtalo de nuevo."
            
    return render_template('login.html', error_message=error_message)