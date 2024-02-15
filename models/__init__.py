from sqlalchemy import create_engine, Column, BigInteger, Integer, Text, DateTime, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

from .persona import Persona
from .usuario import Usuario
from .evento import Evento
from .inscripcion import Inscripcion
from .donacion import Donacion