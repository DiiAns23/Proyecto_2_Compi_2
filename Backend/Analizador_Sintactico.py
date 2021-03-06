from Abstract.Tipo import *
from Expresiones.Struct import Struct
from Instrucciones.Declaracion_Structs import *
from Nativas.LowerCase import *
from Nativas.UpperCase import *
from Nativas.Float import *
from Nativas.Trunc import Trunc
from Expresiones.Llamada_Funcion import *
from Instrucciones.Funcion import Funcion
from Instrucciones.Asignacion_Arrays import *
from Nativas.Length import *
from Expresiones.Array import Array
from Instrucciones.Break import *
from Instrucciones.Continue import *
from Instrucciones.Return import *
from Instrucciones.For import *
from Instrucciones.While import *
from Instrucciones.Declaracion_Arrays import *
from Instrucciones.If import *
from Expresiones.Relacionales import *
from TablaSimbolos.Arbol import *
from TablaSimbolos.Excepcion import *
from Expresiones.Variable import *
from Instrucciones.Declaracion import *
from Expresiones.Primitivos import *
from Expresiones.Logicas import *
from Expresiones.Aritmeticas import *
from Instrucciones.Imprimir import *
from TablaSimbolos.Tabla_Simbolos import *
from TablaSimbolos.Generador import *
import ply.yacc as yacc
import ply.lex as lex
from Analizador_Lexico import tokens
from Analizador_Lexico import lexer, errores
from Analizador_Lexico import find_column


# Asociación de operadores y precedencia
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right','UNOT'),
    ('left', 'IGUALDAD', 'DIFERENTE'),
    ('left', 'MENOR', 'MAYOR', 'MAYORI', 'MENORI'),
    ('left','MAS','MENOS','COMA'),
    ('left','POR','DIV', 'MOD'),
    ('left','PARI', 'PARD'),
    ('left','POT'),
    ('right','UMENOS'),
    )


# Definicion de la Gramatica
def p_init(t):
    'init : instrucciones'
    t[0] = t[1]
    return t[0]

