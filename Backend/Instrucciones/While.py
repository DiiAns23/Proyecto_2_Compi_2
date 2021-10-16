from Abstract.Instruccion import *
from Abstract.Return import *
from Abstract.Tipo import *
from TablaSimbolos.Generador import *
from TablaSimbolos.Excepcion import *
from TablaSimbolos.Tabla_Simbolos import *

class While(Instruccion):
    def __init__(self,condicion, instrucciones, fila, colum):
        super().__init__(fila, colum)
        self.condicion = condicion
        self.instrucciones = instrucciones
    
    def compilar(self, tree, table):
        genAux = Generador()
        generator = genAux.getInstance()
        generator.addComment("Inicia Loop While")
        while True:
            # bandera = False #Nos servira para el break, o el continue
            if self.getTipo():
                Lbl0 = generator.newLabel()
                generator.putLabel(Lbl0)
                condicion = self.condicion.compilar(tree, table)
                if isinstance(condicion, Excepcion): 
                    tree.setExcepciones(condicion)
                generator.putLabel(condicion.getTrueLbl())
                for instruccion in self.instrucciones:
                    entorno = Tabla_Simbolo(table)
                    value = instruccion.compilar(tree, entorno)
                    if isinstance(value, Excepcion): 
                        tree.setExcepciones(condicion)
                generator.addGoto(Lbl0)
                generator.putLabel(condicion.getFalseLbl())
                generator.addComment("Finaliza Loop While")
            break
    
    def getTipo(self):
        if self.condicion.type == OperadorRelacional.MAYOR:
            return True
        elif self.condicion.type == OperadorRelacional.MENOR:
            return True
        elif self.condicion.type == OperadorRelacional.MAYORI:
            return True
        elif self.condicion.type == OperadorRelacional.MENORI:
            return True
        elif self.condicion.type == OperadorRelacional.IGUALDAD:
            return True
        elif self.condicion.type == OperadorRelacional.DIFERENTE:
            return True
        else:
            return False