from flask import Blueprint, url_for, request, redirect, render_template, flash, session, make_response
from werkzeug.security import check_password_hash
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Usuario

# Función para establecer la conexión con la base de datos
def establecer_conexion():
    engine = create_engine('mysql://root@localhost/llenadegracia')
    Session = sessionmaker(bind=engine)
    return Session()

# Función para renderizar la página de inicio de sesión
def renderizar_inicio_sesion(error=None):
    # Creamos una respuesta que deshabilita la caché
    response = make_response(render_template('login.html', error=error))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'  # Deshabilita la caché en el navegador
    response.headers['Pragma'] = 'no-cache'  # Para versiones anteriores de HTTP
    response.headers['Expires'] = '0'  # Para versiones anteriores de HTTP
    return response

login_administrador_bp = Blueprint('login_administrador_bp', __name__)

@login_administrador_bp.route('/inicio_de_sesion', methods=['GET', 'POST'])
def login_administrador():
    error = None
    if request.method == 'POST':
        # Verificar si se han proporcionado credenciales
        if 'ID_admin' in request.form and 'password' in request.form:
            username = request.form['ID_admin']
            password = request.form['password']
            session_db = establecer_conexion()
            usuario = session_db.query(Usuario).filter_by(clave=username).first()
            if usuario:
                if check_password_hash(usuario.clave, password):
                    session['id_usuario'] = usuario.id_usuario
                    return redirect(url_for('administrador'))
                else:
                    error = 'Contraseña incorrecta.'
            else:
                error = 'Usuario no encontrado.'
        else:
            error = 'Por favor, proporciona el nombre de usuario y la contraseña.'
    return renderizar_inicio_sesion(error)

@login_administrador_bp.route('/administrador')
def administrador():
    if 'id_usuario' in session:
        session_db = establecer_conexion()
        usuario = session_db.query(Usuario).get(session['id_usuario'])
        return render_template('administrador.html', usuario=usuario)
    else:
        return redirect(url_for('login_administrador_bp.login_administrador'))

@login_administrador_bp.route('/logout')
def logout():
    session.pop('id_usuario', None)
    return redirect(url_for('login_administrador_bp.login_administrador'))