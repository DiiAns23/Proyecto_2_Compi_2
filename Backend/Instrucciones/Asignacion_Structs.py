from TablaSimbolos.Generador import *
from Abstract.Instruccion import *
from Abstract.Return import *
from Abstract.Tipo import *
from TablaSimbolos.Simbolo import *
from TablaSimbolos.Excepcion import *

class Asignacion_Structs(Instruccion):
    def __init__(self,id, params, exp, fila, colum):
        self.id = id
        self.params = params
        self.exp = exp

        super().__init__(fila, colum)
    
    def compilar(self, tree, table):
        genAux = Generador()
        generator = genAux.getInstance()

        generator.addComment("Compilacion de Cambio de Valor")

        struct = table.getTabla(self.id)

        if struct == None:
            generator.addComment("Fin compilacion de acceso por error")
            return Excepcion("Semantico", "Error no existe la variable '"+str(self.id)+"'", self.fila, self.colum)
         # Temporal para guardar variable
        temp = generator.addTemp()

        # Obtencion de posicion de la variable
        tempPos = struct.pos
        if(not struct.isGlobal):
            tempPos = generator.addTemp()
            generator.addExp(tempPos, 'P', struct.pos, "+")
        generator.getStack(temp, tempPos)

        tmp10 = generator.addTemp()

        generator.getStack(tmp10, tempPos)
        
        value = self.valor.compilar(tree, table)
        if isinstance(value, Excepcion):
            return value
        
        
        