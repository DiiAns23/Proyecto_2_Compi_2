from Abstract.Instruccion import *
from Abstract.Return import *
from Abstract.Tipo import *
from Instrucciones.Return import ReturnE
from Instrucciones.Break import Break
from Instrucciones.Continue import Continue
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
            entorno = Tabla_Simbolo(table)
            for instruccion in self.bloqueIf:
                entorno.breakLbl = table.breakLbl 
                entorno.continueLbl = table.continueLbl
                entorno.returnLbl = table.returnLbl
                result = instruccion.compilar(tree, entorno)
                if isinstance(result, Excepcion):
                    tree.setExcepciones(result)
                if isinstance(result, Break):
                    if table.breakLbl != '':
                        generator.addGoto(table.breakLbl)
                    else:
                        salir = generator.newLabel()
                        generator.addGoto(salir)
                        generator.putLabel(condicion.getFalseLbl())
                        generator.putLabel(salir)
                        return Excepcion("Semantico", "Instruccion Break fuera de Ciclo", self.fila, self.colum)
                                        
                if isinstance(result, Continue):
                    if table.continueLbl != '':
                        generator.addGoto(table.continueLbl)
                    else:
                        salir = generator.newLabel()
                        generator.addGoto(salir)
                        generator.putLabel(condicion.getFalseLbl())
                        generator.putLabel(salir)
                        return Excepcion("Semantico", "Instruccion Continue fuera de Ciclo", self.fila, self.colum)
                if isinstance(result, ReturnE):
                    if entorno.returnLbl != '':
                        generator.addComment('Resultado a retornar en la funcion')
                        generator.setStack('P',result.getValor())
                        generator.addGoto(entorno.returnLbl)
                        generator.addComment('Fin del resultado a retornar')
                    
                        
            
            salir = generator.newLabel()
            generator.addGoto(salir)

            generator.putLabel(condicion.getFalseLbl())
            if self.bloqueElse != None:
                entorno = Tabla_Simbolo(table)
                for instruccion in self.bloqueElse:
                    entorno.breakLbl = table.breakLbl 
                    entorno.continueLbl = table.continueLbl
                    entorno.returnLbl = table.returnLbl
                    result = instruccion.compilar(tree, entorno)
                    if isinstance(result, Excepcion):
                        tree.setExcepciones(result)
                    if isinstance(result, Break):
                        if table.breakLbl != '':
                            generator.addGoto(table.breakLbl)
                        else:
                            generator.putLabel(salir)
                            return Excepcion("Semantico", "Instruccion Break fuera de Ciclo", self.fila, self.colum)
                    if isinstance(result, Continue):
                        if table.continueLbl != '':
                            generator.addGoto(table.continueLbl)
                        else:
                            generator.putLabel(salir)
                            return Excepcion("Semantico", "Instruccion Continue fuera de Ciclo", self.fila, self.colum)
                    if isinstance(result, ReturnE):
                        if entorno.returnLbl != '':
                            generator.addComment('Resultado a retornar en la funcion')
                            generator.setStack('P',result.getValor())
                            generator.addGoto(entorno.returnLbl)
                            generator.addComment('Fin del resultado a retornar')
            elif self.bloqueElif != None:
                result = self.bloqueElif.compilar(tree, table)
                if isinstance(result, Excepcion): return result
            generator.putLabel(salir)

        generator.addComment("Termina condicional If")

        