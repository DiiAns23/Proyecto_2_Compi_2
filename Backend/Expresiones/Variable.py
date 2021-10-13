from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Generador import *
from Abstract.Expression import *
from Abstract.Return import *
from Abstract.Tipo import *

class Variable(Expression):

    def __init__(self, id, line, colum):
        Expression.__init__(self, line, colum)
        self.id = id

    def compilar(self,  tree, table):
        genAux = Generador()
        generator = genAux.getInstance()

        generator.addComment("Compilacion de Acceso")
        
        var = table.getTabla(self.id)

        if(var == None):
            return Excepcion("Semantico", "Error, no existe la variable '"+str(self.id)+"'", self.fila, self.colum)

        # Temporal para guardar variable
        temp = generator.addTemp()

        # Obtencion de posicion de la variable
        tempPos = var.pos
        if(not var.isGlobal):
            tempPos = generator.addTemp()
            generator.addExp(tempPos, 'P', var.pos, "+")
        generator.getStack(temp, tempPos)

        if var.type != Tipo.BOOL:
            generator.addComment("Fin compilacion acceso")
            generator.addSpace()
            return Return(temp, var.type, True)
        if self.trueLbl == '':
            self.trueLbl = generator.newLabel()
        if self.falseLbl == '':
            self.falseLbl = generator.newLabel()
        
        generator.addIf(temp, '1', '==', self.trueLbl)
        generator.addGoto(self.falseLbl)

        generator.addComment("Fin compilacion acceso")
        generator.addSpace()

        ret = Return(None, Tipo.BOOL, False)
        ret.trueLbl = self.trueLbl
        ret.falseLbl = self.falseLbl
        return ret