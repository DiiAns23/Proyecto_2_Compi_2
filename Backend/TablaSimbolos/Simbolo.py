from Abstract.Return import *
from Abstract.Tipo import *

class Simbolo:

    def __init__(self, symbolID, symbolType, position, globalVar, inHeap):
        self.id = symbolID
        self.type = symbolType
        self.pos = position
        self.isGlobal = globalVar
        self.inHeap = inHeap
        self.value = None
        self.tipoAux = ''
        self.length = 0
        self.referencia = False
    
    def getTipo(self):
        return self.type
    def getId(self):
        return self.id
    def getPos(self):
        return self.pos
    def getInHeap(self):
        return self.inHeap
    
    def setTipo(self, tipo):
        self.type = tipo
    def setId(self, id):
        self.id = id
    def setPos(self, pos):
        self.pos = pos
    def setInHeap(self, value):
        self.inHeap = value
    
    def setTipoAux(self, tipo):
        self.tipoAux = tipo

    def getTipoAux(self):
        return self.tipoAux

    def setLength(self, length):
        self.length = length
    def getLength(self):
        return self.length

    def setReferencia(self, ref):
        self.referencia = ref
    def getReferencia(self):
        return self.referencia
    
    def getValue(self):
        return self.value
    def setValue(self, value):
        self.value = value