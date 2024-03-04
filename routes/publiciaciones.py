from flask import render_template, Blueprint
from sqlalchemy.orm import sessionmaker 
from sqlalchemy import desc
from models import Evento
from sqlalchemy import create_engine
from config import db

publicaciones_pb = Blueprint('publicaciones_pb', __name__)

@publicaciones_pb.route('/publicaciones')
def mostrar_publicaciones():
    # Establecer la conexión a la base de datos
    engine = create_engine('mysql://root@localhost/llenadegracia')
    Session = sessionmaker(bind=engine)
    
    # Obtener la sesión de la base de datos
    session = Session()

    # Consultar todos los eventos ordenados por fecha en orden descendente
    eventos = session.query(Evento).order_by(desc(Evento.fecha)).all()

    # Cerrar la sesión
    session.close()

    # Pasar los eventos a la plantilla y renderizarla
    return render_template('publicaciones.html', eventos=eventos)