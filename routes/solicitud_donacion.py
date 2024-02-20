from flask import render_template, Blueprint
from config import db
from models import Donacion, Persona
from sqlalchemy import func

solicitud_donacion_bp = Blueprint('solicitud_donacion_bp', __name__)

@solicitud_donacion_bp.route('/solicitud_donacion')
def solicitud_donancion():
    datos_donaciones = db.session.query(
        Donacion.descripcion,
        func.cast(Donacion.fecha, db.DateTime),
        Persona.nombre,
        Persona.apellido,
        Persona.direccion,
        Persona.celular
    ).join(Persona).order_by(Donacion.fecha.desc()).all()
    return render_template('solicitud_donacion.html', datos_donaciones=datos_donaciones)