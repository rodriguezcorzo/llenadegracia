from . import Base, Column, Integer, BigInteger, String
from config import db

class Persona(Base):
    __tablename__ = 'personas'

    id_persona = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(30), nullable=False)
    apellido = Column(String(30), nullable=False)
    cedula = Column(BigInteger, nullable=False)
    correo = Column(String(100), nullable=False)
    celular = Column(BigInteger, nullable=False)
    direccion = Column(String(100), nullable=False)
    profesion = Column(String(100))