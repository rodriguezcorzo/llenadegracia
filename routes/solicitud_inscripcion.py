from flask import render_template, Blueprint
from sqlalchemy.orm import sessionmaker
from models import Evento, Persona, Inscripcion
from config import db

solicitud_inscripcion_bp = Blueprint('solicitud_incripcion_bp', __name__)

@solicitud_inscripcion_bp.route('/solicitud_inscripcion')
def solicitud_inscripion():
    # Crear una sesión de SQLAlchemy
    Session = sessionmaker(bind=db.engine)
    session = Session()

    # Obtener los eventos con personas inscritas
    eventos_con_participantes = []
    eventos = session.query(Evento).join(Inscripcion).group_by(Evento.id_evento).all()
    for evento in eventos:
        participantes = session.query(Persona).join(Inscripcion).filter(Inscripcion.id_evento == evento.id_evento).all()
        eventos_con_participantes.append((evento, participantes))

    # Cerrar la sesión de SQLAlchemy
    session.close()

    return render_template('solicitud_inscripcion.html', eventos_con_participantes=eventos_con_participantes)