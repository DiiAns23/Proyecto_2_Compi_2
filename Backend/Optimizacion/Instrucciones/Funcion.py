from Optimizacion.CodigoTresDirecciones import CodigoTresDirecciones as c3d

class Funcion(c3d):

    def __init__(self, id, inst, fila, colum):
        self.id = id
        self.inst = inst
        super().__init__(fila, colum)

    def getCode(self):
        ret = f'func {self.id} () {{\n'
        for inst in self.inst:
            aux1 = inst.getCode()
            if aux1 != '':
                ret += f'\t{aux1}\n'
        
        ret += '}'
        return ret