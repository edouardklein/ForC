# Yacc example

import ply.yacc as yacc
import sys

# Get the token map from the lexer.  This is required.
from ForC_lex import tokens,lexer

#Org-derived grammar rules
def p_expression_org_text(p):
    'expression : TEXT'

def p_expression_text_composition(p):
    'expression : expression TEXT'

#ForC grammar rules
def p_expression_definition_lexer_level(p):
    'expression : expression SHEBANG_dl NAME ELEMENT ELEMENT ELEMENT'
    parser.dic_dl[p[3]] = [p[4],p[5],p[6]]
def p_expression_definition_parser_level(p):
    'expression : expression SHEBANG_dg NAME ELEMENT ELEMENT ELEMENT'
    parser.dic_dg[p[3]] = [p[4].strip()[1:-1],p[5],p[6]]
def p_expression_silent_symbol_lexer_level(p):
    'expression : expression SHEBANG_l NAME ELEMENT'
    parser.dic_l[p[3]] = p[4]
def p_expression_silent_symbol_parser_level(p):
    'expression : expression SHEBANG_g NAME ELEMENT'
    parser.dic_g[p[3]] = p[4][1:-1]


# Build the parser
parser = yacc.yacc(debug=True)
parser.dic_dl = {}
parser.dic_dg = {}
parser.dic_l = {}
parser.dic_g= {}
#print()
parser.parse(open(sys.argv[1]).read(),debug=0)
#for i in [parser.dic_dl,parser.dic_dg,parser.dic_l,parser.dic_g]:
#    print(i)

G_RULE_TEMPLATE='''
def p_math_expression_{name}(p):
    \'\'\'{name} : {rule}\'\'\'
    i = 1
    p[0] = ''
    while True:
        try:
            p[0] += p[i]
            i+=1
        except IndexError:
            break
'''
if sys.argv[2]=='parser':
    for k in parser.dic_g.keys():
        print(G_RULE_TEMPLATE.format(name=k.strip(),
                                     rule=parser.dic_g[k].replace("|","\n\t\t|")),
              end='')

DG_RULE_TEMPLATE='''
def p_math_expression_{name}(p):
    \'\'\'math_expression : {rule}\'\'\'
    i = 1
    p[0] = ''
    while True:
        try:
            p[0] += p[i]
            i+=1
        except IndexError:
            break
    if not "{name}" in parser.dic:
        parser.dic["{name}"] = [r{notation},
                                {description},
                                r'\\ref{{FORC_{name}}}']
        parser.dollar_label_stack.append('FORC_{name}')
'''
if sys.argv[2]=='parser':
    for k in parser.dic_dg.keys():
        print(DG_RULE_TEMPLATE.format(name=k.strip(),
                                      rule = parser.dic_dg[k][0].replace("|","\n\t\t|"),
                                      notation = parser.dic_dg[k][1],
                                      description = parser.dic_dg[k][2]),
              end='')
TOKENS_RULE_TEMPLATE='''
def p_math_expression_tokens(p):
    \'\'\'math_expression : {tokens}\'\'\'
    p[0] = p[1]
'''
MATH_TOKENS= ['PAREN',
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
              'IN', #All above copied from Lexer_header.py
              ] + list(parser.dic_dl.keys()) + list(parser.dic_g.keys())
if sys.argv[2]=='parser':
    print(TOKENS_RULE_TEMPLATE.format(tokens="\n\t\t| ".join(MATH_TOKENS)))


if sys.argv[2]=='lexer1':
    for k in parser.dic_dl.keys():
        print("\t'"+k.strip()+"',")
    for k in parser.dic_l.keys():
        print("\t'"+k.strip()+"',")
    

L_RULE_TEMPLATE='''
def t_MATH_{name}(t):
    r{regex}
    return t
'''
if sys.argv[2]=='lexer2':
    for k in parser.dic_l.keys():
        print(L_RULE_TEMPLATE.format(name=k.strip(),
                                     regex=parser.dic_l[k]),
              end='')
DL_RULE_TEMPLATE='''
def t_MATH_{name}(t):
    r{regex}
    if not t.type in lexer.dic:
        lexer.dic[t.type] = [r{notation},{description},
                             r"\\ref{{FORC_{name}}}",t.lineno,t.lexpos]
        lexer.dollar_label_stack.append("FORC_{name}")
    return t
'''
if sys.argv[2]=='lexer2':
    for k in parser.dic_dl.keys():
        print(DL_RULE_TEMPLATE.format(name=k.strip(),
                                      regex = parser.dic_dl[k][0],
                                      notation = parser.dic_dl[k][1],
                                      description = parser.dic_dl[k][2]),
              end='')
    

