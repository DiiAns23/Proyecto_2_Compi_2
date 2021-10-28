from Abstract.Expression import *
from Abstract.Return import *
from Abstract.Tipo import *
from TablaSimbolos.Generador import *
class Primitivos(Expression):

    def __init__(self, value, type, line, column):
        Expression.__init__(self, line, column)
        self.value = value
        self.type = type
        self.tipoAux = ''
    
    def compilar(self, tree, table):
        genAux = Generador()
        generator = genAux.getInstance()
        if(self.type == Tipo.INT or self.type == Tipo.FLOAT):
            return Return(str(self.value), self.type, False)
        elif self.type == Tipo.BOOL:
            if self.trueLbl == '':
                self.trueLbl = generator.newLabel()
            if self.falseLbl == '':
                self.falseLbl = generator.newLabel()
            
            if(self.value):
                generator.addGoto(self.trueLbl)
                # generator.addComment("GOTO PARA EVITAR ERROR DE GO")
                generator.addGoto(self.falseLbl)
            else:
                generator.addGoto(self.falseLbl)
                # generator.addComment("GOTO PARA EVITAR ERROR DE GO")
                generator.addGoto(self.trueLbl)
            
            ret = Return(self.value, self.type, False)
            ret.trueLbl = self.trueLbl
            ret.falseLbl = self.falseLbl

            return ret
        elif self.type == Tipo.STRING:
            retTemp = generator.addTemp()
            generator.addAsig(retTemp, 'H')

            for char in str(self.value):
                generator.setHeap('H', ord(char))   # heap[H] = NUM;
                generator.nextHeap()                # H = H + 1;

            generator.setHeap('H', '-1')            # FIN DE CADENA
            generator.nextHeap()

            return Return(retTemp, self.type, True)
        elif self.type == Tipo.CHAR:
            retTemp = generator.addTemp()
            generator.addAsig(retTemp, 'H')
            generator.setHeap('H', ord(self.value))
            generator.nextHeap()

            return Return(retTemp, self.type, True)
        else:
            print('Por hacer')
    
    def getTipo(self):
        return self.type
    def getValue(self):
        return int(self.value)
    def getTipoAux(self):
        return self.tipoAux
    def setValue(self, value):
        self.value = value
    def setTipo(self, tipo):
        self.tipo = tipo
    def setTipoAux(self, tipo):
        self.tipoAux = tipo