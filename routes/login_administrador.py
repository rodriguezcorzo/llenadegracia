from flask import Blueprint, url_for, request, redirect, render_template
from werkzeug.security import check_password_hash
from models import Base, Usuario
from sqlalchemy.orm import sessionmaker
from werkzeug.security import check_password_hash
from sqlalchemy import create_engine
from models.usuario import Usuario

login_administrador_bp = Blueprint('login_administrador_bp', __name__)

@login_administrador_bp.route('/inicio_de_sesion', methods=['GET','POST'])
def login_administrador():

    engine = create_engine('mysql://root@localhost/llenadegracia')
    Session = sessionmaker(bind=engine)  # Crea una sesión de SQLAlchemy
    session = Session()

    if request.method == 'POST':
            usuario = request.form.get('ID_admin')
            password = request.form.get('password')

            if not usuario or not password:
                return redirect(url_for('app_routes.login_administrador_bp.login_administrador'))

            administrador = session.query(Usuario).filter_by(id_usuario=usuario).first()
            if administrador:
                if check_password_hash(administrador.clave, password):
                    print('Autenticación exitosa.')
                    return redirect(url_for('administrador_bp.administrador'))

    # Si la solicitud es GET o si la autenticación falló, muestra el formulario de inicio de sesión
    return render_template('login.html')