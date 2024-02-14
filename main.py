from flask import Flask, render_template, request, redirect, url_for
from models.administrador import db

#* IMPORTACIONES LOCALES
from config import Config
from routes import app_routes

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(app_routes)
db.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
