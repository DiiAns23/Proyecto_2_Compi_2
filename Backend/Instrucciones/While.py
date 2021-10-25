from Abstract.Instruccion import *
from Abstract.Return import *
from Abstract.Tipo import *
from Instrucciones.Return import ReturnE
from Instrucciones.Break import *
from Instrucciones.Continue import Continue
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

                table.breakLbl = condicion.getFalseLbl()
                table.continueLbl = Lbl0
                
                for instruccion in self.instrucciones:
                    entorno = Tabla_Simbolo(table)
                    entorno.breakLbl = condicion.getFalseLbl()
                    entorno.continueLbl = Lbl0
                    entorno.returnLbl = table.returnLbl
                    value = instruccion.compilar(tree, entorno)
                    if isinstance(value, Excepcion): 
                        tree.setExcepciones(condicion)
                    if isinstance(value, Break):
                        generator.addGoto(condicion.getFalseLbl())
                    if isinstance(value, Continue):
                        generator.addGoto(Lbl0)
                    if isinstance(value, ReturnE):
                        if entorno.returnLbl != '':
                            generator.addComment('Resultado a retornar en la funcion')
                            generator.setStack('P',value.getValor())
                            generator.addGoto(entorno.returnLbl)
                            generator.addComment('Fin del resultado a retornar')
                table.breakLbl = ''
                table.continueLbl = ''

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
        elif self.condicion.type == OperadorLogico.OR:
            return True
        elif self.condicion.type == OperadorLogico.AND:
            return True
        else:
            return False