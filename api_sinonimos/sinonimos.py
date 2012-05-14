from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'Para acceder al api ingresa en la url la palabra que queres buscar, por ejemplo "/hombre"'

@app.route('/sinonimos/<palabra>')
def buscar_sinonimo(palabra):
    return json.dumps({'buscada':palabra, 'sinonimos': sinonimos(palabra)})

@app.route('/antonimos/<palabra>')
def buscar_antonimo(palabra):
    return json.dumps({'buscada':palabra, 'antonimos': antonimos(palabra)})

def antonimos(palabra):
    nuestras_palabras = { 'chau': 'shalom', 'bleh': ['foo', 'bar'] }
    return nuestras_palabras.get(palabra, None)

def sinonimos(palabra):
    nuestras_palabras = { 'hola': 'shalom', 'bleh': ['blah', 'bluh'] }
    return nuestras_palabras.get(palabra, None)

if __name__ == '__main__':
    app.run()
