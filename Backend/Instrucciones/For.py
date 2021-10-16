from Abstract.Instruccion import *
from Abstract.Return import *
from Abstract.Tipo import *
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

        Lbl0 = generator.newLabel()
        Lbl1 = generator.newLabel()
        Lbl2 = generator.newLabel()
        Lbl3 = generator.newLabel()
        self.inicio.value = self.rango[0]
        self.inicio.tipo = self.rango[0].getTipo()
        fin = self.rango[1].compilar(tree,table)

        bandera = True
        entorno = table
        
        if table.findTabla(self.inicio.id):
            bandera = False
        
        if bandera:
            entorno = Tabla_Simbolo(table)
            self.inicio.compilar(tree,entorno)

            generator.putLabel(Lbl0)
            tmp1 = generator.addTemp()
            tmp2 = generator.addTemp()
            generator.addExp(tmp2, 'P', table.size,'+')
            generator.getStack(tmp1, tmp2)

            generator.addIf(tmp1,fin.getValue(),'<=',Lbl1)
            generator.addGoto(Lbl2)
            generator.putLabel(Lbl1)
            
            entorno = Tabla_Simbolo(entorno)
            for instruccion in self.instrucciones:
                value = instruccion.compilar(tree, entorno)
                if isinstance(value,Excepcion):
                    tree.setExcepciones(value)
            
            tmp11 = generator.addTemp()
            tmp12 = generator.addTemp()
            tmp13 = generator.addTemp()
            tmp14 = generator.addTemp()

            generator.addGoto(Lbl3)
            generator.putLabel(Lbl3)

            generator.addExp(tmp11, 'P',table.size,'+')
            generator.addExp(tmp13, 'P', table.size,'+')
            generator.getStack(tmp12, tmp13)
            generator.addExp(tmp14, tmp12, '1','+')
            generator.setStack(tmp11, tmp14)
        else:
            self.inicio.compilar(tree,entorno)

        
        generator.addGoto(Lbl0)
        generator.putLabel(Lbl2)
        generator.addSpace()
        
        


