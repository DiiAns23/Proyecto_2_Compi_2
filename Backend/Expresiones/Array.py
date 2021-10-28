from typing import List
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

        generator.fboundError()
        temp = generator.addTemp()
        # Obtencion de posicion de la variable
        tempPos = var.pos
        if(not var.isGlobal):
            tempPos = generator.addTemp()
            generator.addExp(tempPos, 'P', var.pos, "+")
        generator.getStack(temp, tempPos)
        x = 0
        tipo = var.getTipo()
        tipoAux = var.getTipoAux()
        for value in self.indice:
            x += 1
            tmp3 = generator.addTemp()
            tmp4 = generator.addTemp()
            tmp5 = generator.addTemp()
            Lbl1 = generator.newLabel()  #Agregado
            Lbl2 = generator.newLabel() #Agregado
            Lbl3 = generator.newLabel() #Agregado

            indice = value.compilar(tree, table)
            generator.addExp(tmp3, temp,indice.getValue(), '+')

            generator.addIf(indice.getValue(),'1','<',Lbl1) #Agregado
            generator.getHeap(tmp5, temp)
            generator.addIf(indice.getValue(),tmp5,'>', Lbl1) #Agregado
            generator.addGoto(Lbl2)
            generator.putLabel(Lbl1)
            generator.callFun('BoundsError')
            generator.addGoto(Lbl3)
            generator.putLabel(Lbl2)

            generator.getHeap(tmp4, tmp3)

            generator.addGoto(Lbl3)
            generator.putLabel(Lbl3)

            temp = tmp4
            if x == len(self.indice):
                var.setTipo(var.getTipoAux())
            else:
                if isinstance(var.getTipoAux(), List):
                    var.setTipo(var.getTipoAux()[0])
                    var.setTipoAux(var.getTipoAux()[1])
                else:
                    return Excepcion("Semantico", "No se puede acceder al arreglo", self.fila, self.colum)

        generator.addComment(f'Fin compilacion de acceso de la variable {self.id}')
        space = Return(tmp4, var.getTipo(), True, var.getTipoAux())
        var.setTipo(tipo)
        var.setTipoAux(tipoAux)
        return space

    def getTipo(self):
        return self.tipo