from flask import render_template, Blueprint, redirect, url_for, session
from functools import wraps

historial_evento_bp = Blueprint('historial_evento_bp', __name__)

def require_admin(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if session.get('user_role') != 'admin':
            return redirect(url_for('app_routes.login_administrador_bp.login_administrador'))  # Redirecciona a la página de inicio de sesión si el usuario no es administrador
        return func(*args, **kwargs)
    return decorated_function

@historial_evento_bp.route('/historial_de_eventos')
@require_admin
def historial_evento():
    return render_template('historial_eventos.html')
