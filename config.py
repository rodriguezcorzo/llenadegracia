from flask_sqlalchemy import SQLAlchemy

class Config:
    SECRET_KEY = '6547c09aad56961ec53cfaa155084e86'
    DEBUG = True
    TESTING = True

    # Configuración de la base de datos MySQL
    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/llenadegracia'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy()