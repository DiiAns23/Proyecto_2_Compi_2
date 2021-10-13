from Abstract.Expression import *
from Abstract.Return import *
from Abstract.Tipo import *
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Generador import *
from Expresiones.Primitivos import *

class Logicas(Expression):

    def __init__(self, left, right, type, fila, colum):
        Expression.__init__(self, fila, colum)
        self.left = left
        self.right = right
        self.type = type
    
    def compilar(self, tree, table):
        genAux = Generador()
        generator = genAux.getInstance()

        # generator.addComment("INICIO EXPRESION LOGICA")
        
        self.checkLabels()
        lblAndOr = ''

        if self.getTipo() == OperadorLogico.AND:
            lblAndOr =  generator.newLabel()

            self.left.setTrueLbl(lblAndOr) 
            self.right.setTrueLbl(self.trueLbl)
            self.left.falseLbl = self.right.falseLbl = self.falseLbl

        elif self.type == OperadorLogico.OR:
            self.left.setTrueLbl(self.trueLbl) 
            self.right.setTrueLbl(self.trueLbl)

            lblAndOr =  generator.newLabel()

            self.left.setFalseLbl(lblAndOr)
            self.right.setFalseLbl(self.falseLbl)
            
        elif self.type == OperadorLogico.NOT:
            self.left.setFalseLbl(self.trueLbl) 
            self.left.setTrueLbl(self.falseLbl)
            lblNot = self.left.compilar( tree, table)

            if self.left.getTipo() != Tipo.BOOL:
                return Excepcion("Semantico", "No se puede utilizar la expresion booleana en: ", self.fila, self.column)
            
            self.setTipo(Tipo.BOOL)
            return lblNot

        left = self.left.compilar( tree, table)
        if left.getTipo() != Tipo.BOOL:
            print("No se puede utilizar en expresion booleana")
            return Excepcion("Semantico", "No se puede utilizar la expresion booleana en: ", self.fila, self.column)

        generator.putLabel(lblAndOr)
        right = self.right.compilar( tree, table)

        if right.getTipo() != Tipo.BOOL:
            return Excepcion("Semantico", "No se puede utilizar la expresion booleana en: ", self.fila, self.column)

        # generator.addComment("FINALIZO EXPRESION LOGICA")
        generator.addSpace()
        ret = Return(None, Tipo.BOOL, False)
        ret.setTrueLbl(self.trueLbl)
        ret.setFalseLbl(self.falseLbl)
        return ret
    
    def checkLabels(self):
        genAux = Generador()
        generator = genAux.getInstance()
        if self.trueLbl == '':
            self.trueLbl = generator.newLabel()
        if self.falseLbl == '':
            self.falseLbl = generator.newLabel()
    
    def getTipo(self):
        return self.type

    def setTipo(self, tipo):
        self.tipo = tipo     
