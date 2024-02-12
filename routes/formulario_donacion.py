from flask import render_template, Blueprint

formulario_donacion_bp= Blueprint('formulario_donacion', __name__)

@formulario_donacion_bp.route('/donacion')
def formulario_donacion():
    return render_template('formulario_donacion.html')