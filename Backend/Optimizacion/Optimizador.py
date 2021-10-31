from Optimizacion.Gotos.Goto import *
from Optimizacion.Gotos.If import *
from Optimizacion.Instrucciones.Asignacion import *
from Optimizacion.Instrucciones.Label import Label

class Optimizador:

    def __init__(self, packages, temporales, codigo):
        self.packages = packages
        self.temps = temporales
        self.code = codigo
    
    def getCode(self):
        ret = f'package main;\n\n'
        if self.packages:
            var = ''
            for pk in self.packages:
                var += '"'+ pk + '";\n\t'
            var = var[:-3]
            ret += f'import(\n\t{var}\n);\n'
        for temp in self.temps:
            ret += f'var {temp}\n'
        
        ret += '\n'
        
        for func in self.code:
            ret += func.getCode() + '\n\n'
            
        return ret
    
    def Mirilla(self):
        for func in self.code:
            # tam = 100
            tam = int(len(func.inst)/4)
            while tam <= len(func.inst):
                flagOpt = False

                # Darle 5 pasadas al codigo con el tamaño actual
                for i in range(5):
                    aux = 0
                    # Dar una pasada completa
                    while (tam + aux) <= len(func.inst):
                        flagOpt = flagOpt or self.Regla1(func.inst[0 + aux: tam + aux])
                        flagOpt = flagOpt or self.Regla3(func.inst[0 + aux: tam + aux])
                        # flagOpt = flagOpt or self.Regla6(func.inst[0 + aux: tam + aux])
                        aux = aux + 1
                        
                # Si no hubo optimizacion en la pasada, subir el tamaño
                if not flagOpt:
                    tam += tam
        return ''

    def Regla1(self, array):
        # Auxiliar para verificar que la regla se implemento
        ret = False
        # Recorrer el arreglo de instrucciones C3D
        for i in range(len(array)):
            actual = array[i]
            if isinstance(actual, Asignacion) and not actual.deleted:
                if i < len(array)-1:
                    nextIns = array[i+1]
                    if not isinstance(nextIns, Label):
                        #Si el siguiente es la misma asignacion
                        if isinstance(nextIns, Asignacion) and not nextIns.deleted:
                            a = actual.getPlace()
                            b = nextIns.getExp()
                            c = actual.getExp()
                            d = nextIns.getPlace()
                            if (a == b) and (c == d):
                                nextIns.deleted = True
                                ret = True
        return ret
    
    def Regla3(self, array):
        # Auxiliar para verificar que la regla se implemento
        ret = False
        # Recorrer el arreglo de instrucciones C3D
        for i in range(len(array)):
            actual = array[i]
            # Si la instruccion es un If
            if isinstance(actual, If) and not actual.deleted:
                try:
                    nextIns = array[i+1]
                    # Si el siguiente es un Goto
                    if isinstance(nextIns, Goto) and not nextIns.deleted:
                        # SE DEBE ELIMINAR i+1 e i+2. Goto LBL y LBL:
                        actual.condicion.getContrary()
                        actual.label = nextIns.label
                        nextIns.deleted = True
                        array[i+2].deleted = True
                        ret = True
                except:
                    pass
        return ret
    
    def Regla6(self, array):
        ret = False
        # Recorrer el arreglo de instrucciones C3D
        for i in range(len(array)):
            actual = array[i]
            # Si la instruccion es una Asignacion
            if isinstance(actual, Asignacion) and not actual.deleted:
                # Si se esta asignando a si mismo
                if(actual.selfAsignacion()):
                    actualOpt = actual.exp.nulos()
                    if actualOpt:
                        ret = True
                        actual.deleted = True
        return ret