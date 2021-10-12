from flask import Flask, request
from flask.helpers import url_for
from werkzeug.utils import redirect
import json
from flask_cors import CORS
import sys
from Symbol.Environment import Environment
from Symbol.Generator import Generator
from Analizador_Sintactico import parse as Analizar

sys.setrecursionlimit(10000000)

app = Flask(__name__)
CORS(app)

@app.route('/saludo', methods = ["GET"])
def saludo():
    return "Hola mundo"

@app.route('/prueba', methods = ["POST", "GET"])
def prueba():
    if request.method == "POST":
        entrada = request.data.decode("utf-8")
        entrada = json.loads(entrada)
        global tmp_val
        tmp_val = entrada["codigo"]
        return redirect(url_for("salida"))
    
@app.route('/salida')
def salida():
    global tmp_val
    global Excepciones
    global Tabla
    
    genAux = Generator()
    genAux.cleanAll()
    generador = genAux.getInstance()

    newEnt = Environment(None)
    ast = Analizar(tmp_val)
    try:
        for instruccion in ast:
            instruccion.compilar(newEnt)
        # print(generador.getCode())
        consola = generador.getCode()
        return json.dumps(consola)
    except:
        print("Error al ejecutar las instrucciones :c")

if __name__ == '__main__':
    app.run(debug = True, port=5200)