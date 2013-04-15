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
    'BRACE',
    'COMMA',
    #Should be automatically added
    'STATE_SPACE',
    'ACTION_SPACE',
    'TRANSITION_PROBABILITIES',
    'REWARD_FUNCTION',
    'DISCOUNT_FACTOR',
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
#Conventional MATH tokens (everybody uses them, cumbersome to define in every document)
def t_MATH_BRACE(t):
    r'\\\{|\\\}'
    return t
def t_MATH_COMMA(t):
    r','
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
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: break      # No more input
    print(tok.value,end='')

print("* Notation table")
print("| *Symbol* | *Meaning* | *Defined* |")
for key in lexer.dic.keys():
    print("| ${}$ |{}|{}|".format(*(lexer.dic[key][:3])))
