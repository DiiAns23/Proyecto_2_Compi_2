from Symbol.Generator import *
from Abstract.Instruccion import *
from Abstract.Return import *
from Abstract.Tipo import *

class Declaracion(Instruccion):

    def __init__(self, id, value, line, column):
        Instruccion.__init__(self, line, column)
        self.id = id
        self.value = value
    
    def compilar(self, environment):
        genAux = Generator()
        generator = genAux.getInstance()

        generator.addComment("Compilacion de valor de variable")
        # Compilacion de valor que estamos asignando
        val = self.value.compilar(environment)

        generator.addComment("Fin de valor de variable")

        # Guardado y obtencion de variable. Esta tiene la posicion, lo que nos sirve para asignarlo en el heap
        newVar = environment.saveVar(self.id, val.type, (val.type == Tipo.STRING or val.type == Tipo.STRUCT))

        # Obtencion de posicion de la variable
        tempPos = newVar.pos
        if(not newVar.isGlobal):
            tempPos = generator.addTemp()
            generator.addExp(tempPos, 'P', newVar.pos, "+")
        
        if(val.type == Tipo.BOOL):
            tempLbl = generator.newLabel()
            
            generator.putLabel(val.trueLbl)
            generator.setStack(tempPos, "1")
            
            generator.addGoto(tempLbl)

            generator.putLabel(val.falseLbl)
            generator.setStack(tempPos, "0")

            generator.putLabel(tempLbl)
        else:
            generator.setStack(tempPos, val.value)
        generator.addSpace()