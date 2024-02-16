from flask import render_template, Blueprint

administrador_bp = Blueprint('administrador_bp', __name__)

@administrador_bp.route('/administrador')
def administrador():
    return render_template('administrador.html')