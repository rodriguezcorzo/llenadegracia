from flask import render_template, Blueprint, request, redirect, url_for
from sqlalchemy.orm import sessionmaker
from config import db
from models import Evento, Persona, Inscripcion
from datetime import datetime

formulario_inscripcion_bp = Blueprint('Formulario_inscripcion_bp', __name__)

@formulario_inscripcion_bp.route('/inscripcion/<int:id_evento>', methods=['GET', 'POST'])
def formulario_inscripcion(id_evento):
    Session = sessionmaker(bind=db.engine)

    if request.method == 'POST':
        session = Session()

        nombre = request.form['nombre']
        apellido = request.form['apellido']
        cedula = request.form['cedula']
        correo = request.form['correo']
        celular = request.form['celular']
        direccion = request.form['direccion']
        profesion = request.form['profesion']

        nueva_persona = Persona(nombre=nombre, apellido=apellido, cedula=cedula, correo=correo,
                                celular=celular, direccion=direccion, profesion=profesion)
        session.add(nueva_persona)
        session.flush()

        evento = session.query(Evento).get(id_evento)

        nueva_inscripcion = Inscripcion(fecha=datetime.now(), persona=nueva_persona, evento=evento)
        session.add(nueva_inscripcion)
        session.commit()

        session.close()

        return redirect(url_for('app_routes.Formulario_inscripcion_bp.formulario_inscripcion', id_evento=id_evento))
    else:
        session = Session()
        evento = session.query(Evento).get(id_evento)
        session.close()

        return render_template('formulario_inscripcion.html', id_evento=id_evento, evento=evento)