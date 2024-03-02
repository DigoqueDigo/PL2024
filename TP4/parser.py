from sys import stdin
from ply.lex import lex


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


def t_VARIABLE(t):
    r'\w+'
    t.type = reserved.get(t.value.upper(),'VARIABLE')
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_ignore_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f'Invalid character {t.value[0]}')
    t.lexer.skip(1)


if __name__ == '__main__':
    lexer = lex()
    for line in stdin:
        lexer.input(line)
        for token in lexer:
            print(token)