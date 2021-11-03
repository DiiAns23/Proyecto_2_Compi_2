class Arbol:
    def __init__(self, instrucciones):
        self.instrucciones = instrucciones
        self.funciones = {}
        self.structs = {}
        self.excepciones = []
        self.consola = ""
        self.tsglobal = None
        self.tsgInterpretada = {}
    
    def setTsgI(self, entorno, valor):
        self.tsgInterpretada[entorno] = valor
    
    def getTsgI(self):
        return self.tsgInterpretada

    def getInst(self):
        return self.instrucciones
    
    def setInst(self, instrucciones):
        self.instrucciones = instrucciones
    
    def getFunciones(self):
        return self.funciones
    
    def setFunciones(self,id, function):
        if id in self.funciones.keys():
            return "error"
        else:
            self.funciones[id] = function
    
    def getFuncion(self, id):
        actual = self
        if actual!=None:
            if id in actual.funciones.keys():
                return actual.funciones[id]
        return None
    
    def setStruct(self,id, struct):
        if id in self.structs.keys():
            return "error"
        else:
            self.structs[id] = struct

    def getStruct(self,id):
        actual = self
        if actual!=None:
            if id in actual.structs.keys():
                return actual.structs[id]
        return None
            

    def getExcepciones(self):
        return self.excepciones
    
    def setExcepciones(self, excep):
        self.excepciones.append(excep)
    
    def getConsola(self):
        return self.consola
    
    def setConsola(self, consola):
        self.consola = consola
    
    def updateConsola(self, cadena):
        self.consola += str(cadena) + '\n'
    
    def updateConsola2(self, cadena):
        self.consola += str(cadena)

    def getTSGlobal(self):
        return self.TSglobal
    
    def setTSglobal(self, TSglobal):
        self.TSglobal = TSglobal
