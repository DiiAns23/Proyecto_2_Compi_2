from types import GenericAlias
from Abstract.Expression import *
from Abstract.Return import *
from Abstract.Tipo import *
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Generador import *

class Relacionales(Expression):
    def __init__(self,left, right, tipo, line, column):
        super().__init__(line, column)
        self.left = left
        self.right = right
        self.type = tipo
    
    def compilar(self, tree, table):
        genAux = Generador()
        generador = genAux.getInstance()

        generador.addComment("Inicio de la expresion relacional")
        
        left = self.left.compilar(tree, table)
        right = None
        result = Return(None, Tipo.BOOL, False)

        if left.getTipo() != Tipo.BOOL:
            right = self.right.compilar(tree, table)
            if (left.getTipo() == Tipo.INT or left.getTipo() == Tipo.FLOAT) and (right.getTipo() == Tipo.INT or right.getTipo() == Tipo.FLOAT):
                self.checkLabels()
                generador.addIf(left.getValue(), right.getValue(), self.getOp(), self.getTrueLbl())
                generador.addGoto(self.getFalseLbl())
            
            elif left.type == Tipo.STRING and right.type == Tipo.STRING:
                generador.fcompareString()
                paramTemp = generador.addTemp()
                
                generador.addExp(paramTemp, 'P', table.size, '+')
                generador.addExp(paramTemp, paramTemp, '1', '+')
                generador.setStack(paramTemp, left.getValue())

                generador.addExp(paramTemp, paramTemp, '1', '+')
                generador.setStack(paramTemp, right.getValue())
                
                generador.newEnv(table.size)
                generador.callFun('compareString')

                temp = generador.addTemp()
                generador.getStack(temp, 'P')
                generador.retEnv(table.size)
                
                
                self.checkLabels()
                generador.addIf(temp,self.getNum(), "==", self.trueLbl)
                generador.addGoto(self.falseLbl)
                
                result.trueLbl = self.trueLbl
                result.falseLbl = self.falseLbl

                return result 

        else:
            gotoR = generador.newLabel()
            leftTmp  = generador.addTemp()

            generador.putLabel(left.getTrueLbl())
            generador.addExp(leftTmp, '1', '','')
            generador.addGoto(gotoR)

            generador.putLabel(left.getFalseLbl())
            generador.addExp(leftTmp, '0', '','')

            generador.putLabel(gotoR)
            
            right = self.right.compile(tree, table)
            if right.type != Tipo.BOOL:
                print("Error, no se pueden comparar")
                return Excepcion("Semantico","No se pueden comparar", self.fila, self.colum)
            
            gotoEnd = generador.newLabel()
            rightTemp = generador.addTemp()

            generador.putLabel(right.trueLbl)
            
            generador.addExp(rightTemp, '1', '', '')
            generador.addGoto(gotoEnd)

            generador.putLabel(right.getFalseLbl())
            generador.addExp(rightTemp, '0', '', '')

            generador.putLabel(gotoEnd)

            self.checkLabels()
            generador.addIf(leftTmp, rightTemp, self.getOp(), self.trueLbl)
            generador.addGoto(self.falseLbl)
            
        generador.addComment("FIN DE EXPRESION RELACIONAL")
        generador.addSpace()
        result.trueLbl = self.trueLbl
        result.falseLbl = self.falseLbl

        return result              
            
    def checkLabels(self):
        genAux = Generador()
        generador = genAux.getInstance()
        if self.trueLbl == '':
            self.trueLbl = generador.newLabel()
        if self.falseLbl == '':
            self.falseLbl = generador.newLabel()

    def getOp(self):
        if self.type == OperadorRelacional.MAYOR:
            return '>'
        elif self.type == OperadorRelacional.MENOR:
            return '<'
        elif self.type == OperadorRelacional.MENORI:
            return '<='
        elif self.type == OperadorRelacional.MAYORI:
            return '>='
        elif self.type == OperadorRelacional.IGUALDAD:
            return '=='
        elif self.type == OperadorRelacional.DIFERENTE:
            return '!='

    def getNum(self):
        if self.type == OperadorRelacional.IGUALDAD:
            return '1'
        if self.type == OperadorRelacional.DIFERENTE:
            return '0'