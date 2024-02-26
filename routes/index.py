from flask import render_template, Blueprint
from models import Evento, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime
import base64

index_bp = Blueprint('index_bp', __name__)

engine = create_engine('mysql://root@localhost/llenadegracia')
Session = sessionmaker(bind=engine)

@index_bp.route('/')
def mostrar_eventos():
    # Crear una nueva sesión
    session = Session()

    eventos = session.query(
        Evento.titulo,
        Evento.descripcion,
        Evento.fecha,
        # Evento.costo,
        Evento.imagen
    )

    # Consulta para obtener próximos eventos
    eventos_proximos = session.query(
        Evento.id_evento,
        Evento.titulo,
        Evento.fecha,
        Evento.descripcion
    ).filter(Evento.fecha >= datetime.now()).order_by(Evento.fecha).all()

    # print(eventos_proximos)

    # Consulta para obtener eventos anteriores
    eventos_anteriores = session.query(
        Evento.titulo,
        Evento.fecha
    ).filter(Evento.fecha < datetime.now()).order_by(Evento.fecha.desc()).all()

    # Comprobar si hay eventos próximos
    hay_eventos = len(eventos_proximos) > 0

    # Cerrar la sesión
    session.close()

    return render_template('mostrar_eventos.html', eventos=eventos, eventos_proximos=eventos_proximos, eventos_anteriores=eventos_anteriores, hay_eventos=hay_eventos)