from flask import render_template, Blueprint, request, url_for, redirect
from datetime import datetime
from config import db
from sqlalchemy.orm import sessionmaker
from models import Persona, Donacion

formulario_donacion_bp= Blueprint('formulario_donacion', __name__)

@formulario_donacion_bp.route('/formulario_donacion', methods=['GEt', 'POST'])
def formulario_donacion():

    Session = sessionmaker(bind=db.engine)

    if request.method == 'POST':
        # Capturar datos del formulario
        cedula = request.form['cedula']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        celular = request.form['celular']
        direccion = request.form['direccion']
        descripcion_donacion = request.form['descripcionDonacion']
        
        session = Session()
        persona = session.query(Persona).filter_by(cedula=cedula).first()
        if not persona:

            persona = Persona(cedula=cedula, nombre=nombre, apellido=apellido, correo=correo, celular=celular, direccion=direccion)
            session.add(persona)
            session.commit()
        
        donacion = Donacion(descripcion=descripcion_donacion, fecha=datetime.now(), persona=persona)
        session.add(donacion)
        session.commit()

        return redirect(url_for('app_routes.index_bp.index'))

    return render_template('formulario_donacion.html')