def p_instrucciones_lista(t):
    '''instrucciones    : instrucciones instruccion
                        |   instruccion'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[1].append(t[2])
        t[0] = t[1]


def p_instrucciones_evaluar(t):
    '''instruccion : imprimir PTCOMA
                    | declaracion_instr PTCOMA
                    | declaracion_local PTCOMA
                    | declaracion_global PTCOMA
                    | declaracion_function PTCOMA
                    | inmutable_struct PTCOMA
                    | mutable_struct PTCOMA
                    | asignacion_struct PTCOMA
                    | llamada_function PTCOMA
                    | llamada_function
                    | condicional_ifs REND PTCOMA
                    | loop_while PTCOMA
                    | loop_for PTCOMA
                    | r_return PTCOMA
                    | r_break  PTCOMA
                    | r_continue PTCOMA
                    | asignacion_array PTCOMA
                    '''
    t[0] = t[1]

def p_imprimir(t):
    '''imprimir : RPRINT PARI parametros_ll PARD
                | RPRINT2 PARI parametros_ll PARD'''
    if t[1] == "print":
        t[0] = Imprimir(t[3], t.lineno(2), find_column(input, t.slice[2]))
    else:
        t[0] = Imprimir(t[3], t.lineno(2), find_column(input, t.slice[2]), True)

def p_imprimir2(t):
    '''imprimir : RPRINT PARI PARD
                | RPRINT2 PARI PARD'''
    if t[1] == "print":
        t[0] = Imprimir(None, t.lineno(2), find_column(input, t.slice[2]))
    else:
        t[0] = Imprimir(None, t.lineno(2), find_column(input, t.slice[2]), True)     

def p_declaracion_tipo(t):
    '''declaracion_instr : ID IGUAL expresion DPUNTOS DPUNTOS tipo'''
    t[0] = Declaracion(t[1], t[6], t.lineno(2),find_column(input, t.slice[2]),  t[3])
    #t[0] = Declaracion(t[1], t.lineno(2), find_column(input, t.slice[2]),t[6], t[3])

def p_declaracion_non_tipo(t):
    '''declaracion_instr : ID IGUAL expresion'''
    t[0] = Declaracion(t[1], None , t.lineno(2),find_column(input, t.slice[2]), t[3])
    #t[0] = Declaracion(t[1], t.lineno(2), find_column(input, t.slice[2]),None, t[3])

def p_declaracion_for(t):
    'declaracion_instr  :   ID'
    t[0] = Declaracion(t[1], None, t.lineno(1), find_column(input, t.slice[1]), None)

def p_declaracion_local(t):
    '''declaracion_local : RLOCAL ID'''
   # t[0] = Declaracion(t[2], t.lineno(1), find_column(input, t.slice[1]),None,None)

def p_declaracion_local1(t):
    '''declaracion_local : RLOCAL ID IGUAL expresion'''
    #t[0] = Declaracion(t[2], t.lineno(1), find_column(input, t.slice[1]),None,t[4])

def p_declaracion_global(t):
    'declaracion_global : RGLOBAL ID'
    #t[0] = Declaracion(t[2], t.lineno(1), find_column(input, t.slice[1]),None,None)

def p_declaracion_global1(t):
    '''declaracion_global : RGLOBAL ID IGUAL expresion'''
    #t[0] = Declaracion(t[2], t.lineno(1), find_column(input, t.slice[1]),None,t[4])

def p_declaracion_array(t):
    'declaracion_instr : ID IGUAL CORI parametros_ll CORD'
    t[0] = Declaracion_Arrays(t[1], t.lineno(2),find_column(input, t.slice[2]), t[4])
    #t[0] = Declaracion(t[1], t.lineno(1), find_column(input, t.slice[1]), TIPO.ARRAY, t[4])

def p_declaracion_array_2(t):
    'declaracion_instr : ID IGUAL CORI parametros_ll CORD DPUNTOS DPUNTOS tipo'
    t[0] = Declaracion_Arrays(t[1], t.lineno(2),find_column(input, t.slice[2]), t[4], t[8])

def p_asignacion_array(t):
    'asignacion_array : ID arrays_1 IGUAL expresion'
    t[0] = Asignacion_Arrays(t[1], t[2], t[4],t.lineno(1), find_column(input, t.slice[1]))

def p_inmutable_struct(t):
    'inmutable_struct : RSTRUCT ID params_structs REND'
    #t[0] = Declaracion_Struct(t[2], t.lineno(1), find_column(input, t.slice[1]),False,t[3])

def p_mutable_struct(t):
    'mutable_struct : RMUTABLE RSTRUCT ID params_structs REND'
    t[0] = Declaracion_Sructs(True,t[3],t[4], t.lineno(1), find_column(input, t.slice[1]))

def p_asignacion_struct(t):
    'asignacion_struct : ID PUNTO asignacion_params IGUAL expresion'
    #t[0] = Asignacion_Struct(t[1], t.lineno(1), find_column(input, t.slice[1]), t[3], t[5])

def p_declaracion_aux1(t):
    'declaracion_aux  :   ID PTCOMA'
    t[0] = Declaracion(t[1],None, t.lineno(1), find_column(input, t.slice[1]),None)
    
def p_declaracion_aux2(t):
    'declaracion_aux  :   ID DPUNTOS DPUNTOS tipo PTCOMA'
    t[0] = {'ide':t[1], 'tipo':t[4]}

def p_llamada_function_1(t):
    'llamada_function : ID PARI parametros_ll PARD' # [3,4,"Diego", [1,2,3,4,suma(3,2)], a[2]]
    t[0] = Llamada_Funcion(t[1],t[3], t.lineno(1), find_column(input, t.slice[1]))

def p_llamada_function_2(t):
    'llamada_function : ID PARI PARD'
    t[0] = Llamada_Funcion(t[1], [], t.lineno(1), find_column(input, t.slice[1]))

def p_declaracion_function_1(t):
    '''declaracion_function : RFUNCTION ID PARI parametros PARD instrucciones REND'''
    t[0] = Funcion(t[2], t[4], t[6],Tipo.NULO, t.lineno(2), find_column(input, t.slice[1]))

def p_declaracion_function_2(t):
    '''declaracion_function : RFUNCTION ID PARI PARD instrucciones REND'''
    t[0] = Funcion(t[2], [], t[5], Tipo.NULO, t.lineno(2), find_column(input, t.slice[1]))

def p_declaracion_function_3(t):
    '''declaracion_function : RFUNCTION ID PARI PARD DPUNTOS DPUNTOS tipo instrucciones REND'''
    t[0] = Funcion(t[2], [], t[8], t[7], t.lineno(2), find_column(input, t.slice[1]))

def p_declaracion_function_4(t):
    '''declaracion_function : RFUNCTION ID PARI parametros PARD DPUNTOS DPUNTOS tipo instrucciones REND'''
    t[0] = Funcion(t[2], t[4], t[9], t[8], t.lineno(2), find_column(input, t.slice[1]))

def p_condicional_if_0(t):
    'condicional_ifs : RIF condicional_if'
    t[0] = t[2]

def p_condicional_if_1(t):
    '''condicional_if : expresion instrucciones'''
    t[0] = If(t[1], t[2], None, None,-1,-1)

def p_condicional_if_2(t):
    '''condicional_if : expresion instrucciones RELSE instrucciones'''
    t[0] = If(t[1], t[2],t[4], None,-1,-1)

def p_condicional_if_3(t):
    '''condicional_if : expresion instrucciones RELSEIF condicional_if'''
    t[0] = If(t[1],t[2],None, t[4], -1, -1)

def p_loop_while_1(t):
    '''loop_while : RWHILE expresion instrucciones REND'''
    t[0] = While(t[2], t[3], t.lineno(1), find_column(input, t.slice[1]))

def p_loop_for_1(t):
    '''loop_for : RFOR declaracion_instr RIN rango instrucciones REND'''
    t[0] = For(t[2], t[4], t[5], t.lineno(1), find_column(input, t.slice[1]))

def p_loop_for_2(t):
    '''loop_for : RFOR declaracion_instr RIN expresion instrucciones REND'''
    t[0] = For(t[2], [t[4]], t[5], t.lineno(1), find_column(input, t.slice[1]))


def p_return(t):
    'r_return : RRETURN expresion'
    t[0] = ReturnE(t[2], t.lineno(1), find_column(input, t.slice[1]))

def p_break(t):
    'r_break : RBREAK'
    t[0] = Break(t.lineno(1), find_column(input, t.slice[1]))

def p_continue(t):
    'r_continue : RCONTINUE'
    t[0] = Continue(t.lineno(1), find_column(input, t.slice[1]))

def p_rango(t):
    'rango : expresion DPUNTOS expresion'
    t[0] = [t[1], t[3]]
    
def p_params(t):
    'parametros : parametros COMA parametro'
    t[1].append(t[3])
    t[0] = t[1]

def p_params1(t):
    'parametros : parametro'
    t[0] = [t[1]]

def p_params2(t):
    'parametro : ID DPUNTOS DPUNTOS tipo'
    t[0] = {'tipo': t[4], 'ide': t[1]}

def p_params3(t):
    'parametro : ID'
    t[0] = {'tipo': "NoTipo" , 'ide':t[1]}

def p_params4(t):
    'parametros_ll : parametros_ll COMA parametro_ll'
    t[1].append(t[3])
    t[0] = t[1]

def p_params5(t):
    'parametros_ll : parametro_ll'
    t[0] = [t[1]]

def p_params6(t):
    '''parametro_ll : expresion'''
    t[0] = t[1]

def p_params7(t):
    'arrays_1 :  arrays_1 CORI arrays_2 CORD'
    t[1].append(t[3])
    t[0] = t[1]

def p_params8(t):
    'arrays_1 : CORI arrays_2 CORD'
    t[0] = [t[2]]

def p_params9(t):
    'arrays_2 : expresion'
    t[0] = t[1]

def p_params10(t):
    'params_structs : params_structs param_structs'
    t[1].append(t[2])
    t[0] = t[1]

def p_params11(t):
    'params_structs : param_structs'
    t[0] = [t[1]]

def p_params12(t):
    'param_structs : declaracion_aux'
    t[0] = t[1]

def p_params13(t):
    'asignacion_params : asignacion_params PUNTO asignacion_param'
    t[1].append(t[3])
    t[0] = t[1]

def p_params14(t):
    'asignacion_params : asignacion_param'
    t[0] = [t[1]]

def p_params15(t):
    'asignacion_param  : expresion'
    t[0] = t[1]


def p_expresion_binaria(t):
    '''expresion : expresion MAS expresion
                  | expresion MENOS expresion
                  | expresion POR expresion
                  | expresion DIV expresion
                  | expresion OR expresion
                  | expresion AND expresion
                  | expresion IGUALDAD expresion
                  | expresion DIFERENTE expresion
                  | expresion MAYOR expresion
                  | expresion MENOR expresion
                  | expresion MAYORI expresion
                  | expresion MENORI expresion
                  | expresion POT expresion
                  | expresion MOD expresion
                  '''
    if t[2] == '+'  : 
        t[0] = Aritmeticas(t[1], t[3], OperadorAritmetico.MAS, t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '-':
        t[0] = Aritmeticas(t[1], t[3], OperadorAritmetico.MEN, t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '*': 
        t[0] = Aritmeticas(t[1], t[3], OperadorAritmetico.POR, t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '/': 
        t[0] = Aritmeticas(t[1], t[3], OperadorAritmetico.DIV, t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '^': 
        t[0] = Aritmeticas(t[1], t[3], OperadorAritmetico.POT, t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '%': 
        t[0] = Aritmeticas(t[1], t[3], OperadorAritmetico.MOD, t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '==': 
        t[0] = Relacionales(t[1], t[3], OperadorRelacional.IGUALDAD,t.lineno(2), find_column(input, t.slice[2]) )
    elif t[2] == '!=': 
        t[0] = Relacionales(t[1], t[3], OperadorRelacional.DIFERENTE,t.lineno(2), find_column(input, t.slice[2]) )
    elif t[2] == '>': 
        t[0] = Relacionales(t[1], t[3], OperadorRelacional.MAYOR,t.lineno(2), find_column(input, t.slice[2]) )
    elif t[2] == '<': 
        t[0] = Relacionales(t[1], t[3], OperadorRelacional.MENOR,t.lineno(2), find_column(input, t.slice[2]) )
    elif t[2] == '>=': 
        t[0] = Relacionales(t[1], t[3], OperadorRelacional.MAYORI,t.lineno(2), find_column(input, t.slice[2]) )
    elif t[2] == '<=':
        t[0] = Relacionales(t[1], t[3], OperadorRelacional.MENORI,t.lineno(2), find_column(input, t.slice[2]) )
    elif t[2] == '||':
        t[0] = Logicas(t[1], t[3],OperadorLogico.OR, t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '&&': 
        t[0] = Logicas(t[1], t[3],OperadorLogico.AND, t.lineno(2), find_column(input, t.slice[2]))


def p_expresion_unaria(t):
    '''expresion : MENOS expresion %prec UMENOS
                    | NOT expresion %prec UNOT'''
    if t[1] == '-':
        t[0] = Aritmeticas(None, t[2], OperadorAritmetico.UME, t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == '!':
        t[0] = Logicas(t[2], None,OperadorLogico.NOT,  t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_agrupacion(t):
    'expresion : PARI expresion PARD'
    t[0] = t[2]

def p_expresion_identificador(t):
    '''expresion : ID'''
    t[0] = Variable(t[1], t.lineno(1),find_column(input, t.slice[1]))

def p_expresion_array(t):
    'expresion : ID arrays_1'
    t[0] = Array(t[1],t[2], t.lineno(1), find_column(input, t.slice[1]) )

def p_expresion_struct(t):
    'expresion : ID PUNTO asignacion_params'
    t[0] = Struct(t[1],t[3], t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_array_4(t):
    'expresion : CORI parametros_ll CORD'
    t[0] = Declaracion_Arrays('',t.lineno(1), find_column(input, t.slice[1]),t[2])

def p_expresion_entero(t):
    'expresion : ENTERO'
    t[0] = Primitivos(int(t[1]), Tipo.INT, t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_decimal(t):
    'expresion : DECIMAL'
    t[0] = Primitivos(float(t[1]), Tipo.FLOAT, t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_char(t):
    'expresion : CHAR'
    t[0] = Primitivos(t[1], Tipo.CHAR, t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_cadena(t):
    'expresion : CADENA'
    t[0] = Primitivos(str(t[1]), Tipo.STRING, t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_true(t):
    'expresion : RTRUE'
    t[0] = Primitivos(True,Tipo.BOOL, t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_false(t):
    'expresion : RFALSE'
    t[0] = Primitivos(False,Tipo.BOOL, t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_llam(t):
    'expresion : llamada_function'
    t[0] = t[1]

def p_tipo(t):
    '''tipo : RINT
            | RFLOAT
            | RBOOL
            | RCHAR
            | RSTRING
            | ID'''
    if t[1] ==  "Int64":
        t[0] = Tipo.INT
    elif t[1] == "Float64":
        t[0] = Tipo.FLOAT
    elif t[1] == "Bool":
        t[0] = Tipo.BOOL
    elif t[1] == "Char":
        t[0] = Tipo.CHAR
    elif t[1] == "String":
        t[0] = Tipo.STRING
    else:
        t[0] = [Tipo.STRUCT, t[1]]
    
def p_tipo_2(t):
    '''tipo : tipo LLI tipo LLD '''
    t[1].append(t[3])
    t[0] = t[1]

def p_tipo_3(t):
    '''tipo : tipo_2'''
    t[0] = [t[1]]

def p_tipo_4(t):
    '''tipo_2 : RLIST'''
    t[0] = Tipo.ARRAY

def agregarNativas(ast):
    nombre = "uppercase"
    params = [{'tipo':Tipo.STRING, 'ide':'uppercase##Param1'}]
    inst = []
    upper = UpperCase(nombre, params, inst, Tipo.STRING, -1, -1)
    ast.setFunciones('uppercase',upper)

    nombre = "lowercase"
    params = [{'tipo':Tipo.STRING, 'ide':'lowercase##Param1'}]
    lower = LowerCase(nombre, params, inst,Tipo.STRING, -1, -1)
    ast.setFunciones('lowercase',lower)

    nombre = "length"
    params = [{'tipo':Tipo.ARRAY, 'ide':'length##Param1'}]
    length = Length(nombre, params, inst,Tipo.INT, -1, -1)
    ast.setFunciones('length',length)

    nombre = "float"
    params = [{'tipo':Tipo.INT, 'ide':'float##Param1'}]
    floats = Float(nombre, params, inst,Tipo.FLOAT, -1, -1)
    ast.setFunciones('float', floats)

    nombre = "trunc"
    params = [{'tipo':Tipo.FLOAT, 'ide':'trunc##Param1'}]
    trunc = Trunc(nombre, params, inst, Tipo.INT, -1, -1)
    ast.setFunciones('trunc',  trunc)



    
def p_error(t):
    print(" Error sintáctico en'%s'" % t.value)

input = ''

def getErrores():
    return errores

def parse(inp):
    global errores
    global parser
    errores = []
    parser = yacc.yacc()
    global input
    input = inp
    lexer.lineno = 1
    return parser.parse(inp)

# f = open("Backend/entrada.jl", "r")
# entrada = f.read()
# print("ARCHIVO DE ENTRADA:")
# print("")
# print(entrada)
# print("")
# print("ARCHIVO DE SALIDA:")


# genAux = Generador()
# genAux.cleanAll()
# generador = genAux.getInstance()

# instrucciones = parse(entrada)
# ast = Arbol(instrucciones)
# TsgGlobal = Tabla_Simbolo()
# ast.setTSglobal(TsgGlobal)

# agregarNativas(ast)

# for instruccion in ast.getInst():
#     value = instruccion.compilar(ast, TsgGlobal)
#     if isinstance(value, Excepcion):
#         ast.setExcepciones(value)
# for error in ast.getExcepciones():
#     print(error.toString2())
# print(generador.getCode())

