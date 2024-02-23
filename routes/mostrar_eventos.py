from flask import render_template, Blueprint
from models import Evento, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import func
from datetime import datetime  # Importa datetime desde la biblioteca datetime

mostrar_eventos_bp = Blueprint('mostrar_eventos_bp', __name__)

engine = create_engine('mysql://root@localhost/llenadegracia')
Session = sessionmaker(bind=engine)

@mostrar_eventos_bp.route('/pagina-eventos')
def mostrar_eventos():
    eventos = Base.session.query(
        Evento.titulo,
        Evento.descripcion,
        Evento.fecha,
        Evento.costo,
        Evento.imagen
    ).order_by(Evento.fecha.desc()).all()

    # Consulta para obtener próximos eventos
    eventos_proximos = Base.session.query(
        Evento.titulo,
        Evento.fecha,
        Evento.descripcion
    ).filter(Evento.fecha >= datetime.now()).all()

    # Consulta para obtener eventos anteriores
    eventos_anteriores = Base.session.query(
        Evento.titulo,
        Evento.fecha
    ).filter(Evento.fecha < datetime.now()).all()

    # Comprobar si hay eventos próximos
    hay_eventos = len(eventos_proximos) > 0

    return render_template('pagina_eventos.html', eventos=eventos, eventos_proximos=eventos_proximos, eventos_anteriores=eventos_anteriores, hay_eventos=hay_eventos)