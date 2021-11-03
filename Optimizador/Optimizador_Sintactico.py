from Optimizacion.Expresiones.Acceso import *
from Optimizacion.Expresiones.Expresion import *
from Optimizacion.Expresiones.Variable import *
from Optimizacion.Gotos.Goto import *
from Optimizacion.Gotos.If import *
from Optimizacion.Instrucciones.Asignacion import *
from Optimizacion.Instrucciones.Funcion import *
from Optimizacion.Instrucciones.Label import *
from Optimizacion.Instrucciones.Llamada_Funcion import *
from Optimizacion.Instrucciones.Print import *
from Optimizacion.Instrucciones.Return import *
from Optimizacion.Optimizador import *

import ply.yacc as yacc
import ply.lex as lex
from Optimizador_Lexico import tokens
from Optimizador_Lexico import lexer, errores, find_column


precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'IGUALDAD', 'DIFERENTE'),
    ('left', 'MENOR', 'MAYOR', 'MAYORI', 'MENORI'),
    ('left','MAS','MENOS','COMA'),
    ('left','POR','DIV', 'MOD'),
    ('left','PARI', 'PARD'),
    ('left','POT'),
    )

# Definicion de la Gramatica

def p_init(t):
    'init : RPACKAGE ID PTCOMA imports declaraciones L_codigo'
    t[0] = Optimizador(t[4], t[5], t[6])

def p_init_2(t):
    'init : RPACKAGE ID PTCOMA declaraciones L_codigo'
    t[0] = Optimizador(None, t[5], t[6])

def p_imports(t):
    'imports : imports import'
    t[1].append(t[2])
    t[0] = t[1]

def p_imports2(t):
    'imports : import'
    t[0] = [t[1]]

def p_import3(t):
    'import : RIMPORT PARI CADENA PARD PTCOMA'
    t[0] = t[3]

def p_declaraciones(t):
    'declaraciones : declaraciones declaracion'
    t[1].append(t[2])
    t[0] = t[1]

def p_declaraciones2(t):
    'declaraciones : declaracion'
    t[0] = [t[1]]

def p_declaraciones3(t):
    'declaracion : RVAR temp_list CORI ENTERO CORD RFLOAT PTCOMA'
    t[0] = f'{t[2]}[{t[4]}] float64;'

def p_declaraciones4(t):
    'declaracion : RVAR temp_list tipo PTCOMA'
    t[0] = f'{t[2]} {t[3]};'

def p_Lista_Temps(t):
    '''temp_list : temp_list COMA ID'''
    t[0] = f'{t[1]}, {t[3]}'

def p_Lista_Temps2(t):
    '''temp_list : ID'''
    t[0] = f'{t[1]}'

def p_tipo(t):
    '''tipo : RINT
            | RFLOAT'''
    if t[1] == 'int':
        t[0] = "int"
    else:
        t[0] = "float64"

def p_codigo_1(t):
    'L_codigo : L_codigo codigo'
    t[1].append(t[2])
    t[0] = t[1]

def p_codigo_2(t):
    'L_codigo : codigo'
    t[0] = [t[1]]

def p_codigo_3(t):
    'codigo : code'
    t[0] = t[1]

def p_codigo_4(t):
    'code : RFUNC ID PARI PARD instrucciones'
    t[0] = Funcion(t[2], t[5],t.lineno(1), find_column(input, t.slice[1]) )

def p_codigo_5(t):
    'instrucciones : LLI instrucciones_2 LLD'
    t[0] = t[2]

def p_codigo_6(t):
    '''instrucciones_2 : instrucciones_2 instruccion
                        | instruccion'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[1].append(t[2])
        t[0] = t[1]

def p_codigo_7(t):
    '''instruccion  : asignacion PTCOMA
                    | label DPUNTOS
                    | gotoS PTCOMA
                    | llamada_funcion PTCOMA
                    | cond_if
                    | returnE PTCOMA
                    | printF PTCOMA
                    '''
    t[0] = t[1]

def p_label(t):
    '''label : ID'''
    t[0] = Label(t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_goto(t):
    'gotoS : RGOTO ID'
    t[0] = Goto(t[2], t.lineno(1), find_column(input, t.slice[1]))

def p_return(t):
    'returnE : RRETURN'
    t[0] = Return(t.lineno(1), find_column(input, t.slice[1]))

def p_printF(t):
    'printF : RFMT PUNTO RPRINTF PARI CADENA COMA valor PARD'
    t[0] = Print(t[5], t[7],t.lineno(1), find_column(input, t.slice[1]))

def p_valor(t):
    '''valor : RINT PARI expresion PARD
            |   expresion'''
    
    if len(t) == 2:
        t[0] = t[1]
    else:
        t[3].haveInt = True
        t[0] = t[3]

def p_if(t):
    'cond_if : RIF expresion LLI RGOTO ID PTCOMA LLD'
    t[0]  = If(t[2], t[5], t.lineno(1), find_column(input, t.slice[1]))

def p_access(t):
    '''access :   ID CORI RINT PARI expresion PARD CORD
                | ID CORI expresion CORD'''
    if len(t) == 5:
        t[0] = Acceso(t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    else:
        t[0] = Acceso(t[1], t[5], t.lineno(2), find_column(input, t.slice[2]))
        t[0].haveInt = True

def p_assign(t):
    'asignacion : access IGUAL expresion'
    t[0] = Asignacion(t[1], t[3], t.lineno(2), t.lexpos(2))

def p_assign2(t):
    '''asignacion :   ID IGUAL expresion
                | ID IGUAL access'''
    aux = Variable(t[1], t.lineno(2), find_column(input, t.slice[2]))
    t[0] = Asignacion(aux, t[3], t.lineno(2), find_column(input, t.slice[2]))


def p_llamada_funcion(t):
    'llamada_funcion : ID PARI PARD'
    t[0] = Llamada_Funcion(t[1], t.lineno(1), find_column(input, t.slice[1]))

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
                  | expresion MOD expresion'''
    t[0] = Expresion(t[1], t[3], t[2], t.lineno(2), find_column(input, t.slice[2]))

def p_expresion_agrupacion(t):
    'expresion : PARI expresion PARD'
    t[0] = t[2]

def p_expresion_entero(t):
    '''expresion : ENTERO
                |   ID
                |   MENOS ENTERO
                |   DECIMAL'''
    if len(t) == 3:
        t[0] = Variable(0-t[2], t.lineno(1), find_column(input, t.slice[1]) )
    else:
        t[0] = Variable(t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_mod(t):
    'expresion : RMATH PUNTO RMOD PARI expresion COMA expresion PARD'
    t[0] = Variable(f'{t[1]}{t[2]}{t[3]}{t[4]}{t[5].value}{t[6]}{t[7].value}{t[8]}', t.lineno(1), find_column(input, t.slice[1]))


def p_error(t):
    print("Error sintáctico en'%s'" % t.value)

input = ''

def getErrores():
    return errores

def parse2(inp):
    global errores
    global parser
    errores = []
    parser = yacc.yacc()
    global input
    input = inp
    lexer.lineno = 1
    return parser.parse(inp)

# f = open("Optimizador/optimizar.txt", "r")
# entrada = f.read()
# print("ARCHIVO DE ENTRADA:")
# print("")
# # print(entrada)
# print("")
# print("ARCHIVO DE SALIDA:")
# a = parse2(entrada)
# a.Mirilla()
# print(a.getCode())
# print("Sin errores :3")

