from flask import render_template, Blueprint, request, redirect, url_for
from config import db
from models.usuario import Persona

formulario_inscripcion_bp = Blueprint('Formulario_inscripcion_bp', __name__)

@formulario_inscripcion_bp.route('/inscripcion')
def formulario_inscripcion():
    return render_template('formulario_inscripcion.html')

@formulario_inscripcion_bp.route('/crear_participante', methods=['POST'])
def crear_participante():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    correo = request.form['correo']
    celular = request.form['celular']
    profesion = request.form['profesion']

    nuevo_participante = Persona(
        Nombre=nombre,
        Apellido=apellido,
        Correo=correo,
        Celular=celular,
        Profesion=profesion
    )

    db.session.add(nuevo_participante)
    db.session.commit()

    return redirect(url_for('Formulario_inscripcion_bp.formulario_inscripcion'))