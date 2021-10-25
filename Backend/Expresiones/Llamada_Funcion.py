from Abstract.Instruccion import *
from Abstract.Return import *
from Abstract.Tipo import *
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
        genAux = Generador()
        generator = genAux.getInstance()
        if funcion != None:
            generator.addComment(f"Llamada de la Funcion {self.id}")
            paramValues = []
            size = table.size
            for param in self.params:
                paramValues.append(param.compilar(tree,table))
            temp = generator.addTemp()

            generator.addExp(temp,'P', size +1, '+')
            aux = 0
            if len(funcion.getParams()) == len(paramValues):
                for param in paramValues:
                    if funcion.params[aux]['tipo'] == param.getTipo():
                        aux += 1
                        generator.setStack(temp, param.getValue())
                        if aux != len(paramValues):
                            generator.addExp(temp, temp, '1', '+')
                    else:
                        generator.addComment(f'Fin de la llamada a la funcion {self.id} por error, consulte la lista de errores')
                        return Excepcion('Semantico', f'Tipos no coinciden en la llamada de la funcion {self.id}', self.fila, self.colum)
            else:
                generator.addComment(f'Error en la llamada de la funcion {self.id}')
            generator.newEnv(size)
            self.getFuncion(generator)
            generator.callFun(self.id)
            generator.getStack(temp, 'P')
            generator.retEnv(size)
            generator.addComment(f"Fin de la llamada a la funcion {self.id}")
            generator.addSpace()
            return Return(temp, funcion.getTipo(), True)
        generator.addComent(f'Error producido en la llamada a la funcion {self.id} consulte la lista de errores')
        return Excepcion('Semantico',f'No se ha encontrado la funcion {self.id}', self.fila, self.colum)
    
    def getFuncion(self, generator):
        if self.id == 'length':
            generator.fLength()
        elif self.id == 'trunc':
            generator.fTrunc()
        elif self.id == 'float':
            generator.fFloat()
        elif self.id == 'uppercase':
            generator.fUpperCase()
        elif self.id == 'lowercase':
            generator.fLowerCase()
        return