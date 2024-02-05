from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Evento(db.Model):
    ID_evento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Titulo = db.Column(db.String(50), nullable=False)
    Descripcion = db.Column(db.String(500), nullable=False)
    Fecha = db.Column(db.Date, nullable=False)
    Imagen = db.Column(db.LargeBinary)
    Costo = db.Column(db.Integer)
    ID_admin = db.Column(db.BigInteger, db.ForeignKey('administrador.ID_admin'))
    administrador = db.relationship('Administrador', backref=db.backref('eventos', lazy=True))