from flask import render_template
from . import app_routes

@app_routes.route('/pagina-eventos')
def mostrar_eventos():
    print("Se está ejecutando la función de la página de eventos")
    return  render_template('mostrar_eventos.html')