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
        Generador.generator = Generador()
    
    #############
    # CODE
    #############
    def getHeader(self):
        ret = '/*----HEADER----*/\npackage main;\n\nimport (\n\t"fmt"\n)\n\n'
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
        self.codeIn(f'{result}={left}{op}{right};\n')
    
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
        self.codeIn(f'heap[int({pos})]={value};\n')

    def getHeap(self, place, pos):
        self.codeIn(f'{place}=heap[int({pos})];\n')

    def nextHeap(self):
        self.codeIn('H=H+1;\n')

    # INSTRUCCIONES
    def addPrint(self, type, value):
        self.codeIn(f'fmt.Printf("%{type}", int({value}));\n')
    
    def printFloat(self, type, value):
        self.codeIn(f'fmt.Printf("%{type}", {value});\n')
    
    def printTrue(self):
        self.addIdent()
        self.addPrint("c", 116)
        self.addIdent()
        self.addPrint("c", 114)
        self.addIdent()
        self.addPrint("c", 117)
        self.addIdent()
        self.addPrint("c", 101)

    def printFalse(self):
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
    def fPrintString(self):
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
        
        t3 = self.addTemp()
        t4 = self.addTemp()

    def fPotencia(self):
        if self.pontencia:
            return
        self.potencia = True
        self.inNatives = True
        #Aqui va todo el codigo para la potencia 
        self.inNatives = False
