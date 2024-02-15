from . import Base, Column, Integer, BigInteger, String, ForeignKey
from sqlalchemy.orm import relationship
from .persona import Persona

class Usuario(Base):
    __tablename__ = 'usuarios'

    id_usuario = Column(BigInteger, primary_key=True)
    clave = Column(String(150), nullable=False)
    id_persona = Column(Integer, ForeignKey('Personas.id_persona'))
    persona = relationship("Persona")