from flask import render_template, Blueprint, request, redirect, url_for
from models.evento import Evento, db

formulario_evento_bp = Blueprint('formulario_evento_bp', __name__)

@formulario_evento_bp.route('/crear-evento', methods=['GET', 'POST'])
def formulario_evento():
    if request.method == 'POST':
        titulo = request.form['nombreEvento']
        descripcion = request.form['descripcionEvento']
        fecha = request.form['fecha']
        imagenes = request.files.getlist('imagenes[]')
        costo = request.form.get('costo')
        #*el id_admin se obtiene atravez de la sesion
        # id_admin = request.form['id_admin']

        nuevo_evento = Evento(
            Titulo=titulo,
            Descripcion=descripcion,
            Fecha=fecha,
            Imagen=imagenes,
            Costo=costo,
            #*Se obtiene atraves de la sesions
            #ID_admin=id_admin
        )

        db.session.add(nuevo_evento)
        db.session.commit()

        return redirect(url_for('formulario_evento_bp.formulario_evento'))
    return render_template('formulario_evento.html')