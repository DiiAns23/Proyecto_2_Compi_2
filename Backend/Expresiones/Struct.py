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

        nombre = self.id
        temp = generator.addTemp()
        tmp2 = generator.addTemp()
        tmp = generator.addTemp()
        tipo = ''
        aux = ''

        struct = table.getTabla(nombre)
        if struct == None:
            generator.addComment("Fin compilacion de acceso por error")
            return Excepcion("Semantico", "Error no existe la variable '"+str(self.id)+"'", self.fila, self.colum)
        # Temporal para guardar variable

        # Obtencion de posicion de la variable
        tempPos = struct.pos
        if(not struct.isGlobal):
            tempPos = generator.addTemp()
            generator.addExp(tempPos, 'P', struct.pos, "+")
        generator.getStack(temp, tempPos)
        
        y = 0
        x = 0           #Debo de componer el acceso a los structs, tienen problema de enciclado
        while True:
            param = self.params[0]
            if isinstance(param, Variable):
                aux = param.id
                for structParam in struct.getParams():
                    if aux in structParam['ide']:
                        tipo = structParam['tipo']
                        generator.addExp(tmp2, temp, x,'+')
                        generator.getHeap(tmp,tmp2)
                        break
                    x += 1
            if isinstance(param, Array):
                indice = param.indice[0].compilar(tree, table)
                if isinstance(indice, Excepcion): return indice
                aux = param.id
                for structParam in struct.getParams():
                    if aux in structParam['ide']:
                        tipo = structParam['tipo'][1]
                        generator.addExp(tmp2, temp, x, '+')
                        tmp3 = generator.addTemp()
                        generator.getHeap(tmp3, tmp2)
                        generator.addExp(tmp3, tmp3, indice.getValue(), '+')
                        generator.getHeap(tmp, tmp3)
                        break
                    x += 1
                    
            if isinstance(param, Struct):
                aux = param.id
                for structParam in struct.getParams():
                    if aux in structParam['ide']:
                        tipo = structParam['tipo']
                        generator.addExp(tmp2, temp, x,'+')
                        generator.getHeap(tmp,tmp2)
                        break
                    x += 1
                struct = tree.getStruct(tipo[1])
                self.params = [param.params[0]]
                nombre = aux
                temp = tmp
                continue
            y += 1
            if y < len(self.params):
                temp = tmp
            else:
                break
        
        return Return(tmp, tipo, True)