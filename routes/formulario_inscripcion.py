from flask import render_template
from . import app_routes

@app_routes.route('/inscripcion')
def formulario_inscripcion():
    return render_template('form_inscripcion.html')