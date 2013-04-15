# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from testLex import tokens,lexer

#Org-derived grammar rules
def p_expression_org_text(p):
    'expression : TEXT'
    p[0] = p[1]

def p_expression_org_special_text(p):
    '''expression : expression ACTUAL_DOLLAR
                   | expression BACKSLASH'''
    p[0] = p[1] + p[2]

def p_expression_text_composition(p):
    'expression : expression TEXT'
    p[0] = p[1]+p[2]
#Maths-rules
def p_expression_enclosed_math(p):
    'expression : expression DOLLAR math_expression DOLLAR'
    p[0] = p[1] + p[2] + p[3] + p[4]

def p_math_expression_composition(p):
    'math_expression : math_expression math_expression'
    p[0] = p[1] + p[2]

#Automatically generated : all tokens that are OK by themselves (whether they come from the user or from the basic tokens does not matter)
def p_math_expression_tokens(p):
    '''math_expression : LATEX_IGNORE
                       | PAREN
                       | BRACE
                       | COMMA
                       | BLANK
                       | EQUAL
                       | SUBSCRIPT
                       | DASH
                       | KNOWING
                       | NUMBER
                       | LEQ
                       | IN
                       | STATE_SPACE
                       | ACTION_SPACE
                       | TRANSITION_PROBABILITIES
                       | REWARD_FUNCTION
                       | DISCOUNT_FACTOR
                       | PROB_FUNCTION
                       | PROB_MATRIX
                       | ACTION
                       | STATE
                       '''
    p[0] = p[1]
    
# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

data = r'''
A Markov Decision process (MDP) is a tuple
$\{\s,\A,\p,\R,\gamma\}$ where $\s$ is the finite state
space.
 $\A$ the finite actions space, $\p =
\{P_a = (p(s'|s,a))_{1\leq s,s'\leq |\s|}, a\in\A\}$
'''
# Build the parser
parser = yacc.yacc(debug=True)
print(parser.parse(data,debug=0))

print("* Notation table")
print("| *Symbol* | *Meaning* | *Defined* |")
for key in lexer.dic.keys():
    print("| ${}$ |{}|{}|".format(*(lexer.dic[key][:3])))
