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
            for value in self.values:
                val = value.compilar(tree,table)
                generator.setHeap(t1,val.getValue())
                generator.addExp(t1,t1,'1','+')
                generator.addSpace()
            generator.addComment('Fin de la compilacion del Array')

