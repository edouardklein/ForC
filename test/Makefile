TABLE_BUILDER_BUILDER=python3 ForC_parser.py
TEST_FILE=Annotated_short.org

test:
	${TABLE_BUILDER_BUILDER} ${TEST_FILE} lexer1 > tmp1.py #Building the table builder
	${TABLE_BUILDER_BUILDER} ${TEST_FILE} lexer2 > tmp2.py #Building the table builder
	cat ../src/Lex_header.py tmp1.py ../src/Lex_middler.py tmp2.py ../src/Lex_footer.py > ForC_tmp_lexer.py
	${TABLE_BUILDER_BUILDER} ${TEST_FILE} parser > tmp3.py #Building the table builder
	cat ../src/Parser_header.py tmp3.py ../src/Parser_footer.py > ForC_tmp_parser.py
	python3 ForC_tmp_parser.py ${TEST_FILE} > table.org #Building the table
	cat header.org ${TEST_FILE} table.org > Complete.org #Adding the symbol table at the end
	emacs -batch --visit $1 --funcall org-export-as-pdf-and-open --script ~/.emacs >/dev/null 2>/dev/null
