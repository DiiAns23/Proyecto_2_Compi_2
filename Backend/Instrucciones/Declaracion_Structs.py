from typing import List
from TablaSimbolos.Generador import *
from Abstract.Instruccion import *
from Abstract.Return import *
from Abstract.Tipo import *
from TablaSimbolos.Simbolo import *
from TablaSimbolos.Excepcion import *

class Declaracion_Sructs(Instruccion):

    def __init__(self,mutable,id, parametros, fila, colum):
        self.mutable = mutable
        self.id = id
        self.params = parametros
        self.tipo = Tipo.STRUCT
        self.tipoAux = id
        super().__init__(fila, colum)
    
    def compilar(self, tree, table):
        struct = tree.setStruct(self.id, self)
        if struct == "error":
            return Excepcion("Semantico",f'Structc {self.id} ya existe', self.fila, self.colum)
        
        genAux = Generador()
        generator = genAux.getInstance()
        generator.addComment(f"Compilacion del Struct {self.id}")
        entorno = Tabla_Simbolo(table)
        if self.params:
            for param in self.params:
                if not isinstance(param["tipo"], List):
                    simbolo = entorno.setTabla(param["ide"], param["tipo"], (param["tipo"] == Tipo.STRING or param["tipo"] == Tipo.STRUCT or param["tipo"] == Tipo.ARRAY))
                else:
                    simbolo = entorno.setTabla(param["ide"], param["tipo"][0],True)
                    simbolo.setTipoAux(param["tipo"][1])

    def getParams(self):
        return self.params