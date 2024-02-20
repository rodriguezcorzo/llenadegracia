from flask import Blueprint, url_for, request, redirect, render_template
from werkzeug.security import check_password_hash
from models.usuario import Usuario

login_administrador_bp = Blueprint('login_administrador_bp', __name__)

@login_administrador_bp.route('/inicio_de_sesion', methods=['GET','POST'])
def login_administrador():

    if request.method == 'GET':
        return render_template('login.html')

    usuario = request.form.get('ID_admin')
    password = request.form.get('password')

    if not usuario or not password:
        return redirect(url_for('app_routes.login_administrador_bp.login_administrador'))

    administrador = Usuario.query.filter_by(id_usuario=usuario).first()
    if administrador and check_password_hash(administrador.clave, password):
        print('Autenticación exitosa.')
        return redirect(url_for('app_routes.administrador_bp.administrador'))
    else:
        return redirect(url_for('app_routes.login_administrador_bp.login_administrador'))