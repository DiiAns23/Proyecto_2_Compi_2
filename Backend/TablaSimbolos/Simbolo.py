from Abstract.Return import *

class Simbolo:

    def __init__(self, symbolID, symbolType, position, globalVar, inHeap):
        self.id = symbolID
        self.type = symbolType
        self.pos = position
        self.isGlobal = globalVar
        self.inHeap = inHeap

        self.value = None
    
    def getTipo(self):
        return self.type
    def getId(self):
        return self.id
    def getPos(self):
        return self.getPos
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