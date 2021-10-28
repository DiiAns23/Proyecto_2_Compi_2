import ply.yacc as yacc
import ply.lex as lex
from Optimizador_Lexico import tokens

# Definicion de la Gramatica
def p_init(t):
    'init : RPACKAGE ID '
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