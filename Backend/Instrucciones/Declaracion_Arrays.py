from typing import List
from TablaSimbolos.Generador import *
from Abstract.Instruccion import *
from Abstract.Return import *
from Abstract.Tipo import *
from TablaSimbolos.Simbolo import *
from TablaSimbolos.Excepcion import *

class Declaracion_Arrays(Instruccion):

    def __init__(self, id, fila, colum, values = None, tipoAux = None):
        Instruccion.__init__(self, fila, colum)
        self.id = id
        self.values = values
        self.tipo = Tipo.ARRAY
        self.tipoAux = tipoAux
        self.length = len(self.values)
        self.multiDim = False
        self.isinStruct = False
    
    def compilar(self, tree, table):
        genAux = Generador()
        generator = genAux.getInstance()
        if self.values!= None:
            if isinstance(self.tipoAux, List):
                if self.tipo == self.tipoAux[0]:
                    generator.addComment('Compilacion del Array')
                    t0 = generator.addTemp()
                    t1 = generator.addTemp()
                    generator.addAsig(t0,'H')
                    generator.addExp(t1,t0,'1','+')
                    generator.setHeap('H', len(self.values))
                    apuntador = str(len(self.values)+1)
                    generator.addExp('H','H',apuntador,'+')
                    generator.addSpace()
                    length = 0
                    for value in self.values:
                        if not isinstance(value, Declaracion_Arrays):
                            val = value.compilar(tree,table)
                            try:
                                if val.getTipo() == Tipo.STRUCT:
                                    if [val.getTipo(), val.getTipoAux()] == self.tipoAux[1]:
                                        generator.setHeap(t1,val.getValue())
                                        generator.addExp(t1,t1,'1','+')
                                        generator.addSpace()
                                        length += 1    
                                    else:
                                        return Excepcion("Semantico", "Tipos no coinciden en declaracion o asignacion del array", self.fila, self.colum)    
                                elif val.getTipo() == self.tipoAux[1]:
                                    generator.setHeap(t1,val.getValue())
                                    generator.addExp(t1,t1,'1','+')
                                    generator.addSpace()
                                    length += 1
                                else:
                                    return Excepcion("Semantico", "Tipos no coinciden en declaracion o asignacion del array", self.fila, self.colum)
                            except:
                                return Excepcion("Semantico", "Tipos no coinciden en declaracion o asignacion del array", self.fila, self.colum)
                        else:
                            value.multiDim = True
                            value.tipoAux = self.tipoAux[1]
                            val = value.compilar(tree,table)
                            try:
                                if val.getTipo() == self.tipoAux[1][0]:
                                    generator.setHeap(t1,val.getValue())
                                    generator.addExp(t1,t1,'1','+')
                                    generator.addSpace()
                                    length += 1
                                else:
                                    return Excepcion("Semantico", "Tipos no coinciden en declaracion o asignacion del array", self.fila, self.colum)
                            except:
                                return Excepcion("Semantico", "Tipos no coinciden en declaracion o asignacion del array", self.fila, self.colum)
                    
                    if self.multiDim:
                        return Return(t0, Tipo.ARRAY, True, self.tipoAux[1])
                    if self.isinStruct == False:
                        simbolo = table.setTabla(self.id,self.tipo,True)
                        simbolo.setTipoAux(self.tipoAux[1])
                        simbolo.setLength(length)
                        tempPos = simbolo.pos
                        if not simbolo.isGlobal:
                            tempPos = generator.addTemp()
                            generator.addExp(tempPos, 'P', simbolo.pos, "+")
                        generator.setStack(tempPos, t0)
                        generator.addComment('Fin de la compilacion del Array')
                    else:
                        return Return(t0, Tipo.ARRAY, True, self.tipoAux[1])
            else:
                generator.addComment('Compilacion del Array')
                t0 = generator.addTemp()
                t1 = generator.addTemp()
                generator.addAsig(t0,'H')
                generator.addExp(t1,t0,'1','+')
                generator.setHeap('H', len(self.values))
                apuntador = str(len(self.values)+1)
                generator.addExp('H','H',apuntador,'+')
                generator.addSpace()
                length = 0
                tipoAux = []
                tipoAux.append(Tipo.ARRAY)
                aux = ''
                for value in self.values:
                    if not isinstance(value, Declaracion_Arrays):
                        val = value.compilar(tree,table)
                        aux = val.getTipo()
                        generator.setHeap(t1,val.getValue())
                        generator.addExp(t1,t1,'1','+')
                        generator.addSpace()
                        length += 1
                    else:
                        value.multiDim = True
                        value.tipoAux = value.getTipo()
                        val = value.compilar(tree,table)
                        tipoAux.append(val.getTipoAux())
                        generator.setHeap(t1,val.getValue())
                        generator.addExp(t1,t1,'1','+')
                        generator.addSpace()
                        length += 1
                tipoAux.append(aux)
                if self.multiDim:
                    return Return(t0, Tipo.ARRAY, True, tipoAux)
                if self.isinStruct == False:
                    simbolo = table.setTabla(self.id,self.tipo,True)
                    simbolo.setTipoAux(tipoAux)
                    simbolo.setLength(length)
                    tempPos = simbolo.pos
                    if not simbolo.isGlobal:
                        tempPos = generator.addTemp()
                        generator.addExp(tempPos, 'P', simbolo.pos, "+")
                    generator.setStack(tempPos, t0)
                    generator.addComment('Fin de la compilacion del Array')
                else:
                    return Return(t0, Tipo.ARRAY, True, tipoAux)

    def getTipoAux(self):
        return self.tipoAux
    
    def setTipoAux(self, tipo):
        self.tipoAux = tipo

    def getTipo(self):
        return self.tipo
    def setId(self, id):
        self.id = id
    def getId(self):
        return self.id
    def getLength(self):
        return self.length