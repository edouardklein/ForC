import ply.lex as lex

states = (
    ('ORG','exclusive'),
    ('MATH','exclusive'),
    )

tokens = (
    'BACKSLASH',
    'ACTUAL_DOLLAR',
    'TEXT',
    'DOLLAR',
    'PAREN',
    'BRACE',
    'COMMA',
    'BLANK',
    'EQUAL',
    'SUBSCRIPT',
    'DASH',
    'KNOWING',
    'LATEX_IGNORE',
    'LEQ',
    'NUMBER',
    'IN',
    #Should be automatically added
    'STATE',
    'ACTION',
    'STATE_SPACE',
    'ACTION_SPACE',
    'TRANSITION_PROBABILITIES',
    'REWARD_FUNCTION',
    'DISCOUNT_FACTOR',
    'PROB_MATRIX',
    'PROB_FUNCTION',
    #End of SBAA
)

#ORG_MODE tokens
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
    r'[^\$\\]+'
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
#########
#Tokens that should be automatically added after scanning the annotated document
#########
def t_MATH_STATE_SPACE(t):
    r'\\s' #<- User specified
    if not t.type in lexer.dic:
        lexer.dic[t.type] = [r'\s',"State space", #<- User specified, all the rest should be automatically generated
                             r"\ref{FORC_STATE_SPACE}",t.lineno,t.lexpos]
        lexer.dollar_label_stack.append("FORC_STATE_SPACE")
    return t
def t_MATH_ACTION_SPACE(t):
    r'\\A'
    if not t.type in lexer.dic:
        lexer.dic[t.type] = [r'\A',"Action Space", #<- User specified, all the rest should be automatically generated
                             r"\ref{FORC_ACTION_SPACE}",t.lineno,t.lexpos]
        lexer.dollar_label_stack.append("FORC_ACTION_SPACE")
    return t
def t_MATH_TRANSITION_PROBABILITIES(t):
    r'\\p'
    return t
def t_MATH_REWARD_FUNCTION(t):
    r'\\R'
    return t
def t_MATH_DISCOUNT_FACTOR(t):
    r'\\gamma'
    return t
def t_MATH_PROB_FUNCTION(t):
    r'p'
    return t
def t_MATH_PROB_MATRIX(t):
    r'P'
    return t
def t_MATH_ACTION(t):
    r'a'
    return t
def t_MATH_STATE(t):
    r's'
    return t
#########
#End of automatically added tokens
#########

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

data = r'''
A Markov Decision process (MDP) is a tuple
$\{\s,\A,\p,\R,\gamma\}$ where $\s$ is the finite state
space.
 $\A$ the finite actions space, $\p =
\{P_a = (p(s'|s,a))_{1\leq s,s'\leq |\s|}, a\in\A\}$
'''

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
# Error handling rule
def t_ORG_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
# Error handling rule
def t_MATH_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
lexer.dic = {}
lexer.dollar_label_stack = []
lexer.begin('ORG')
# Give the lexer some input
#lexer.input(data)

# Tokenize
#while True:
#    tok = lexer.token()
#    if not tok: break      # No more input
#    #print(tok)
#    print(tok.value,end='')

#print("* Notation table")
#print("| *Symbol* | *Meaning* | *Defined* |")
#for key in lexer.dic.keys():
#    print("| ${}$ |{}|{}|".format(*(lexer.dic[key][:3])))
