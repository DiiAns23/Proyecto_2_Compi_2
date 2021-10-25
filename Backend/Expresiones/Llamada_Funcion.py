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

class Llamada_Funcion(Instruccion):

    def __init__(self, id, params, fila, colum):
        self.id = id
        self.params = params
        super().__init__(fila, colum)
    
    def compilar(self, tree, table):
        funcion = tree.getFuncion(self.id)
        if funcion != None:
            genAux = Generador()
            generator = genAux.getInstance()
            generator.addComment(f"Llamada de la Funcion {self.id}")
            paramValues = []
            size = table.size

            for param in self.params:
                paramValues.append(param.compilar(tree,table))
            
            temp = generator.addTemp()

            generator.addExp(temp,'P', size +1, '+')
            aux = 0
            for param in paramValues:
                aux += 1
                generator.setStack(temp, param.value)
                if aux != len(paramValues):
                    generator.addExp(temp, temp, '1', '+')
                

            generator.newEnv(size)
            generator.callFun(self.id)
            generator.getStack(temp, 'P')
            generator.retEnv(size)

            generator.addComment(f"Fin de la llamada a la funcion {self.id}")
            generator.addSpace()
            return Return(temp, Tipo.NULO, True)