from Abstract.Instruccion import *
from Abstract.Return import * 
from Abstract.Tipo import *
from Instrucciones.Funcion import Funcion
from TablaSimbolos.Generador import *
from TablaSimbolos.Excepcion import *
from TablaSimbolos.Tabla_Simbolos import *
from Instrucciones.Declaracion import *

class Float(Funcion):

    def __init__(self, id, params, inst, tipo, fila, colum):
        super().__init__(id, params, inst, tipo, fila, colum)

    def compilar(self, tree, table):
        return
        