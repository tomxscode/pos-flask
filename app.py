"""APLICACIÓN "POS" EN FLASK
- CARACTERÍSTICAS:
    *
- VERSIÓN ACTUAL: 0.0.0
"""

from flask import Flask

# Hola mundo en Flask

app = Flask(__name__)

@app.route('/')

def index():
    return 'Hola mundo'


if __name__ == '__main__':
    app.run(debug=True)
    