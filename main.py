from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#* IMPORTACIONES LOCALES
from config import Config
from routes import app_routes

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

app.register_blueprint(app_routes)

if __name__ == "__main__":
    app.run(debug=True)
