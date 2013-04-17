
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Error handling rule
def t_error(t):
    print("Illegal character '%s' at l.%d, pos %d" % (t.value[0],t.lineno,t.lexpos))
    t.lexer.skip(1)
# Error handling rule
def t_ORG_error(t):
    print("Illegal character '%s' at l.%d, pos %d" % (t.value[0],t.lineno,t.lexpos))
    t.lexer.skip(1)
# Error handling rule
def t_MATH_error(t):
    print("Illegal character '%s' at l.%d, pos %d" % (t.value[0],t.lineno,t.lexpos))
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
lexer.dic = {}
lexer.dollar_label_stack = []
lexer.begin('ORG')

