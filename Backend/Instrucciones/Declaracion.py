from TablaSimbolos.Generador import *
from Abstract.Instruccion import *
from Abstract.Return import *
from Abstract.Tipo import *
from TablaSimbolos.Simbolo import *
from TablaSimbolos.Excepcion import *

class Declaracion(Instruccion):

    def __init__(self, id, tipo, fila, colum, value = None):
        Instruccion.__init__(self, fila, colum)
        self.id = id
        self.value = value
        self.tipo = tipo
        self.find = True
    
    def compilar(self,  tree, table):
        genAux = Generador()
        generator = genAux.getInstance()
        if self.value != None:
            if self.tipo != None:
                generator.addComment("Compilacion de valor de variable")
                # Compilacion de valor que estamos asignando
                
                val = self.value.compilar( tree, table)

                if isinstance(val, Excepcion): return val

                if val.type != self.tipo:
                    generator.addComment("Se ha creado un error en la creacion de la variable")
                    return Excepcion("Semantico", "Error de tipos", self.fila, self.colum)
                # Guardado y obtencion de variable. Esta tiene la posicion, lo que nos sirve para asignarlo en el heap
                simbolo = table.setTabla(self.id, val.type, (val.type == Tipo.STRING or val.type == Tipo.STRUCT))
                
                if simbolo == "update":
                    simbolo = table.updateTabla(self.id, val.type,((val.type == Tipo.STRING or val.type == Tipo.STRUCT)))

                # Obtencion de posicion de la variable
                tempPos = simbolo.pos
                if(not simbolo.isGlobal):
                    tempPos = generator.addTemp()
                    generator.addExp(tempPos, 'P', simbolo.pos, "+")
                
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
                generator.addComment("Fin de valor de variable")
                generator.addSpace()
            else:
                generator.addComment("Compilacion de valor de variable")
                # Compilacion de valor que estamos asignando
                val = self.value.compilar(tree, table)
                if isinstance(val, Excepcion): return val
                # Guardado y obtencion de variable. Esta tiene la posicion, lo que nos sirve para asignarlo en el heap
                simbolo = table.setTabla(self.id, val.type, (val.type == Tipo.STRING or val.type == Tipo.STRUCT), self.find)

                # Obtencion de posicion de la variable
                tempPos = simbolo.pos
                if(not simbolo.isGlobal):
                    tempPos = generator.addTemp()
                    generator.addExp(tempPos, 'P', simbolo.pos, "+")
                
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
                generator.addComment("Fin de valor de variable")
                generator.addSpace()
        else:
            generator.addComment("Compilacion de valor de variable")
            value = "nothing"
            generator.addComment("Fin de valor de variable")
            simbolo = table.setTabla(self.id, Tipo.NULO, True)

