from flask import render_template
from . import app_routes

@app_routes.route('/formulario-evento')
def formulario_evento():
    return render_template('form_evento.html')