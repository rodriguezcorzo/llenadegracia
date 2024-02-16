from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .usuario import Usuario
from . import Base

class Inscripcion(Base):
    __tablename__ = 'inscripciones'

    id_inscripcion = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(DateTime)
    id_evento = Column(Integer, ForeignKey('eventos.id_evento'))
    id_persona = Column(Integer, ForeignKey('personas.id_persona'))
    evento = relationship("Evento")
    persona = relationship("Persona")