from TablaSimbolos.Generador import *
from Abstract.Instruccion import *
from Abstract.Return import *
from Abstract.Tipo import *
from TablaSimbolos.Simbolo import *
from TablaSimbolos.Excepcion import *

class Asignacion_Arrays(Instruccion):
    def __init__(self, ide, indices, valor,fila, colum):
        self.id = ide
        self.indices = indices
        self.valor = valor
        super().__init__(fila, colum)
    
    def compilar(self, tree, table):
        genAux = Generador()
        generator = genAux.getInstance()

        generator.addComment("Compilacion de Cambio de Valor")
        
        var = table.getTabla(self.id)

        if(var == None):
            generator.addComment("Fin Compilacion de Cambio de Valor por error")
            return Excepcion("Semantico", "Error no existe la variable '"+str(self.id)+"'", self.fila, self.colum)

        # Temporal para guardar variable
        temp = generator.addTemp()

        # Obtencion de posicion de la variable
        tempPos = var.getPos()
        if(not var.isGlobal):
            tempPos = generator.addTemp()
            generator.addExp(tempPos, 'P', var.getPos(), "+")
        
        tmp10 = generator.addTemp()

        generator.getStack(tmp10, tempPos)
        
        value = self.valor.compilar(tree, table)
        if isinstance(value, Excepcion):
            return value

        indice = self.indices[0].compilar(tree,table)
        if isinstance(indice, Excepcion):
            return indice

        tmp4 = generator.addTemp()
        Lbl1 = generator.newLabel()
        Lbl2 = generator.newLabel()
        Lbl3 = generator.newLabel()

        generator.addExp(temp, tmp10, indice.getValue(),'+')
        generator.addIf(indice.getValue(),'1','<',Lbl1)
        generator.getHeap(tmp4, tmp10)
        generator.addIf(indice.getValue(),tmp4,'>', Lbl1)
        generator.addGoto(Lbl2)
        generator.putLabel(Lbl1)
        error = "Bounds Error \n"
        for char in error:
            generator.addPrint("c",ord(char))
        generator.addGoto(Lbl3)
        generator.putLabel(Lbl2)
        
        generator.setHeap(temp, value.getValue())
        generator.addGoto(Lbl3)
        generator.putLabel(Lbl3)

        
        generator.addComment('Fin de compilacion de Cambio de Valor')
        generator.addSpace()

