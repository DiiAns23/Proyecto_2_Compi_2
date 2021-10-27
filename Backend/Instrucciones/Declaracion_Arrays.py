from TablaSimbolos.Generador import *
from Abstract.Instruccion import *
from Abstract.Return import *
from Abstract.Tipo import *
from TablaSimbolos.Simbolo import *
from TablaSimbolos.Excepcion import *

class Declaracion_Arrays(Instruccion):

    def __init__(self, id, fila, colum, values = None):
        Instruccion.__init__(self, fila, colum)
        self.id = id
        self.values = values
        self.tipo = Tipo.ARRAY
        self.length = len(self.values)
        self.multiDim = False
    
    def compilar(self, tree, table):
        genAux = Generador()
        generator = genAux.getInstance()
        if self.values!= None:
            generator.addComment('Compilacion del Array')
            t0 = generator.addTemp()
            t1 = generator.addTemp()
            generator.addAsig(t0,'H')
            generator.addExp(t1,t0,'1','+')
            generator.setHeap('H', len(self.values))
            apuntador = str(len(self.values)+1)
            generator.addExp('H','H',apuntador,'+')
            generator.addSpace()
            tipo = ''
            length = 0
            for value in self.values:
                if not isinstance(value, Declaracion_Arrays):
                    val = value.compilar(tree,table)
                    tipo = val.getTipo()
                    generator.setHeap(t1,val.getValue())
                    generator.addExp(t1,t1,'1','+')
                    generator.addSpace()
                    length += 1
                else:
                    value.multiDim = True
                    val = value.compilar(tree,table)
                    generator.setHeap(t1,val.getValue())
                    generator.addExp(t1,t1,'1','+')
                    generator.addSpace()
                    length += 1
            if self.multiDim:
                return Return(t0, Tipo.ARRAY, True)
            simbolo = table.setTabla(self.id,self.tipo,True)
            simbolo.setTipoAux(tipo)
            simbolo.setLength(length)
            tempPos = simbolo.pos
            if(not simbolo.isGlobal):
                tempPos = generator.addTemp()
                generator.addExp(tempPos, 'P', simbolo.pos, "+")
            generator.setStack(tempPos, t0)
            generator.addComment('Fin de la compilacion del Array')
            


    def getTipo(self):
        return self.tipo
    def setId(self, id):
        self.id = id
    def getId(self):
        return self.id
    def getLength(self):
        return self.length