# Error rule for syntax errors
def p_error(p):
    print("Error line "+str(p.lineno),file=sys.stderr)

# Build the parser
parser = yacc.yacc(debug=True)
parser.dic = {}
parser.dollar_label_stack = []
print(parser.parse(open(sys.argv[1]).read(),debug=0))

print("* Notation table")
print("| *Symbol* | *Meaning* | *Defined* |")
for key in lexer.dic.keys():
    print("| {} |{}|{}|".format(*(lexer.dic[key][:3])))
for key in parser.dic.keys():
    print("| {} |{}|{}|".format(*(parser.dic[key][:3])))

