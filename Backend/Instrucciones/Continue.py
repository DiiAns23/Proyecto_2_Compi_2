from Abstract.Instruccion import Instruccion

class Continue(Instruccion):
    def __init__(self, fila, colum):
        super().__init__(fila, colum)
    
    def compilar(self, tree, table):
        return self