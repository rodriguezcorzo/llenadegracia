from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .persona import Persona
from . import Base

class Donacion(Base):
    __tablename__ = 'donaciones'

    id_donacion = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(Text(500), nullable=False)
    fecha = Column(DateTime)
    id_persona = Column(Integer, ForeignKey('Personas.id_persona'))
    persona = relationship("Personas")