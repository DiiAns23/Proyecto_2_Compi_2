from Abstract.Expression import *
from Abstract.Return import *
from Abstract.Tipo import *
from Abstract.Tipo import *
from TablaSimbolos.Generador import *
from TablaSimbolos.Excepcion import *

class Aritmeticas(Expression):
    
    def __init__(self, left, right, tipo, fila, colum):
        self.left = left
        self.right = right
        self.type = tipo
        self.fila = fila
        self.colum = colum
    
    def compilar(self, tree, table):
        genAux = Generador()
        generator = genAux.getInstance()
        leftValue = self.left.compilar(tree, table)

        rightValue = self.right.compilar(tree, table)

        temp = generator.addTemp()
        op = ''
        if (self.getTipo() == OperadorAritmetico.MAS):
            op = '+'
            if leftValue.getTipo() == Tipo.INT and rightValue.getTipo() == Tipo.INT:
                generator.addExp(temp, leftValue.getValue(), rightValue.getValue(), op)
                return Return(temp, Tipo.INT, True)
            
            if leftValue.getTipo() == Tipo.FLOAT and rightValue.getTipo() == Tipo.INT:
                generator.addExp(temp, leftValue.getValue(), rightValue.getValue(), op)
                return Return(temp, Tipo.FLOAT, True)
            
            if leftValue.getTipo() == Tipo.INT and rightValue.getTipo() == Tipo.FLOAT:
                generator.addExp(temp, leftValue.getValue(), rightValue.getValue(), op)
                return Return(temp, Tipo.FLOAT, True)
            
            if leftValue.getTipo() == Tipo.FLOAT and rightValue.getTipo() == Tipo.FLOAT:
                generator.addExp(temp, leftValue.getValue(), rightValue.getValue(), op)
                return Return(temp, Tipo.FLOAT, True)

            return Excepcion("Semantico", "Operacion 'Suma' no permitida en: ", self.fila, self.colum)
            
        elif(self.getTipo() == OperadorAritmetico.MEN):
            op = '-'
            if leftValue.getTipo() == Tipo.INT and rightValue.getTipo() == Tipo.INT:
                generator.addExp(temp, leftValue.getValue(), rightValue.getValue(), op)
                return Return(temp, Tipo.INT, True)
            
            if leftValue.getTipo() == Tipo.FLOAT and rightValue.getTipo() == Tipo.INT:
                generator.addExp(temp, leftValue.getValue(), rightValue.getValue(), op)
                return Return(temp, Tipo.FLOAT, True)
            
            if leftValue.getTipo() == Tipo.INT and rightValue.getTipo() == Tipo.FLOAT:
                generator.addExp(temp, leftValue.getValue(), rightValue.getValue(), op)
                return Return(temp, Tipo.FLOAT, True)
            
            if leftValue.getTipo() == Tipo.FLOAT and rightValue.getTipo() == Tipo.FLOAT:
                generator.addExp(temp, leftValue.getValue(), rightValue.getValue(), op)
                return Return(temp, Tipo.FLOAT, True)

            return Excepcion("Semantico", "Operacion 'Resta' no permitida en: ", self.fila, self.column)

        elif(self.getTipo() == OperadorAritmetico.POR):
            op = '*'
            if leftValue.getTipo() == Tipo.INT and rightValue.getTipo() == Tipo.INT:
                generator.addExp(temp, leftValue.getValue(), rightValue.getValue(), op)
                return Return(temp, Tipo.INT, True)
            
            if leftValue.getTipo() == Tipo.FLOAT and rightValue.getTipo() == Tipo.INT:
                generator.addExp(temp, leftValue.getValue(), rightValue.getValue(), op)
                return Return(temp, Tipo.FLOAT, True)
            
            if leftValue.getTipo() == Tipo.INT and rightValue.getTipo() == Tipo.FLOAT:
                generator.addExp(temp, leftValue.getValue(), rightValue.getValue(), op)
                return Return(temp, Tipo.FLOAT, True)
            
            if leftValue.getTipo() == Tipo.FLOAT and rightValue.getTipo() == Tipo.FLOAT:
                generator.addExp(temp, leftValue.getValue(), rightValue.getValue(), op)
                return Return(temp, Tipo.FLOAT, True)

            #Pendiente la concatenacion de strings

            return Excepcion("Semantico", "Operacion 'Multiplicacion' no permitida en: ", self.fila, self.column)

        elif(self.getTipo() == OperadorAritmetico.DIV):
            op = '/' 
            bandera = False
            if leftValue.getTipo() == Tipo.INT and rightValue.getTipo() == Tipo.INT:
                bandera = True
            if leftValue.getTipo() == Tipo.FLOAT and rightValue.getTipo() == Tipo.INT:
                bandera = True
            if leftValue.getTipo() == Tipo.INT and rightValue.getTipo() == Tipo.FLOAT:
                bandera = True
            if leftValue.getTipo() == Tipo.FLOAT and rightValue.getTipo() == Tipo.FLOAT:
                bandera = True
            if bandera:
                label = generator.newLabel()
                generator.addIf(rightValue.getValue(), "0", "!=",label) 
                error = "Math Error \n"
                for char in error:
                    generator.addPrint("c",ord(char))
                tmp2 = generator.addTemp()
                generator.addExp(tmp2,"0","","")
                label2 = generator.newLabel()
                generator.addGoto(label2)
                generator.putLabel(label)
                generator.addExp(temp, leftValue.getValue(), rightValue.getValue(), op)
                generator.putLabel(label2)
                return Return(temp, Tipo.FLOAT, True)
            return Excepcion("Semantico", "Operacion 'Division' no permitida en: ", self.fila, self.column)


        elif (self.getTipo() == OperadorAritmetico.POT):
            op = "*"

        return Return(temp, Tipo.INT, True)

    def getTipo(self):
        return self.type

    def setTipo(self, tipo):
        self.tipo = tipo