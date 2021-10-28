from Abstract.Instruccion import *
from Abstract.Return import *
from Abstract.Tipo import *
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
        funcion = tree.getFuncion(self.id)
        genAux = Generador()
        generator = genAux.getInstance()
        if funcion != None:
            generator.addComment(f"Llamada de la Funcion {self.id}")

            paramValues = []
            temps = []
            size = table.size
            
            for param in self.params:
                if isinstance(param, Llamada_Funcion):
                    self.guardarTemps(generator, table, temps)
                    a = param.compilar(tree, table)
                    paramValues.append(a)
                    self.recuperarTemps(generator, table, temps)
                else:
                    a = param.compilar(tree, table)
                    paramValues.append(a)
                    temps.append(a.getValue())

            temp = generator.addTemp()

            generator.addExp(temp,'P', size +1, '+')
            aux = 0
            if len(funcion.getParams()) == len(paramValues):
                for param in paramValues:
                    try:
                        if funcion.params[aux]['tipo'] == param.getTipo()[0]:
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

        generator.addComent(f'Error producido en la llamada a la funcion {self.id} consulte la lista de errores')
        return Excepcion('Semantico',f'No se ha encontrado la funcion {self.id}', self.fila, self.colum)
    
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