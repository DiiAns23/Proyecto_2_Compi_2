from Optimizacion.CodigoTresDirecciones import CodigoTresDirecciones

class Expresion(CodigoTresDirecciones):

    def __init__(self, izq, der, tipo, line, column):
        self.izq = izq
        self.der = der
        self.tipo = tipo
        super().__init__(line, column)
    
    def nulos(self):
        if self.tipo == '+' or self.tipo == '-':
            self.deleted = self.der.getCode() == '0' or self.izq.getCode() == '0'
        if self.tipo == '*':
            self.deleted = self.der.getCode() == '1' or self.izq.getCode() == '1'
        if self.tipo == '/':
            self.deleted = self.der.getCode() == '1'
        return self.deleted

    def getContrary(self):
        if self.tipo == '>':
            self.tipo = '<='
        elif self.tipo == '<':
            self.tipo = '>='
        elif self.tipo == '>=':
            self.tipo = '<'
        elif self.tipo == '<=':
            self.tipo = '>'
        elif self.tipo == '==':
            self.tipo = '!='
        elif self.tipo == '!=':
            self.tipo = '=='
        return 
        
    def getCode(self):
        return f'{self.izq.getCode()} {self.tipo} {self.der.getCode()}'