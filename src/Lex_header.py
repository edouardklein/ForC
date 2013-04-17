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

