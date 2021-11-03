import re
from Abstract.Instruccion import Instruccion
from Abstract.Return import Return
from Abstract.Tipo import Tipo
from Expresiones.Aritmeticas import Aritmeticas
from TablaSimbolos.Generador import Generador
from Expresiones.Llamada_Funcion import Llamada_Funcion
from TablaSimbolos.Excepcion import Excepcion

class ReturnE(Instruccion):
    def __init__(self, expresion, fila, colum):
        self.expresion = expresion
        self.tipo = None
        self.valor = None
        self.trueLbl = ''
        self.falseLbl = ''
        
        super().__init__(fila, colum)
    
    def compilar(self, tree, table):
        value = self.expresion.compilar(tree, table)
        if isinstance(value, Excepcion): return value
        self.tipo = value.getTipo()
        self.valor = value.getValue()
        if self.tipo == Tipo.BOOL:
            self.trueLbl = value.getTrueLbl()
            self.falseLbl = value.getFalseLbl()

        return self
        
        
    def getValor(self):
        return self.valor
    def getTipo(self):
        return self.tipo
    def getTrueLbl(self):
        return self.trueLbl
    
    def getFalseLbl(self):
        return self.falseLbl
    
    def setValor(self, valor):
        self.valor = valor
    
    def setTipo(self, tipo):
        self.tipo  = tipo
    
    def setTrueLbl(self, lbl):
        self.trueLbl = lbl
    def setFalseLbl(self, lbl):
        self.falseLbl = lbl