from sqlalchemy import Column, Integer, BigInteger, Text, String, DateTime, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship
from .usuario import Usuario
from . import Base

class Evento(Base):
    __tablename__ = 'eventos'

    id_evento = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(50), nullable=False)
    descripcion = Column(Text(500), nullable=False)
    fecha = Column(DateTime)
    imagen = Column(LargeBinary)
    id_usuario = Column(BigInteger, ForeignKey('Usuarios.id_usuario'))
    usuario = relationship("Usuarios")