import re
import ply.lex as lex

errores = []


reserved = {
    'float64'   :   'RFLOAT',
    'int'       :   'RINT',
    'func'      :   'RFUNC',
    'return'    : 'RRETUNR',
    'if'        : 'RIF',
    'goto'      : 'RGOTO',
    'fmt'       : 'RFMT',
    'printf'    : 'RPRINTF',
    'package'   : 'RPACKAGE',
    'import'    : 'RIMPORT',
    'var'       :   'RVAR'
}

tokens  = [
    'COMA',
    'PTCOMA',
    'PUNTO',
    'DPUNTOS',
    'PARI',
    'PARD',
    'MAS',
    'MENOS',
    'POR',
    'DIV',
    'POT',
    'MOD',
    'IGUAL',
    'IGUALDAD',
    'DIFERENTE',
    'MAYOR',
    'MENOR',
    'MAYORI',
    'MENORI',
    'OR',
    'AND',
    'NOT',
    'ENTERO',
    'DECIMAL',
    'CADENA',
    'CHAR',
    'ID',
    'CORI',
    'CORD'
]+ list(reserved.values())


#Identificador
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')# Check for reserved words
    return t

#Comentario Multilinea
def t_Com_Multiple(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    
#Nueva Linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Caracteres ignorados
t_ignore = " \t"

#Error
def t_error(t):
    t.lexer.skip(1)

def find_column(inp, tk):
    line_start = inp.rfind('\n', 0, tk.lexpos) + 1
    return (tk.lexpos - line_start) + 1

lexer = lex.lex(reflags = re.IGNORECASE)