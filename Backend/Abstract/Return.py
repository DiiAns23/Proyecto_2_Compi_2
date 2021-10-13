
class Return:
    def __init__(self, val, retType, isTemp, auxType = ""):
        self.value = val
        self.type = retType
        self.auxType = auxType
        self.isTemp = isTemp
        self.trueLbl = ''
        self.falseLbl = ''
    
    def getValue(self):
        return self.value
    def getTipo(self):
        return self.type
    def getTrueLbl(self):
        return self.trueLbl
    def getFalseLbl(self):
        return self.falseLbl
    def setValue(self, value):
        self.value = value
    def setTipo(self, tipo):
        self.type = tipo
    def setTrueLbl(self, trueLbl):
        self.trueLbl = trueLbl
    def setFalseLbl(self, falseLbl):
        self.falseLbl = falseLbl