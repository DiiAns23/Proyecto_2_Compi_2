from Abstract.Tipo import Tipo
from TablaSimbolos.Excepcion import Excepcion
from TablaSimbolos.Simbolo import *

class Tabla_Simbolo:
    
    def __init__(self, anterior = None):
        self.tabla = {}
        self.anterior = anterior
        # NUEVO
        self.breakLbl = ''
        self.continueLbl = ''
        self.returnLbl = ''
        self.recTemps = False
        self.size = 0
        if(anterior != None):
            self.size = self.anterior.size

    
    def setTabla(self, id, tipo, inHeap, find = True):
        if find:
            tablaActual = self
            while tablaActual != None:
                if id in tablaActual.tabla:
                    tablaActual.tabla[id].setTipo(tipo)
                    tablaActual.tabla[id].setInHeap(inHeap)
                    return tablaActual.tabla[id]
                else:
                    tablaActual = tablaActual.anterior
        
        if id in self.tabla:
            self.tabla[id].setTipo(tipo)
            self.tabla[id].setInHeap(inHeap)
            return self.tabla[id]
        else:
            simbolo = Simbolo(id, tipo, self.size, self.anterior == None, inHeap)
            self.size += 1
            self.tabla[id] = simbolo
            return self.tabla[id]
    
    def findTabla(self, id):
        tablaActual = self
        while tablaActual != None:
            if id in tablaActual.tabla:
                return True
            else:
                tablaActual = tablaActual.anterior
        return False

    def getTabla(self, ide):
        tablaActual = self
        while tablaActual != None:
            if ide in tablaActual.tabla:
                return tablaActual.tabla[ide]
            tablaActual = tablaActual.anterior
        return None
    
    def updateTabla(self,id, tipo, inHeap):
        tablaActual = self
        while tablaActual != None:
            if id in tablaActual.tabla:
                tablaActual.tabla[id].setTipo(tipo)
                tablaActual.tabla[id].setInHeap(inHeap)
                return tablaActual.tabla[id]
            else:
                tablaActual = tablaActual.anterior
        return Excepcion("Semantico", "Variable no encontrada",-1,-1)

    def getGlobal(self):
        tablaActual = self
        while tablaActual.anterior != None:
            tablaActual = tablaActual.anterior
        return tablaActual