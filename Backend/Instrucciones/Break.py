from Abstract.Instruccion import Instruccion

class Break(Instruccion):
    def __init__(self, fila, colum):
        self.fila = fila
        self.colum = colum
    
    def compilar(self, tree, table):
        return self