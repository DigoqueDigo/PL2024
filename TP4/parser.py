from sys import stdin
from ply.lex import lex
from ply.yacc import yacc

## TOKENIZER

reserved = {
   'SELECT' : 'SELECT',
   'FROM' : 'FROM',
   'WHERE' : 'WHERE'
}


tokens = [
    'NUMBER',
    'VARIABLE',
    'COMMA',
    'LESS',
    'GREATER',
    'EQUALS',
    'LESS_THAN_EQUALS',
    'GREATER_THAN_EQUALS'
] + list(reserved.values())


t_ignore = ' \t'
t_COMMA = r','
t_LESS = r'<'
t_GREATER = r'>'
t_EQUALS = r'='
t_LESS_THAN_EQUALS = r'<='
t_GREATER_THAN_EQUALS = r'>='


def t_NUMBER(t):
    r'[+\-]?\d+'
    t.value = int(t.value)
    return t


def t_VARIABLE(t):
    r'\w+'
    t.type = reserved.get(t.value.upper(),'VARIABLE')
    return t


def t_ignore_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f'Invalid character {t.value[0]}')
    t.lexer.skip(1)


## GRAMMAR RULES

def p_expression_reserved(p):
    '''expression : SELECT select_list FROM VARIABLE WHERE compare_condition'''
    p[0] = {'SELECT' : p[2], 'FROM' : p[4], 'WHERE' : p[6]}


def p_select_list(p):
    '''select_list : VARIABLE
        | select_list COMMA VARIABLE'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_compare_condition(p):
    '''compare_condition : VARIABLE LESS NUMBER
        | VARIABLE LESS_THAN_EQUALS NUMBER
        | VARIABLE GREATER NUMBER
        | VARIABLE GREATER_THAN_EQUALS NUMBER
        | VARIABLE EQUALS NUMBER'''
    p[0] = {'VARIABLE' : p[1], 'OPERATOR' : p[2], 'VALUE' : p[3]}


def p_error(p):
    print(f'Syntax error at {p.value}')


## MAIN FUNCTION

if __name__ == '__main__':
    lexer = lex()
    parser = yacc()
    print(parser.parse(stdin.read()))