TABLE_BUILDER_BUILDER=python3 ForC_parser.py
TEST_FILE=Annotated.org

test:
	${TABLE_BUILDER_BUILDER} ${TEST_FILE} lexer1 > tmp1.py #Building the table builder
	${TABLE_BUILDER_BUILDER} ${TEST_FILE} lexer2 > tmp2.py #Building the table builder
	cat ../src/Lex_header.py tmp1.py ../src/Lex_middler.py tmp2.py ../src/Lex_footer.py > ForC_tmp_lexer.py
	${TABLE_BUILDER_BUILDER} ${TEST_FILE} parser > tmp3.py #Building the table builder
	cat ../src/Parser_header.py tmp3.py ../src/Parser_footer.py > ForC_tmp_parser.py
	python3 ForC_tmp_parser.py ${TEST_FILE} > Processed.org #Building the table
	cat header.org Processed.org > Complete.org #Adding the symbol table at the end
