from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/administrador')
def administrador():
    return render_template('administrador.html')

@app.route('/formulario-evento')
def formulario_evento():
    return render_template('form_evento.html')

@app.route('/inscripcion')
def formulario_inscripcion():
    return render_template('form_inscripcion.html')

@app.route('/donacion')
def formulario_donacion():
    return render_template('form_donacion.html')

@app.route('/eventos')
def eventos():
    return render_template('eventos.html')

@app.route('/pagina-eventos')
def pagina_eventos():
    print("Se está ejecutando la función de la página de eventos")
    return  render_template('pagina_eventos.html')

if __name__ == "__main__":
    app.run(debug=True)
