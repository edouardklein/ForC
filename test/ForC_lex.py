import ply.lex as lex
import sys

states = (
    ('ORG','exclusive'),
    ('FORC','exclusive'),
    )

tokens = (
    'TEXT',
    'SHEBANG_l',
    'SHEBANG_dl',
    'SHEBANG_g',
    'SHEBANG_dg',
    'NAME',
    'ELEMENT',
)

def t_ORG_SHEBANG_l(t):
    r'\#\?l'
    lexer.begin('FORC')
    return t
def t_ORG_SHEBANG_dl(t):
    r'\#\?dl'
    lexer.begin('FORC')
    return t
def t_ORG_SHEBANG_g(t):
    r'\#\?g'
    lexer.begin('FORC')
    return t
def t_ORG_SHEBANG_dg(t):
    r'\#\?dg'
    lexer.begin('FORC')
    return t
def t_ORG_TEXT(t):
    r'.+'
    return t
def t_ORG_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
def t_FORC_ELEMENT(t):
    r"[^\S\n]*'[^']*'[^\S\n]*"
    return t
def t_FORC_NAME(t):
    r'[^\S\n]*[^\s]+[^\S\n]*'
    return t
def t_FORC_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.lexer.begin('ORG')

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
# Error handling rules
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
def t_ORG_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
def t_FORC_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
lexer.begin('ORG')
# Give the lexer some input
#lexer.input(open(sys.argv[1]).read())

# Tokenize
#while True:
#    tok = lexer.token()
#    if not tok: break      # No more input
#    #print(tok.value,end='')
#    print(tok)

