from Abstract.Expression import *
from Abstract.Return import *
from Abstract.Tipo import *
from Abstract.Tipo import *
from Symbol.Generator import Generator
from enum import Enum
import uuid

class Aritmeticas(Expression):
    
    def __init__(self, left, right, type, line, column):
        Expression.__init__(self, line, column)
        self.left = left
        self.right = right
        self.type = type
    
    def compilar(self, env):
        genAux = Generator()
        generator = genAux.getInstance()
        leftValue = self.left.compilar(env)
        rightValue = self.right.compilar(env)

        temp = generator.addTemp()
        op = ''
        if (self.type == OperadorAritmetico.MAS):
            op = '+'
            if leftValue.type == Tipo.INT and rightValue.type == Tipo.INT:
                generator.addExp(temp, leftValue.value, rightValue.value, op)
                return Return(temp, Tipo.INT, True)
            
            if leftValue.type == Tipo.FLOAT and rightValue.type == Tipo.INT:
                generator.addExp(temp, leftValue.value, rightValue.value, op)
                return Return(temp, Tipo.FLOAT, True)
            
            if leftValue.type == Tipo.INT and rightValue.type == Tipo.FLOAT:
                generator.addExp(temp, leftValue.value, rightValue.value, op)
                return Return(temp, Tipo.FLOAT, True)
            
            if leftValue.type == Tipo.FLOAT and rightValue.type == Tipo.FLOAT:
                generator.addExp(temp, leftValue.value, rightValue.value, op)
                return Return(temp, Tipo.FLOAT, True)

            #inserte aqui el return del error
            
        elif(self.type == OperadorAritmetico.MEN):
            op = '-'
            if leftValue.type == Tipo.INT and rightValue.type == Tipo.INT:
                generator.addExp(temp, leftValue.value, rightValue.value, op)
                return Return(temp, Tipo.INT, True)
            
            if leftValue.type == Tipo.FLOAT and rightValue.type == Tipo.INT:
                generator.addExp(temp, leftValue.value, rightValue.value, op)
                return Return(temp, Tipo.FLOAT, True)
            
            if leftValue.type == Tipo.INT and rightValue.type == Tipo.FLOAT:
                generator.addExp(temp, leftValue.value, rightValue.value, op)
                return Return(temp, Tipo.FLOAT, True)
            
            if leftValue.type == Tipo.FLOAT and rightValue.type == Tipo.FLOAT:
                generator.addExp(temp, leftValue.value, rightValue.value, op)
                return Return(temp, Tipo.FLOAT, True)

            #inserte aqui el return del error

        elif(self.type == OperadorAritmetico.POR):
            op = '*'
            if leftValue.type == Tipo.INT and rightValue.type == Tipo.INT:
                generator.addExp(temp, leftValue.value, rightValue.value, op)
                return Return(temp, Tipo.INT, True)
            
            if leftValue.type == Tipo.FLOAT and rightValue.type == Tipo.INT:
                generator.addExp(temp, leftValue.value, rightValue.value, op)
                return Return(temp, Tipo.FLOAT, True)
            
            if leftValue.type == Tipo.INT and rightValue.type == Tipo.FLOAT:
                generator.addExp(temp, leftValue.value, rightValue.value, op)
                return Return(temp, Tipo.FLOAT, True)
            
            if leftValue.type == Tipo.FLOAT and rightValue.type == Tipo.FLOAT:
                generator.addExp(temp, leftValue.value, rightValue.value, op)
                return Return(temp, Tipo.FLOAT, True)

            #Pendiente la concatenacion de strings

            #inserte aqui el return del error

        elif(self.type == OperadorAritmetico.DIV):
            op = '/'   
            label = generator.newLabel()
            generator.addIf(rightValue.value, "0", "!=",label) 
            error = "Math Error \n"
            for char in error:
                generator.addPrint("c",ord(char))
            tmp2 = generator.addTemp()
            generator.addExp(tmp2,"0","","")
            label2 = generator.newLabel()
            generator.addGoto(label2)
            generator.putLabel(label)
            generator.addExp(temp, leftValue.value, rightValue.value, op)
            generator.putLabel(label2)
            return Return(temp, Tipo.FLOAT, True)
        
        elif (self.type == OperadorAritmetico.POT):
            op = "*"

            
        return Return(temp, Tipo.INT, True)