from flask import Blueprint
from base64 import b64encode

app_routes = Blueprint('app_routes', __name__)

# Importa las rutas individuales
from .index import index_bp
from .mostrar_eventos import mostrar_eventos_bp
from .formulario_donacion import formulario_donacion_bp
from .login_administrador import login_administrador_bp
from .historial_evento import historial_evento_bp
from .formulario_evento import formulario_evento_bp
from .formulario_inscripcion import formulario_inscripcion_bp
from .administrador import administrador_bp
from .solicitud_donacion import solicitud_donacion_bp

# Registra las rutas en el Blueprint
app_routes.register_blueprint(index_bp)
app_routes.register_blueprint(mostrar_eventos_bp)
app_routes.register_blueprint(formulario_donacion_bp)
app_routes.register_blueprint(login_administrador_bp)
app_routes.register_blueprint(historial_evento_bp)
app_routes.register_blueprint(formulario_evento_bp)
app_routes.register_blueprint(formulario_inscripcion_bp)
app_routes.register_blueprint(administrador_bp)
app_routes.register_blueprint(solicitud_donacion_bp)

@app_routes.context_processor
def utility_processor():
    return dict(b64encode=b64encode)