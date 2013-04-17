import ply.lex as lex

states = (
    ('ORG','exclusive'),
    ('MATH','exclusive'),
    )

tokens = (
    'BACKSLASH',
    'ACTUAL_DOLLAR',
    'TEXT',
    'newline',
    'COMMENT',
    'DOLLAR',
    'PAREN',
    'BRACE',
    'COMMA',
    'BLANK',
    'EQUAL',
    'SUBSCRIPT',
    'EXPONENT',
    'DASH',
    'KNOWING',
    'LATEX_IGNORE',
    'LEQ',
    'NUMBER',
    'IN',

