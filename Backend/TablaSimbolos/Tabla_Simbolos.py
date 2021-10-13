from Abstract.Tipo import Tipo
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Simbolo import *

class Tabla_Simbolo:
    
    def __init__(self, anterior = None):
        self.tabla = {}
        self.anterior = anterior
        
        # NUEVO
        self.size = 0
        if(anterior != None):
            self.size = self.anterior.size
    
    def setTabla(self, id, tipo, inHeap):
        if id in self.tabla:
            self.tabla[id].setTipo(tipo)
            self.tabla[id].setInHeap(inHeap)
        else:
            simbolo = Simbolo(id, tipo, self.size, self.anterior == None, inHeap)
            self.size += 1
            self.tabla[id] = simbolo
        return self.tabla[id]
    

    def getTabla(self, ide):
        tablaActual = self
        while tablaActual != None:
            if ide in tablaActual.tabla:
                return tablaActual.tabla[ide]
            tablaActual = tablaActual.anterior
        return None
        

    def getGlobal(self):
        tablaActual = self
        while tablaActual.anterior != None:
            tablaActual = tablaActual.anterior
        return tablaActual