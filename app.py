from flask import Flask
from routes.usuarios import usuarios

app = Flask(__name__)

app.register_blueprint(usuarios)