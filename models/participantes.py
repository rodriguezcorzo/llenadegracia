from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Participante(db.Model):
    ID_usuario = db.Column(db.BigInteger, primary_key=True)
    Nombre = db.Column(db.String(50), nullable=False)
    Apellido = db.Column(db.String(50), nullable=False)
    Correo = db.Column(db.String(100), nullable=False)
    Celular = db.Column(db.BigInteger, nullable=False)
    Profesion = db.Column(db.String(30))