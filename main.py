from flask import Flask

#* IMPORTACIONES LOCALES
from config import Config, db
from routes import app_routes

app = Flask(__name__)
app.config.from_object(Config)

# Inicializar la instancia de SQLAlchemy
db.init_app(app)

app.register_blueprint(app_routes)

if __name__ == "__main__":
    app.run(debug=True)
