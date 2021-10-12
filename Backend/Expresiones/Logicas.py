from Abstract.Expression import *
from Abstract.Return import *
from Abstract.Tipo import *
from Symbol.Generator import Generator
from Expresiones.Primitivos import *

class Logicas(Expression):

    def __init__(self, left, right, type, line, column):
        Expression.__init__(self, line, column)
        self.left = left
        self.right = right
        self.type = type
    
    def compilar(self, environment):
        genAux = Generator()
        generator = genAux.getInstance()

        # generator.addComment("INICIO EXPRESION LOGICA")
        
        self.checkLabels()
        lblAndOr = ''

        if self.type == OperadorLogico.AND:
            lblAndOr = self.left.trueLbl = generator.newLabel()
            self.right.trueLbl = self.trueLbl
            self.left.falseLbl = self.right.falseLbl = self.falseLbl

        elif self.type == OperadorLogico.OR:
            self.left.trueLbl = self.right.trueLbl = self.trueLbl
            lblAndOr = self.left.falseLbl = generator.newLabel()
            self.right.falseLbl = self.falseLbl
            
        elif self.type == OperadorLogico.NOT:
            print("No me sale :c")

        left = self.left.compilar(environment)
        if left.type != Tipo.BOOL:
            print("No se puede utilizar en expresion booleana")
            return

        generator.putLabel(lblAndOr)
        right = self.right.compilar(environment)

        if right.type != Tipo.BOOL:
            print("No se puede utilizar en expresion booleana")
            return

        # generator.addComment("FINALIZO EXPRESION LOGICA")
        generator.addSpace()
        ret = Return(None, Tipo.BOOL, False)
        ret.trueLbl = self.trueLbl
        ret.falseLbl = self.falseLbl
        return ret
        




    
    def checkLabels(self):
        genAux = Generator()
        generator = genAux.getInstance()
        if self.trueLbl == '':
            self.trueLbl = generator.newLabel()
        if self.falseLbl == '':
            self.falseLbl = generator.newLabel()
    
            
