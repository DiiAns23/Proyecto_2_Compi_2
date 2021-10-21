from Abstract.Instruccion import *
from Abstract.Return import *
from Abstract.Tipo import *
from Instrucciones.Break import Break
from Instrucciones.Continue import Continue
from Expresiones.Variable import Variable
from Expresiones.Array import Array
from Expresiones.Primitivos import Primitivos
from TablaSimbolos.Generador import *
from TablaSimbolos.Excepcion import *
from TablaSimbolos.Tabla_Simbolos import *
from Instrucciones.Declaracion import *

class Funcion(Instruccion):

    def __init__(self,id, params, inst, fila, colum):
        self.id = id
        self.params = params
        self.inst = inst
        self.tipo = Tipo.NULO
        super().__init__(fila, colum)

    def compilar(self, tree, table):
        funcion = tree.setFunciones(self.id)
        
        if funcion == "error":
            error = Excepcion("Semantico", f"Funcion {self.id} ya existe", self.fila, self.colum)
            tree.setExcepciones(error)
        
        genAux = Generador()
        generator = genAux.getInstance()
        generator.addComment(f"Compilacion de la Funcion {self.id}")
        entorno = Tabla_Simbolo(table)

        Lblreturn = generator.newLabel()
        entorno.returnLbl = Lblreturn
        entorno.size = 1
        for param in self.params:
            entorno.setTabla(param["ide"], param["tipo"], (param["tipo"] == Tipo.STRING or param["tipo"] == Tipo.STRUCT or param["tipo"] == Tipo.ARRAY))
        generator.addBeginFunc(self.id)

        for ins in self.inst:
            value = ins.compilar(tree, entorno)
            if isinstance(value, Excepcion):
                tree.setExcepciones(value)
            if isinstance(value, Break):
                error = Excepcion("Semantico", "Breack fuera de ciclo", ins.fila, ins.colum)
                tree.setExcepciones(error)
        
        generator.putLabel(Lblreturn)

        generator.addComment(f"Fin de la Compilacion de la Funcion {self.id}")
        generator.addEndFunc()
        generator.addSpace()

        return None