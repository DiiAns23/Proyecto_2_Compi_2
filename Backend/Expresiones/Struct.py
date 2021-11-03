from typing import List
from Expresiones.Array import Array
from Expresiones.Variable import Variable
from Instrucciones.Declaracion_Arrays import Declaracion_Arrays
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Generador import *
from Abstract.Expression import *
from Abstract.Return import *
from Abstract.Tipo import *

class Struct(Expression):

    def __init__(self,id, parametros, fila, colum):
        super().__init__(fila, colum)
        self.id = id
        self.params = parametros
        self.tipo = Tipo.STRUCT
        self.referencia = False
    
    def compilar(self, tree, table):
        genAux = Generador()
        generator = genAux.getInstance()

        generator.addComment(f"Compilacion de Acceso de la variable {self.id}")

        struct = table.getTabla(self.id)

        if struct == None:
            generator.addComment("Fin compilacion de acceso por error")
            return Excepcion("Semantico", "Error no existe la variable '"+str(self.id)+"'", self.fila, self.colum)
        posiciones = []
        for param in self.params:
            x = 0
            if isinstance(param, Variable):
                aux = param.id
            if isinstance(param, Array):
                print("Por hacer")
            if isinstance(param, Struct):
                print("Por hacer ")
            for structParam in struct.getParams():
                x = 0
                if aux in structParam['ide']:
                    posiciones.append(x)
                    print("Si existe :3")
                x += 1
        
        print(self.id)
        print(str(self.params))
        return Return("Nombreee", Tipo.STRING, False)