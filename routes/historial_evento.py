from flask import render_template
from . import app_routes

@app_routes.route('/eventos')
def historial_evento():
    return render_template('eventos.html')