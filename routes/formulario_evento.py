from flask import render_template, Blueprint, request, redirect, url_for
from config import db
from models.evento import Evento

formulario_evento_bp = Blueprint('formulario_evento_bp', __name__)

@formulario_evento_bp.route('/crear_evento', methods=['GET', 'POST'])
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
            titulo=titulo,
            descripcion=descripcion,
            fecha=fecha,
            imagen=imagenes,
            costo=costo,
            #*Se obtiene atraves de la sesions
            #ID_admin=id_admin
        )

        db.session.add(nuevo_evento)
        db.session.commit()

        return redirect(url_for('formulario_evento_bp.formulario_evento'))
    return render_template('formulario_evento.html')