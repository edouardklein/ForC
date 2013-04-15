import ply.lex as lex
import sys

states = (
    ('ORG','exclusive'),
    ('FORC1','exclusive'),
    ('FORC2','exclusive'),
    ('FORC3','exclusive'),
    )

tokens = (
    'TEXT',
    'SHEBANG',
    'REGEX',
    'EXAMPLE',
    'MEANING',
)

def t_ORG_SHEBANG(t):
    r'\#\?d'
    lexer.begin('FORC1')
    return t
def t_ORG_TEXT(t):
    r'.+'
    return t
def t_ORG_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
def t_FORC1_REGEX(t):
    r'\s*[^\s]+\s*'
    lexer.begin('FORC2')
    lexer.under_construction_element = [t.value]
    return t
def t_FORC2_EXAMPLE(t):
    r'\s*[^\s]+\s*'
    lexer.begin('FORC3')
    lexer.under_construction_element.append(t.value)
    return t
def t_FORC3_MEANING(t):
    r'.+'
    lexer.begin('ORG')
    lexer.under_construction_element.append(t.value)
    lexer.elements.append(lexer.under_construction_element)
    return t

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
def t_FORC1_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
def t_FORC2_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
def t_FORC3_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



# Build the lexer
lexer = lex.lex()
lexer.under_construction_element = []
lexer.elements = []
lexer.begin('ORG')
# Give the lexer some input
lexer.input(open(sys.argv[1]).read())

# Tokenize
while True:
    tok = lexer.token()
    if not tok: break      # No more input
    #print(tok.value,end='')
    print(tok)

print lexer.elements
