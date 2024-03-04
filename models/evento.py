from sqlalchemy import Column, Integer, BigInteger, Text, String, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import LONGBLOB
from sqlalchemy.orm import relationship
from .usuario import Usuario
from . import Base

class Evento(Base):
    __tablename__ = 'eventos'

    id_evento = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(50), nullable=False)
    descripcion = Column(Text(2000), nullable=False)
    fecha = Column(DateTime)
    imagen = Column(LONGBLOB)
    #costo = Column(Integer)
    id_usuario = Column(BigInteger, ForeignKey('usuarios.id_usuario'))
    usuario = relationship("Usuario", lazy='joined')

    # Configurar carga eager para la imagen
    __mapper_args__ = {
        'eager_defaults': True
    }