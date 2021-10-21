from Abstract.Instruccion import *
from Abstract.Return import *
from Abstract.Tipo import *
from Instrucciones.Break import Break
from Instrucciones.Continue import Continue
from Expresiones.Variable import Variable
from Expresiones.Array import Array
from Expresiones.Primitivos import Primitivos
from TablaSimbolos.Generador import *
from TablaSimbolos.Excepcion import *
from TablaSimbolos.Tabla_Simbolos import *
from Instrucciones.Declaracion import *

class For(Instruccion):
    def __init__(self, inicio, rango, instrucciones,fila, colum):
        super().__init__(fila, colum)
        self.inicio = inicio
        self.rango = rango
        self.instrucciones = instrucciones
        
    
    def compilar(self, tree, table):
        genAux = Generador()
        generator = genAux.getInstance()
        generator.addComment("Inicia Loop For")

        bandera = True
        entorno = table
        if table.findTabla(self.inicio.id):
            bandera = False

        if len(self.rango) == 2:
            Lbl0 = generator.newLabel()
            Lbl1 = generator.newLabel()
            Lbl2 = generator.newLabel()
            Lbl3 = generator.newLabel()
            self.inicio.value = self.rango[0]
            self.inicio.tipo = self.rango[0].getTipo()
            fin = self.rango[1].compilar(tree,table)
            
            if bandera:
                entorno = Tabla_Simbolo(table)
                self.inicio.compilar(tree,entorno)

                generator.putLabel(Lbl0)
                tmp2 = generator.addTemp()
                
                generator.addExp(tmp2, 'P', table.size,'+')
                tmp1 = generator.addTemp()
                generator.getStack(tmp1, tmp2)

                generator.addIf(tmp1,fin.getValue(),'<=',Lbl1)
                generator.addGoto(Lbl2)
                generator.putLabel(Lbl1)
                
                entorno = Tabla_Simbolo(entorno)
                entorno.breakLbl = Lbl2
                entorno.continueLbl = Lbl3
                for instruccion in self.instrucciones:
                    value = instruccion.compilar(tree, entorno)
                    if isinstance(value,Excepcion):
                        tree.setExcepciones(value)
                    if isinstance(value, Break):
                        generator.addGoto(Lbl2)
                    if isinstance(value, Continue):
                        generator.addGoto(Lbl3)
                entorno.breakLbl = ''
                entorno.continueLbl = ''

                generator.addGoto(Lbl3)
                generator.putLabel(Lbl3)

                generator.addExp(tmp1,tmp1, '1', '+')
                generator.setStack(tmp2, tmp1)

            else:
                Lbl0 = generator.newLabel()
                Lbl1 = generator.newLabel()
                Lbl2 = generator.newLabel()
                Lbl3 = generator.newLabel()
                self.inicio.compilar(tree,entorno)
                generator.putLabel(Lbl0)
                variable = table.getTabla(self.inicio.id)
                tmp1 = generator.addTemp()
                generator.getStack(tmp1, variable.getPos())

                generator.addIf(tmp1, fin.getValue(), '<=', Lbl1)
                generator.addGoto(Lbl2)
                generator.putLabel(Lbl1)

                entorno = Tabla_Simbolo(entorno)
                entorno.breakLbl = Lbl2
                entorno.continueLbl = Lbl3
                for instruccion in self.instrucciones:
                    value = instruccion.compilar(tree, entorno)
                    if isinstance(value,Excepcion):
                        tree.setExcepciones(value)
                    if isinstance(value, Break):
                        generator.addGoto(Lbl2)
                    if isinstance(value, Continue):
                        generator.addGoto(Lbl3)
                entorno.breakLbl = ''
                entorno.continueLbl = ''
                tmp7 = generator.addTemp()
                tmp8 = generator.addTemp()

                generator.addGoto(Lbl3)
                generator.putLabel(Lbl3)
                generator.addComment('Actualizacion de Ciclo For')
                generator.getStack(tmp7,variable.getPos())
                generator.addExp(tmp8,tmp7,'1','+')
                generator.setStack(variable.getPos(),tmp8)
                generator.addComment('Fin de la actualizacion')
        
        if len(self.rango) == 1:
            valor = self.rango[0]
            if not isinstance(valor, Variable):
                if valor.getTipo() == Tipo.ARRAY:
                    if bandera:
                        entorno = Tabla_Simbolo(table)
                        valor.setId('for')
                        value = valor.compilar(tree, entorno)
                        if isinstance(value, Excepcion): return value
                        Lbl0 = generator.newLabel()
                        Lbl1 = generator.newLabel()
                        Lbl2 = generator.newLabel()
                        Lbl3 = generator.newLabel()

                        tmp3 = generator.addTemp()
                        generator.addExp(tmp3, tmp3,'1','+')

                        generator.putLabel(Lbl0)
                        generator.addIf(tmp3, int(valor.getLength())+1, '==', Lbl2)
                        
                        primitivo = Primitivos(tmp3, Tipo.INT, self.fila, self.colum)
                        array = Array('for', [primitivo],self.fila, self.colum)
                        self.inicio.value = array
                        self.inicio.compilar(tree,entorno)
                        if isinstance(value, Excepcion): return value

                        entorno = Tabla_Simbolo(entorno)
                        entorno.breakLbl = Lbl2
                        entorno.continueLbl = Lbl3
                        for instruccion in self.instrucciones:
                            value = instruccion.compilar(tree, entorno)
                            if isinstance(value, Excepcion):
                                tree.setExcepciones(value)
                            if isinstance(value, Continue):
                                generator.addGoto(Lbl3)
                            if isinstance(value, Break):
                                generator.addGoto(Lbl2)
                        entorno.breakLbl = ''
                        entorno.continueLbl = ''
                        generator.addGoto(Lbl3)
                        generator.putLabel(Lbl3)

                        generator.addExp(tmp3, tmp3, '1', '+')

                elif valor.getTipo() == Tipo.STRING:
                    if bandera:
                        entorno = Tabla_Simbolo(table)
                        value = valor.compilar(tree,entorno)
                        if isinstance(value, Excepcion): return value
                                            
                        Lbl0 = generator.newLabel()
                        Lbl1 = generator.newLabel()
                        Lbl2 = generator.newLabel()
                        Lbl3 = generator.newLabel()


                        generator.putLabel(Lbl0)

                        tmp = self.inicio.gosth = value.getValue()
                        pos = self.inicio.compilar(tree, entorno)

                        tmp3 = generator.addTemp()
                        tmp4 = generator.addTemp()

                        generator.getStack(tmp3,pos)
                        generator.getHeap(tmp4, tmp3)
                        generator.addIf(tmp4, '-1', '!=', Lbl1)
                        generator.addGoto(Lbl2)
                        generator.putLabel(Lbl1)

                        entorno = Tabla_Simbolo(entorno)
                        entorno.breakLbl = Lbl2
                        entorno.continueLbl = Lbl3
                        for instruccion in self.instrucciones:
                            value = instruccion.compilar(tree, entorno)
                            if isinstance(value, Excepcion):
                                tree.setExcepciones(value)
                        entorno.breakLbl = ''
                        entorno.continueLbl = ''
                        generator.addGoto(Lbl3)
                        generator.putLabel(Lbl3)
                        generator.addExp(tmp, tmp, '1','+')
            else:
                value = valor.compilar(tree, table)
                if isinstance(value, Excepcion): return value
                                            
                Lbl0 = generator.newLabel()
                Lbl1 = generator.newLabel()
                Lbl2 = generator.newLabel()
                Lbl3 = generator.newLabel()


                generator.putLabel(Lbl0)
                entorno = Tabla_Simbolo(entorno)
                tmp = self.inicio.gosth = value.getValue()
                pos = self.inicio.compilar(tree, entorno)

                tmp3 = generator.addTemp()
                tmp4 = generator.addTemp()

                generator.getStack(tmp3,pos)
                generator.getHeap(tmp4, tmp3)
                generator.addIf(tmp4, '-1', '!=', Lbl1)
                generator.addGoto(Lbl2)
                generator.putLabel(Lbl1)

                entorno = Tabla_Simbolo(entorno)
                for instruccion in self.instrucciones:
                    value = instruccion.compilar(tree, entorno)
                    if isinstance(value, Excepcion):
                        tree.setExcepciones(value)
                generator.addGoto(Lbl3)
                generator.putLabel(Lbl3)
                generator.addExp(tmp, tmp, '1','+')

        generator.addGoto(Lbl0)
        generator.putLabel(Lbl2)
        generator.addSpace()
