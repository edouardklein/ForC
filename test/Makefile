TABLE_BUILDER_BUILDER="ForC.py"


test:
	${TABLE_BUILDER_BUILDER} Annotated.org > tmp.py #Building the table builder
	python3 tmp.py Annotated.org > table.org #Building the table
	cat Annotated.org table.org > Complete.org #Adding the symbol table at the end
	emacs -batch --visit $1 --funcall org-export-as-pdf-and-open --script ~/.emacs >/dev/null 2>/dev/null
