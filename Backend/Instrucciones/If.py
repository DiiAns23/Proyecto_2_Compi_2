from Abstract.Instruccion import *
from Abstract.Return import *
from Abstract.Tipo import *
from TablaSimbolos.Generador import *
from TablaSimbolos.Excepcion import *
from TablaSimbolos.Tabla_Simbolos import *

class If(Instruccion):

    def __init__(self,condicion, bloqueIf, bloqueElse, bloqueElif, fila, colum):
        super().__init__(fila, colum)
        self.condicion = condicion
        self.bloqueIf = bloqueIf
        self.bloqueElse = bloqueElse
        self.bloqueElif = bloqueElif
    
    def compilar(self, tree, table):
        genAux = Generador()
        generator = genAux.getInstance()
        generator.addComment("Inicia condicional If")
        condicion = self.condicion.compilar(tree, table)
        if isinstance(condicion, Excepcion): return condicion

        if condicion.getTipo() == Tipo.BOOL:
            generator.putLabel(condicion.getTrueLbl())
            for instruccion in self.bloqueIf:
                result = instruccion.compilar(tree, table)
                if isinstance(result, Excepcion):
                    tree.setExcepciones(result)
            
            salir = generator.newLabel()
            generator.addGoto(salir)

            generator.putLabel(condicion.getFalseLbl())
            if self.bloqueElse != None:
                for instruccion in self.bloqueElse:
                    result = instruccion.compilar(tree, table)
                    if isinstance(result, Excepcion):
                        tree.setExcepciones(result)
            elif self.bloqueElif != None:
                result = self.bloqueElif.compilar(tree, table)
                if isinstance(result, Excepcion): return result
            generator.putLabel(salir)

        generator.addComment("Termina condicional If")

        