from flask import Flask, request
from flask.helpers import url_for
from werkzeug.utils import redirect
import json
from flask_cors import CORS
import sys
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Arbol import Arbol
from TablaSimbolos.Tabla_Simbolos import *
from TablaSimbolos.Generador import *
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
    
    genAux = Generador()
    genAux.cleanAll()
    generador = genAux.getInstance()

    instrucciones = Analizar(tmp_val)
    ast = Arbol(instrucciones)
    TsgGlobal = Tabla_Simbolo()
    ast.setTSglobal(TsgGlobal)

    try:
        for instruccion in ast.getInst():
            value = instruccion.compilar(ast, TsgGlobal)
            if isinstance(value, Excepcion):
                ast.setExcepciones(value)
        Excepciones = ast.getExcepciones()
        consola = generador.getCode()
        return json.dumps(consola)
    except:
        print("Error al ejecutar las instrucciones :c")

@app.route('/errores')
def getErrores():
    global Excepciones
    aux = []
    for x in Excepciones:
        aux.append(x.toString2())
    return {'valores': aux}

if __name__ == '__main__':
    app.run(debug = True, port=5200)