from flask import Blueprint

categorias = Blueprint('categorias', __name__)

@categorias.route('/categorias')
def index():
  return 'Página de categorias'