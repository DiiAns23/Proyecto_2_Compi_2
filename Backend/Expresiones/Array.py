from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Generador import *
from Abstract.Expression import *
from Abstract.Return import *
from Abstract.Tipo import *

class Array(Expression):

    def __init__(self,id, indice, fila, colum):
        super().__init__(fila, colum)
        self.id = id
        self.indice = indice
        self.tipo = Tipo.ARRAY
        self.referencia = False

    def compilar(self, tree, table):
        genAux = Generador()
        generator = genAux.getInstance()

        generator.addComment(f"Compilacion de Acceso de la variable {self.id}")
        var = ''

        if self.id:
            var = table.getTabla(self.id)

            if(var == None):
                generator.addComment("Fin compilacion de acceso por error")
                return Excepcion("Semantico", "Error no existe la variable '"+str(self.id)+"'", self.fila, self.colum)
        else:
            var = ''

        if len(self.indice) == 1:
            temp = generator.addTemp()
            # Obtencion de posicion de la variable
            tempPos = var.pos
            if(not var.isGlobal):
                tempPos = generator.addTemp()
                generator.addExp(tempPos, 'P', var.pos, "+")
            generator.getStack(temp, tempPos)

            tmp3 = generator.addTemp()
            tmp4 = generator.addTemp()
            tmp5 = generator.addTemp()
            Lbl1 = generator.newLabel()
            Lbl2 = generator.newLabel()
            Lbl3 = generator.newLabel()
            indice = self.indice[0].compilar(tree, table)
            generator.addExp(tmp3, temp,indice.getValue(), '+')
            generator.addIf(indice.getValue(),'1','<',Lbl1)
            generator.getHeap(tmp5, temp)
            generator.addIf(indice.getValue(),tmp5,'>', Lbl1)
            generator.addGoto(Lbl2)
            generator.putLabel(Lbl1)
            error = "Bounds Error \n"
            for char in error:
                generator.addPrint("c",ord(char))
            generator.addGoto(Lbl3)
            generator.putLabel(Lbl2)
            generator.getHeap(tmp4, tmp3)
            generator.addGoto(Lbl3)
            generator.putLabel(Lbl3)
            generator.addComment(f'Fin compilacion de acceso de la variable {self.id}')
            return Return(tmp4, var.getTipoAux(), True)

    def getTipo(self):
        return self.tipo