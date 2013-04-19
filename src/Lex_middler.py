)

#ORG_MODE tokens
def t_ORG_COMMENT(t):
    r'[^\S\n]*\#.*\n'
    t.lexer.lineno += 1
    return t
def t_ORG_ACTUAL_DOLLAR(t):
    r'\\\$'
    return t
def t_ORG_BACKSLASH(t):
    r'\\'
    return t
def t_ORG_DOLLAR(t):
    r'\$'
    t.lexer.begin('MATH')
    return t
def t_ORG_TEXT(t):
    r'[^\$\n\\]+'
    return t
def t_ORG_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t
#Lexer-mechanics MATH token
def t_MATH_DOLLAR(t):
    r'\$'
    while True:
        try:
            anchor = lexer.dollar_label_stack.pop()
            t.value+="\n"+r'# <<'+anchor+r'>>'
        except IndexError:
            t.value+="\n"
            break
    t.lexer.begin('ORG')
    return t
#LaTeX tokens to be ignored
def t_MATH_LATEX_IGNORE(t):
    r'\{|\}'
    return t
#Conventional MATH tokens (everybody uses them, cumbersome to define in every document)
def t_MATH_PAREN(t):
    r'\(|\)'
    return t
def t_MATH_BRACE(t):
    r'\\\{|\\\}'
    return t
def t_MATH_BRACKET(t):
    r'\[|\]'
    return t
def t_MATH_COMMA(t):
    r','
    return t
def t_MATH_BLANK(t):
    r'\s+'
    return t
def t_MATH_EQUAL(t):
    r'='
    return t
def t_MATH_SUBSCRIPT(t):
    r'_'
    return t
def t_MATH_EXPONENT(t):
    r'\^'
    return t
def t_MATH_DASH(t):
    r"'"
    return t
def t_MATH_KNOWING(t):
    r'\|'
    return t
def t_MATH_NUMBER(t):
    r'[0-9]+'
    return t
def t_MATH_LEQ(t):
    r'\\leq'
    return t
def t_MATH_IN(t):
    r'\\in'
    return t
def t_MATH_SUM(t):
    r'\\sum'
    return t

