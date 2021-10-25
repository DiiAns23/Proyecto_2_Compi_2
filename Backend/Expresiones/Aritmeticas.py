from Abstract.Expression import *
from Abstract.Return import *
from Abstract.Tipo import *
from Abstract.Tipo import *
from Expresiones.Llamada_Funcion import Llamada_Funcion
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
        temp = ''
        op = ''
        leftValue = ''
        rightValue = ''
        if self.left != None:
            leftValue = self.left.compilar(tree, table)
            
        if self.right != None:
            if isinstance(self.right, Llamada_Funcion):
                self.right.guardarTemps(generator, table, [leftValue.getValue()])
                rightValue = self.right.compilar(tree, table)
                self.right.recuperarTemps(generator, table, [leftValue.getValue()])
            else:
                rightValue = self.right.compilar(tree, table)

        if (self.getTipo() == OperadorAritmetico.UME):
            op = '-'
            temp = generator.addTemp()
            if rightValue.getTipo() == Tipo.INT:
                generator.addExp(temp, 0, rightValue.getValue(), op)
                return Return(temp, Tipo.INT, True)
            
            if rightValue.getTipo() == Tipo.FLOAT:
                generator.addExp(temp, 0, rightValue.getValue(), op)
                return Return(temp, Tipo.FLOAT, True)

            return Excepcion("Semantico", "Operacion 'Resta' no permitida en: ", self.fila, self.column)          


        elif (self.getTipo() == OperadorAritmetico.MAS):
            op = '+'
            temp = generator.addTemp()
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
            temp = generator.addTemp()
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
                temp = generator.addTemp()
                generator.addExp(temp, leftValue.getValue(), rightValue.getValue(), op)
                return Return(temp, Tipo.INT, True)
            
            if leftValue.getTipo() == Tipo.FLOAT and rightValue.getTipo() == Tipo.INT:
                temp = generator.addTemp()
                generator.addExp(temp, leftValue.getValue(), rightValue.getValue(), op)
                return Return(temp, Tipo.FLOAT, True)
            
            if leftValue.getTipo() == Tipo.INT and rightValue.getTipo() == Tipo.FLOAT:
                temp = generator.addTemp()
                generator.addExp(temp, leftValue.getValue(), rightValue.getValue(), op)
                return Return(temp, Tipo.FLOAT, True)
            
            if leftValue.getTipo() == Tipo.FLOAT and rightValue.getTipo() == Tipo.FLOAT:
                temp = generator.addTemp()
                generator.addExp(temp, leftValue.getValue(), rightValue.getValue(), op)
                return Return(temp, Tipo.FLOAT, True)

            if leftValue.getTipo() == Tipo.STRING and rightValue.getTipo() == Tipo.STRING:
                generator.fconcatString()
                t8 = generator.addTemp()
                t9 = generator.addTemp()

                generator.addExp(t8, 'P', table.size,'+' )
                generator.addExp(t8, t8, '1', '+')

                generator.setStack(t8, leftValue.getValue())
                generator.addExp(t8,t8,'1','+')
                generator.setStack(t8, rightValue.getValue())

                generator.newEnv(table.size)
                generator.callFun('concatString')
                generator.getStack(t9, 'P')
                generator.retEnv(table.size)

                return Return(t9, Tipo.STRING, False)

            return Excepcion("Semantico", "Operacion 'Multiplicacion' no permitida en: ", self.fila, self.column)

        elif(self.getTipo() == OperadorAritmetico.DIV):
            op = '/' 
            temp = generator.addTemp()
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
            tipo = ''
            if leftValue.getTipo() == Tipo.INT and rightValue.getTipo() == Tipo.INT:
                tipo = Tipo.INT
            elif leftValue.getTipo() == Tipo.FLOAT and rightValue.getTipo() == Tipo.INT:
                tipo = Tipo.FLOAT
            elif leftValue.getTipo() == Tipo.STRING and rightValue.getTipo() == Tipo.INT:
                tipo = Tipo.STRING
            else:
                return Excepcion("Semantico","Operacion 'Potencia' no permitida en ", self.fila, self.colum)

            temp = generator.addTemp()
            generator.fPotencia()

            t5 = generator.addTemp()

            generator.addExp(t5, 'P', table.size,'+')
            generator.addExp(t5,t5,'1','+')

            generator.setStack(t5, leftValue.getValue())
            generator.addExp(t5, t5,'1','+')
            generator.setStack(t5, rightValue.getValue())

            generator.newEnv(table.size)
            generator.callFun('potencia')

            generator.getStack(temp, 'P')

            generator.retEnv(table.size)

            return Return(temp, tipo, True)
        
        elif self.getTipo() == OperadorAritmetico.MOD:
            tipo = ''
            if leftValue.getTipo() == Tipo.INT and rightValue.getTipo() == Tipo.INT:
                tipo = Tipo.INT
            elif leftValue.getTipo() == Tipo.INT and rightValue.getTipo() == Tipo.FLOAT:
                tipo = Tipo.FLOAT
            elif leftValue.getTipo() == Tipo.FLOAT and rightValue.getTipo() == Tipo.INT:
                tipo = Tipo.FLOAT
            elif leftValue.getTipo() == Tipo.FLOAT and rightValue.getTipo() == Tipo.FLOAT:
                tipo = Tipo.FLOAT
            else:
                return Excepcion("Semantico","Operacion 'Modulo' no permitida en ", self.fila, self.colum)
            temp = generator.addTemp()
            generator.setImport('math')
            generator.addModulo(temp, leftValue.getValue(), rightValue.getValue())
            return Return(temp, tipo, True)

    def getTipo(self):
        return self.type

    def setTipo(self, tipo):
        self.tipo = tipo