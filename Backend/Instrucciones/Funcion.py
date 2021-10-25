from Abstract.Instruccion import *
from Abstract.Return import *
from Abstract.Tipo import *
from Instrucciones.Return import ReturnE
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

    def __init__(self,id, params, inst, tipo, fila, colum):
        self.id = id
        self.params = params
        self.inst = inst
        self.tipo = tipo
        self.recTemps = True
        super().__init__(fila, colum)

    def compilar(self, tree, table):
        funcion = tree.setFunciones(self.id, self)
        
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
            if isinstance(value, ReturnE):
                if value.getTipo() == self.getTipo():
                    generator.addComment('Resultado a retornar en la funcion')
                    generator.setStack('P',value.getValor())
                    generator.addGoto(Lblreturn)
                    generator.addComment('Fin del resultado a retornar')
                else:
                    generator.addComment('Error en la instruccion Return, consule la lista de errores')
                    error = Excepcion('Semantico','El tipo en el return no coincide con el tipo de la funcion', value.fila, value.colum)
                    tree.setExcepciones(error)

        generator.addGoto(Lblreturn)
        generator.putLabel(Lblreturn)

        generator.addComment(f"Fin de la Compilacion de la Funcion {self.id}")
        generator.addEndFunc()
        generator.addSpace()

        return
    
    def getParams(self):
        return self.params
    
    def getTipo(self):
        return self.tipo
    