from typing import List
from Abstract.Instruccion import *
from Abstract.Return import *
from Abstract.Tipo import *
from Instrucciones.Declaracion_Arrays import Declaracion_Arrays
from TablaSimbolos.Generador import *
from TablaSimbolos.Excepcion import *
from TablaSimbolos.Tabla_Simbolos import *
from Instrucciones.Declaracion import *

class Llamada_Funcion(Instruccion):

    def __init__(self, id, params, fila, colum):
        self.id = id
        self.params = params
        self.trueLbl = ''
        self.falseLbl = ''
        super().__init__(fila, colum)
    
    def compilar(self, tree, table):
        genAux = Generador()
        generator = genAux.getInstance()
        funcion = tree.getFuncion(self.id)
        if funcion != None:
            generator.addComment(f"Llamada de la Funcion {self.id}")
            paramValues = []
            temps = []
            size = table.size
            
            for param in self.params:
                if isinstance(param, Llamada_Funcion):
                    self.guardarTemps(generator, table, temps)
                    a = param.compilar(tree, table)
                    if isinstance(a, Excepcion): return a
                    paramValues.append(a)
                    self.recuperarTemps(generator, table, temps)
                else:
                    a = param.compilar(tree, table)
                    if isinstance(a, Excepcion): return a
                    paramValues.append(a)
                    temps.append(a.getValue())

            temp = generator.addTemp()

            generator.addExp(temp,'P', size +1, '+')
            aux = 0
            if len(funcion.getParams()) == len(paramValues):
                for param in paramValues:
                    try:
                        if (funcion.params[aux]['tipo'] == param.getTipo()[0]) or (funcion.params[aux]['tipo'] == param.getTipo()[0]):
                            aux += 1
                            generator.setStack(temp, param.getValue())
                            if aux != len(paramValues):
                                generator.addExp(temp, temp, '1', '+')
                    except:
                        try:
                            if funcion.params[aux]['tipo'][0] == param.getTipo():
                                aux += 1
                                generator.setStack(temp, param.getValue())
                                if aux != len(paramValues):
                                    generator.addExp(temp, temp, '1', '+')
                            else:
                                generator.addComment(f'Fin de la llamada a la funcion {self.id} por error, consulte la lista de errores')
                                return Excepcion('Semantico', f'Tipos no coinciden en la llamada de la funcion {self.id}', self.fila, self.colum)
                        except:
                            if funcion.params[aux]['tipo'] == param.getTipo():
                                aux += 1
                                generator.setStack(temp, param.getValue())
                                if aux != len(paramValues):
                                    generator.addExp(temp, temp, '1', '+')
                            else:
                                generator.addComment(f'Fin de la llamada a la funcion {self.id} por error, consulte la lista de errores')
                                return Excepcion('Semantico', f'Tipos no coinciden en la llamada de la funcion {self.id}', self.fila, self.colum)
            else:
                generator.addComment(f'Error en la llamada de la funcion {self.id}')
                return Excepcion("Semantico",f'Error en la llamada de la funcion {self.id}', self.fila, self.colum)
            generator.newEnv(size)
            self.getFuncion(generator)
            generator.callFun(self.id)
            generator.getStack(temp, 'P')
            generator.retEnv(size)
            generator.addComment(f"Fin de la llamada a la funcion {self.id}")
            generator.addSpace()

            if funcion.getTipo() != Tipo.BOOL:
                return Return(temp, funcion.getTipo(), True)

            else:
                generator.addComment('Recuperacion de booleano')
                if self.trueLbl == '':
                    self.trueLbl = generator.newLabel()
                if self.falseLbl == '':
                    self.falseLbl = generator.newLabel()
                generator.addIf(temp, '1', '==', self.trueLbl)
                generator.addGoto(self.falseLbl)
                ret = Return(temp, funcion.getTipo(), True)
                ret.trueLbl = self.trueLbl
                ret.falseLbl = self.falseLbl
                generator.addComment('Fin de recuperacion de booleano')
                return ret

        struct = tree.getStruct(self.id)
        if struct != None:
            generator.addComment(f'Creando Struct {self.id}')
            paramValues = []
            temps = []
            size = table.size
            t0 = generator.addTemp()
            t1 = generator.addTemp()
            generator.addAsig(t0,'H')
            generator.addAsig(t1,'H')
            generator.addExp('H','H',len(struct.params),'+')
            generator.addSpace()
            length = 0
            apuntador = 0
            for param in self.params:
                if isinstance(param, Llamada_Funcion):
                    self.guardarTemps(generator, table, temps)
                    a = param.compilar(tree, table)
                    if isinstance(a, Excepcion): return a
                    paramValues.append(a)
                    self.recuperarTemps(generator, table, temps)
                else:
                    if isinstance(param, Declaracion_Arrays):
                        param.isinStruct = True
                    val = param.compilar(tree, table)
                    try:
                        if not isinstance(struct.params[apuntador]['tipo'], List):
                            if val.getTipo() == struct.params[apuntador]['tipo']:
                                generator.setHeap(t1,val.getValue())
                                generator.addExp(t1,t1,'1','+')
                                generator.addSpace()
                                length += 1
                                apuntador += 1
                            else:
                                return Excepcion("Semantico", "Tipos no coinciden en declaracion o asignacion del struct", self.fila, self.colum)
                        else:
                            if val.getTipo() == struct.params[apuntador]['tipo'][0] and (val.getTipoAux() == struct.params[apuntador]['tipo'] or val.getTipoAux() == struct.params[apuntador]['tipo'][1]):
                                generator.setHeap(t1,val.getValue())
                                generator.addExp(t1,t1,'1','+')
                                generator.addSpace()
                                length += 1
                                apuntador += 1
                            else:
                                return Excepcion("Semantico", "Tipos no coinciden en declaracion o asignacion del struct", self.fila, self.colum)
                        
                    except:
                        return Excepcion("Semantico", "Tipos no coinciden en declaracion o asignacion del struct", self.fila, self.colum)
    
            ret = Return(t0, Tipo.STRUCT, True, struct.id, struct.params)
            generator.addComment('Fin de la asignacion')
            return ret
            
        else:
            generator.addComment(f'Error producido en la llamada a la funcion o struct {self.id} consulte la lista de errores')
            return Excepcion('Semantico',f'No se ha encontrado la funcion o struct {self.id}', self.fila, self.colum)
    
    def guardarTemps(self, generator, table, tmp2):
        generator.addComment('Guardado de temporales')
        tmp = generator.addTemp()
        for tmp1 in tmp2:
            generator.addExp(tmp, 'P', table.size, '+')
            generator.setStack(tmp,tmp1)
            table.size += 1
        generator.addComment('Fin de guardado de temporales')
    
    def recuperarTemps(self, generator, table, tmp2):
        generator.addComment('Recuperacion de Temporales')
        tmp = generator.addTemp()
        for tmp1 in tmp2:
            table.size -= 1
            generator.addExp(tmp, 'P', table.size, '+')
            generator.getStack(tmp1,tmp)
        generator.addComment('Fin de recuperacion de temporales')

    def getFuncion(self, generator):
        if self.id == 'length':
            generator.fLength()
        elif self.id == 'trunc':
            generator.fTrunc()
        elif self.id == 'float':
            generator.fFloat()
        elif self.id == 'uppercase':
            generator.fUpperCase()
        elif self.id == 'lowercase':
            generator.fLowerCase()
        return