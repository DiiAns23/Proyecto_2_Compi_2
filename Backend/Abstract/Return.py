class Return:
    def __init__(self, val, retType, isTemp, auxType = ""):
        self.value = val
        self.type = retType
        self.auxType = auxType
        self.isTemp = isTemp
        self.trueLbl = ''
        self.falseLbl = ''