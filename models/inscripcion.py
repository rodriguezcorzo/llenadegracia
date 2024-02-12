from . import db

class Inscripcion(db.Model):
    ID_inscripcion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ID_evento = db.Column(db.Integer, db.ForeignKey('evento.ID_evento'))
    ID_usuario = db.Column(db.BigInteger, db.ForeignKey('usuario.ID_usuario'))
    fecha_inscripcion = db.Column(db.Date)
    evento = db.relationship('Evento', backref=db.backref('inscripciones', lazy=True))
    usuario = db.relationship('Participante', backref=db.backref('inscripciones', lazy=True))