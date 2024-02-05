from flask import Blueprint

app_routes = Blueprint('app_routes', __name__)

# Importa las rutas individuales
from .index import index
from .mostrar_eventos import mostrar_eventos
from .formulario_donacion import formulario_donacion
from .login_administrador import login_administrador
from .historial_evento import historial_evento
from .formulario_evento import formulario_evento
from .formulario_inscripcion import formulario_inscripcion
from .administrador import administrador

# Registra las rutas en el Blueprint
app_routes.register_blueprint(index)
app_routes.register_blueprint(mostrar_eventos)
app_routes.register_blueprint(formulario_donacion)
app_routes.register_blueprint(login_administrador)
app_routes.register_blueprint(historial_evento)
app_routes.register_blueprint(formulario_evento)
app_routes.register_blueprint(formulario_inscripcion)
app_routes.register_blueprint(administrador)