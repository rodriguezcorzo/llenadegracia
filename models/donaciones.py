from . import db

class Donacion(db.Model):
    ID_donacion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(30))
    apellido = db.Column(db.String(30))
    correo = db.Column(db.String(100))
    celular = db.Column(db.BigInteger)
    direccion = db.Column(db.String(100))
    descripcion = db.Column(db.String(200))
    fecha = db.Column(db.DateTime)