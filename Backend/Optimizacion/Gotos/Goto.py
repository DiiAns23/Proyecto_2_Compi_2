from Optimizacion.CodigoTresDirecciones import CodigoTresDirecciones as c3d

class Goto(c3d):

    def __init__(self,label, fila, colum):
        self.label = label
        super().__init__(fila, colum)
    
    def getCode(self):
        if self.deleted:
            return ''
        return f'goto {self.label};'