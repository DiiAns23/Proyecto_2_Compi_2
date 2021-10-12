from Abstract.Instruccion import *
from Abstract.Return import *
from Abstract.Tipo import *
from Symbol.Generator import Generator

class Imprimir(Instruccion):

    def __init__(self,value, line, column, newLine = False):
        super().__init__(line, column)
        self.value = value
        self.newLine = newLine
    
    def compilar(self, env):
        for valor in self.value:
            val = valor.compilar(env)
            genAux = Generator()
            generator = genAux.getInstance()

            if(val.type == Tipo.INT):
                generator.addPrint("d", val.value)
            elif val.type == Tipo.FLOAT:
                generator.printFloat("f", val.value)
            elif val.type == Tipo.BOOL:
                
                tempLbl = generator.newLabel()
                
                generator.putLabel(val.trueLbl)
                generator.printTrue()
                
                generator.addGoto(tempLbl)
                
                generator.putLabel(val.falseLbl)
                generator.printFalse()

                generator.putLabel(tempLbl)
            elif val.type == Tipo.STRING:
                generator.fPrintString()

                paramTemp = generator.addTemp()
                
                generator.addExp(paramTemp, 'P', env.size, '+')
                generator.addExp(paramTemp, paramTemp, '1', '+')
                generator.setStack(paramTemp, val.value)
                
                generator.newEnv(env.size)
                generator.callFun('printString')

                temp = generator.addTemp()
                generator.getStack(temp, 'P')
                generator.retEnv(env.size)
            else:
                print("POR HACER")
            
            if self.newLine:
                generator.addPrint("c", 10)