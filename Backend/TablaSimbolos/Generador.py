from typing import AsyncIterable
from TablaSimbolos.Tabla_Simbolos import *

class Generador:
    generator = None
    def __init__(self):
        # Contadores
        self.countTemp = 0
        self.countLabel = 0
        # Code
        self.code = ''
        self.funcs = ''
        self.natives = ''
        self.inFunc = False
        self.inNatives = False
        # Lista de Temporales
        self.temps = []
        # Lista de Nativas
        self.printString = False
        self.compareString = False
        self.concatString = False
        self.potencia = False
        self.relacionales = ['>', '<', '>=', '<=']
        #Lista de Imports
        self.imports = []
        self.imports2 = ['fmt','math']
        
    def cleanAll(self):
        # Contadores
        self.countTemp = 0
        self.countLabel = 0
        # Code
        self.code = ''
        self.funcs = ''
        self.natives = ''
        self.inFunc = False
        self.inNatives = False
        # Lista de Temporales
        self.temps = []
        # Lista de Nativas
        self.printString = False
        self.compareString = False
        self.concatString = False
        self.potencia = False
        self.relationalString = False
        self.printArray = False
        #Lista de Imports
        self.imports = []
        self.imports2 = ['fmt','math']
        Generador.generator = Generador()

    
    #############
    # IMPORTS
    #############

    def setImport(self, lib):
        if lib in self.imports2:
            self.imports2.remove(lib)
        else:
            return

        ret = f'import(\n\t\"{lib}\"\n);\n'
        self.imports.append(ret)
    #############
    # CODE
    #############
    def getHeader(self):
        ret = '/*----HEADER----*/\npackage main;\n\n'
        if len(self.imports)>0:
            for temp in range(len(self.imports)):
                ret += self.imports[temp]
        if len(self.temps) > 0:
            ret += 'var '
            for temp in range(len(self.temps)):
                ret += self.temps[temp]
                if temp != (len(self.temps) - 1):
                    ret += ", "
            ret += " float64;\n"
        ret += "var P, H float64;\nvar stack [30101999]float64;\nvar heap [30101999]float64;\n\n"
        return ret

    def getCode(self):
        return f'{self.getHeader()}{self.natives}\n{self.funcs}\nfunc main(){{\n{self.code}\n}}'

    def codeIn(self, code, tab="\t"):
        if(self.inNatives):
            if(self.natives == ''):
                self.natives = self.natives + '/*-----NATIVES-----*/\n'
            self.natives = self.natives + tab + code
        elif(self.inFunc):
            if(self.funcs == ''):
                self.funcs = self.funcs + '/*-----FUNCS-----*/\n'
            self.funcs = self.funcs + tab +  code
        else:
            self.code = self.code + '\t' +  code

    def addComment(self, comment):
        self.codeIn(f'/* {comment} */\n')
    
    def getInstance(self):
        if Generador.generator == None:
            Generador.generator = Generador()
        return Generador.generator

    def addSpace(self):
        self.codeIn("\n")
        

    ########################
    # Manejo de Temporales
    ########################
    def addTemp(self):
        temp = f't{self.countTemp}'
        self.countTemp += 1
        self.temps.append(temp)
        return temp

    #####################
    # Manejo de Labels
    #####################
    def newLabel(self):
        label = f'L{self.countLabel}'
        self.countLabel += 1
        return label

    def putLabel(self, label):
        self.codeIn(f'{label}:\n')
    
    def addIdent(self):
        self.codeIn("")

    ###################
    # GOTO
    ###################
    def addGoto(self, label):
        self.codeIn(f'goto {label};\n')
    
    ###################
    # IF
    ###################
    def addIf(self, left, right, op, label):
        self.codeIn(f'if {left} {op} {right} {{goto {label};}}\n')

    ###################
    # EXPRESIONES
    ###################
    def addExp(self, result, left, right, op):
        self.codeIn(f'{result} = {left} {op} {right};\n')
    
    def addModulo(self, result, left, right):
        self.codeIn(f'{result} = math.Mod({left}, {right});\n')
    
    def addAsig(self, result, left):
        self.codeIn(f'{result} = {left};\n')
    ###################
    # FUNCS
    ###################
    def addBeginFunc(self, id):
        if(not self.inNatives):
            self.inFunc = True
        self.codeIn(f'func {id}(){{\n', '')
    
    def addEndFunc(self):
        self.codeIn('return;\n}\n');
        if(not self.inNatives):
            self.inFunc = False

    ###############
    # STACK
    ###############
    def setStack(self, pos, value):
        self.codeIn(f'stack[int({pos})]={value};\n')
    
    def getStack(self, place, pos):
        self.codeIn(f'{place}=stack[int({pos})];\n')

    #############
    # ENVS
    #############
    def newEnv(self, size):
        self.codeIn(f'P=P+{size};\n')

    def callFun(self, id):
        self.codeIn(f'{id}();\n')

    def retEnv(self, size):
        self.codeIn(f'P=P-{size};\n')

    ###############
    # HEAP
    ###############
    def setHeap(self, pos, value):
        self.codeIn(f'heap[int({pos})] = {value};\n')

    def getHeap(self, place, pos):
        self.codeIn(f'{place} = heap[int({pos})];\n')

    def nextHeap(self):
        self.codeIn('H=H+1;\n')

    # INSTRUCCIONES
    def addPrint(self, type, value):
        self.setImport('fmt')
        self.codeIn(f'fmt.Printf("%{type}", int({value}));\n')
    
    def printFloat(self, type, value):
        self.setImport('fmt')
        self.codeIn(f'fmt.Printf("%{type}", {value});\n')
    
    def printTrue(self):
        self.setImport('fmt')
        self.addIdent()
        self.addPrint("c", 116)
        self.addIdent()
        self.addPrint("c", 114)
        self.addIdent()
        self.addPrint("c", 117)
        self.addIdent()
        self.addPrint("c", 101)

    def printFalse(self):
        self.setImport('fmt')
        self.addIdent()
        self.addPrint("c", 102)
        self.addIdent()
        self.addPrint("c", 97)
        self.addIdent()
        self.addPrint("c", 108)
        self.addIdent()
        self.addPrint("c", 115)
        self.addIdent()
        self.addPrint("c", 101)
    
    ##############
    # NATIVES
    ##############
    
    def ftoString(self):
        if self.toString:
            return
        self.inNatives = True
        self.addBeginFunc('toString')

        self.inNatives = False
    
    def fPrintString(self):
        self.setImport('fmt')
        if(self.printString):
            return
        self.printString = True
        self.inNatives = True

        self.addBeginFunc('printString')
        # Label para salir de la funcion
        returnLbl = self.newLabel()
        # Label para la comparacion para buscar fin de cadena
        compareLbl = self.newLabel()
        # Temporal puntero a Stack
        tempP = self.addTemp()
        # Temporal puntero a Heap
        tempH = self.addTemp()
        self.addExp(tempP, 'P', '1', '+')
        self.getStack(tempH, tempP)
        # Temporal para comparar
        tempC = self.addTemp()
        self.putLabel(compareLbl)
        self.addIdent()
        self.getHeap(tempC, tempH)
        self.addIdent()
        self.addIf(tempC, '-1', '==', returnLbl)
        self.addIdent()
        self.addPrint('c', tempC)
        self.addIdent()
        self.addExp(tempH, tempH, '1', '+')
        self.addIdent()
        self.addGoto(compareLbl)
        self.putLabel(returnLbl)
        self.addEndFunc()
        self.inNatives = False
    
    def fcompareString(self):
        if self.compareString:
            return
        self.compareString = True
        self.inNatives = True

        self.addBeginFunc("compareString")
        # Label para salir de la funcion
        returnLbl = self.newLabel()

        t2 = self.addTemp()
        self.addExp(t2, 'P', '1', '+')
        t3 = self.addTemp()
        self.getStack(t3, t2)
        self.addExp(t2,t2,'1', '+')
        t4 = self.addTemp()
        self.getStack(t4, t2)

        l1 = self.newLabel()
        l2 = self.newLabel()
        l3 = self.newLabel()
        self.putLabel(l1)

        t5 = self.addTemp()
        self.addIdent()
        self.getHeap(t5,t3)

        t6 = self.addTemp()
        self.addIdent()
        self.getHeap(t6,t4)

        self.addIdent()
        self.addIf(t5,t6,'!=', l3)
        self.addIdent()
        self.addIf(t5,'-1', '==', l2)

        self.addIdent()
        self.addExp(t3, t3,'1', '+')
        self.addIdent()
        self.addExp(t4, t4,'1','+')
        self.addIdent()
        self.addGoto(l1)

        self.putLabel(l2)
        self.addIdent()
        self.setStack('P', '1')
        self.addIdent()
        self.addGoto(returnLbl)
        self.putLabel(l3)
        self.addIdent()
        self.setStack('P', '0')
        self.putLabel(returnLbl)
        self.addEndFunc()
        self.inNatives = False
    
    def fconcatString(self):
        if self.concatString:
            return
        self.concatString = True
        self.inNatives = True

        self.addBeginFunc('concatString')
        
        returnLbl = self.newLabel()
        Lbl1 = self.newLabel()
        Lbl2 = self.newLabel()
        Lbl3 = self.newLabel()
        t3 = self.addTemp()
        t4 = self.addTemp()
        t5 = self.addTemp()
        t6 = self.addTemp()
        t7 = self.addTemp()

        self.addExp(t3, 'H',"","")
        self.addExp(t4,'P','1','+')
        self.getStack(t6, t4)
        self.addExp(t5, 'P', '2', '+')

        self.putLabel(Lbl1)
        self.addIdent()

        self.getHeap(t7, t6)
        self.addIdent()
        self.addIf(t7, '-1','==', Lbl2)
        self.addIdent()
        self.setHeap('H', t7)
        self.addIdent()
        self.addExp('H', 'H','1','+')
        self.addIdent()
        self.addExp(t6,t6,'1', '+')
        self.addIdent()
        self.addGoto(Lbl1)

        self.putLabel(Lbl2)

        self.addIdent()
        self.getStack(t6,t5)

        self.putLabel(Lbl3)
        self.addIdent()
        self.getHeap(t7, t6)
        self.addIdent()
        self.addIf(t7, '-1','==', returnLbl)
        self.addIdent()
        self.setHeap('H', t7)
        self.addIdent()
        self.addExp('H', 'H','1','+')
        self.addIdent()
        self.addExp(t6,t6,'1', '+')
        self.addIdent()
        self.addGoto(Lbl3)

        self.putLabel(returnLbl)
        self.addIdent()
        self.setHeap('H', '-1')
        self.addIdent()
        self.addExp('H', 'H','1', '+')
        self.addIdent()
        self.setStack('P', t3)
        self.addEndFunc()
        self.inNatives = False

    def fPotencia(self):
        if self.potencia:
            return
        self.potencia = True
        self.inNatives = True
        self.addBeginFunc('potencia')

        # Labels a utilizar
        Lbl0 = self.newLabel()
        Lbl1 = self.newLabel()
        Lbl2 = self.newLabel()
        Lbl3 = self.newLabel()

        # Temporales a utilizar
        t1 = self.addTemp()
        t2 = self.addTemp()
        t3 = self.addTemp()
        t4 = self.addTemp()

        #Escritura del codigo
        self.addExp(t2, 'P', '1','+')
        self.getStack(t1, t2)
        self.addExp(t3,t1,'','')
        self.addExp(t4,t1,'','')
        self.addExp(t2,'P','2','+')
        self.getStack(t1,t2)
        self.addIf(t1,'0','==', Lbl1)
        self.putLabel(Lbl2)
        self.addIdent()
        self.addIf(t1, '1','<=',Lbl0)
        self.addIdent()
        self.addExp(t3, t3,t4,'*')
        self.addIdent()
        self.addExp(t1,t1,'1', '-')
        self.addIdent()
        self.addGoto(Lbl2)
        self.putLabel(Lbl0)
        self.addIdent()
        self.setStack('P', t3)
        self.addIdent()
        self.addGoto(Lbl3)
        self.putLabel(Lbl1)
        self.addIdent()
        self.setStack('P', '1')
        self.putLabel(Lbl3)
        self.addEndFunc()
        self.addSpace()
        self.inNatives = False

    def frelationalString(self, op):
        if op in self.relacionales:
            self.relacionales.remove(op)
        else:
            return
        
        if op == '>':
            self.addBeginFunc('relationalStringM')
        elif op == '<':
            self.addBeginFunc('relationalStringm')
        elif op == '>=':
            self.addBeginFunc('relationalStringMI')
        elif op == '<=':
            self.addBeginFunc('relationalStringmI')


        t2 = self.addTemp()
        t3 = self.addTemp()
        t4 = self.addTemp()
        t5 = self.addTemp()
        t6 = self.addTemp()
        t7 = self.addTemp()
        t8 = self.addTemp()

        Lbl1 = self.newLabel()
        Lbl2 = self.newLabel()
        Lbl3 = self.newLabel()
        Lbl4 = self.newLabel()
        Lbl5 = self.newLabel()
        Lbl6 = self.newLabel()

        self.addExp(t2, 'P', '1','+')
        self.getStack(t3, t2)
        self.addExp(t2, t2,'1','+')
        self.getStack(t4, t2)
        self.addExp(t5,'0','','')
        self.addExp(t7,'0','','')
        
        
        self.putLabel(Lbl1)
        self.addIdent()
        self.getHeap(t6, t3)
        self.addIdent()
        self.addIf(t6, '-1','==', Lbl2)
        self.addIdent()
        self.addExp(t5, t5, t6, '+')
        self.addIdent()
        self.addExp(t3, t3,'1','+')
        self.addIdent()
        self.addGoto(Lbl1)

        
        self.putLabel(Lbl2)
        self.addIdent()
        self.getHeap(t8,t4)
        self.addIdent()
        self.addIf(t8,'-1','==', Lbl3)
        self.addIdent()
        self.addExp(t7,t7,t8,'+')
        self.addIdent()
        self.addExp(t4,t4,'1','+')
        self.addIdent()
        self.addGoto(Lbl2)

        self.putLabel(Lbl3)
        self.addIdent()
        self.addIf(t5, t7,op, Lbl4)
        self.addIdent()
        self.addGoto(Lbl5)

        self.putLabel(Lbl4)
        self.addIdent()
        self.setStack('P', '1')
        self.addIdent()
        self.addGoto(Lbl6)

        self.putLabel(Lbl5)
        self.addIdent()
        self.setStack('P', '0')
        
        self.putLabel(Lbl6)
        self.addEndFunc()
        self.addSpace()

        self.inNatives = False

    def fPrintArray(self):
        if self.printArray:
            return
        self.printArray = True
        self.inNatives = True

        self.addBeginFunc('printArray')

        self.inNatives = False


