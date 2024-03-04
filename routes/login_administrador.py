from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import check_password_hash
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Usuario
from config import db
from sqlalchemy import text

login_administrador_bp = Blueprint('login_administrador_bp', __name__)

@login_administrador_bp.route('/inicio_de_sesion', methods=['GET', 'POST'])
def login_administrador():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['pass']

        print(user, password)
        
        # Consulta SQL para buscar al usuario por ID de usuario
        query = text(f"SELECT * FROM usuarios WHERE id_usuario = '{user}'")
        usuario = db.session.execute(query).fetchone()
        print(usuario)
        
        if usuario:
            # Verificar la contraseña
            if check_password_hash(usuario.clave, password):
                # Iniciar sesión
                session['user_id'] = usuario.id_usuario
                flash('¡Inicio de sesión exitoso!', 'success')
                print(session)
                return redirect(url_for('administrador_bp.administrador'))
            else:
                flash('¡Contraseña incorrecta!', 'error')
        else:
            flash('¡Usuario no encontrado!', 'error')
    
    return render_template('login.html')