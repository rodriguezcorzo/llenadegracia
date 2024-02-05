from flask import render_template
from . import app_routes

@app_routes.route('/donacion')
def formulario_donacion():
    return render_template('form_donacion.html')