from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Administrador(db.Model):
    ID_admin = db.Column(db.BigInteger, primary_key=True)
    Nombre = db.Column(db.String(30), nullable=False)
    Apellido = db.Column(db.String(30), nullable=False)
    Correo = db.Column(db.String(100), nullable=False)
    Celular = db.Column(db.BigInteger, nullable=False)
    Clave = db.Column(db.String(150), nullable=False)