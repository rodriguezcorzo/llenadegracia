from flask import render_template, Blueprint, redirect, url_for, request, jsonify
from werkzeug.security import check_password_hash
from models.usuario import Usuario
from config import db

login_administrador_bp = Blueprint('login_administrador_bp', __name__)

@login_administrador_bp.route('/inicio_de_sesion', methods=['GET','POST'])
def login_administrador():
    datos_usuario = request.get_json()
    usuario = datos_usuario.get('ID_admin')
    password = datos_usuario.get('password')
    
    if request.method == 'POST':
        if not usuario or not password:
            error_message = "Por favor, completa todos los campos."
            return jsonify({'error': error_message}), 400
        
        administrador = Usuario.query.get(usuario)
        if administrador and check_password_hash(administrador.clave, password):
            print('Autenticación exitosa.')
            return jsonify({'ok': True, 'redirect_url': url_for('administrador_bp.administrador')})
        else:
            error_message = 'Número de identificación o contraseña incorrectos. Por favor, inténtalo de nuevo.'
            return jsonify({'ok':False, 'error': error_message}), 401
        
    return jsonify({'ok':False, 'error':'Error al procesar la petición'})