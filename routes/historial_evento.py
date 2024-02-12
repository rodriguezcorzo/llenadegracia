from flask import render_template, Blueprint

historial_evento_bp = Blueprint('historial_evento_bp', __name__)

@historial_evento_bp.route('/historial_de_eventos')
def historial_evento():
    return render_template('historial_eventos.html')