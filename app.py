from flask import Flask

# Rutas
from routes.usuarios import usuarios
from routes.main import index_main
from routes.configuracion import configuracion
from routes.productos import producto
from routes.categorias import categorias
from routes.ventas import ventas

app = Flask(__name__)

app.register_blueprint(usuarios)
app.register_blueprint(index_main)
app.register_blueprint(configuracion)
app.register_blueprint(categorias)
app.register_blueprint(ventas)
app.register_blueprint(producto)