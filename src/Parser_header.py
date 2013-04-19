import ply.yacc as yacc
import sys
# Get the token map from the lexer.  This is required.
from ForC_tmp_lexer import tokens,lexer

#Org-derived grammar rules
def p_expression_org_text(p):
    'expression : TEXT'
    p[0] = p[1]

def p_expression_org_special_text(p):
    '''expression : expression ACTUAL_DOLLAR
                   | expression BACKSLASH'''
    p[0] = p[1] + p[2]

def p_expression_text_composition(p):
    '''expression : expression TEXT
                  | expression COMMENT
                  | expression newline'''
    p[0] = p[1]+p[2]
#Maths-rules
def p_expression_enclosed_math(p):
    'expression : expression DOLLAR math_expression DOLLAR'
    p[0] = p[1] + p[2] + p[3] + p[4]
    while True:
        try:
            anchor = parser.dollar_label_stack.pop()
            p[0] += r'# <<'+anchor+r'>>'+"\n"
        except IndexError:
            break
def p_math_expression_composition(p):
    'math_expression : math_expression math_expression'
    p[0] = p[1] + p[2]
#Conventional MATH grammar rules
def p_math_expression_sum(p):
    'math_expression : SUM SUBSCRIPT LATEX_IGNORE math_expression LATEX_IGNORE EXPONENT LATEX_IGNORE math_expression LATEX_IGNORE'
    p[0] =  p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7] + p[8] + p[9]
def p_math_power(p):
    'math_expression : math_expression EXPONENT math_expression'
    p[0] =  p[1] + p[2] + p[3] 
