from flask import Blueprint

index_main = Blueprint('index_main', __name__)

@index_main.route('/')
def index():
    return "Hello World!"