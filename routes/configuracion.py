from flask import Blueprint

configuracion = Blueprint('configuracion', __name__)

@configuracion.route('/configuracion')
def index():
    return 'configuracion'