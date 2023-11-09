from flask import Blueprint

producto = Blueprint('productos', __name__)

@producto.route('/productos')
def index():
  return 'productos'