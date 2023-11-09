from flask import Blueprint

ventas = Blueprint('ventas', __name__)

@ventas.route('/ventas')
def index():
  return 'Ventas'