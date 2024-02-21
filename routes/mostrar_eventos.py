from flask import render_template, Blueprint

mostrar_eventos_bp = Blueprint('monstrar_eventos_bp', __name__)

@mostrar_eventos_bp.route('/Eventos')
def mostrar_eventos():
    return  render_template('mostrar_eventos.html')