from sys import stdin
from ply.lex import lex


states = (
   ('DESLIGADO', 'inclusive'),
)


tokens = ['ON', 'OFF', 'NUMBER', 'EQUALS']

t_ignore = ' \t'
t_DESLIGADO_ignore = ' \t'
t_ON = r'(?i)on'


def t_NUMBER(t):
    r'[+\-]?\d+'
    t.lexer.soma += int(t.value)
    pass


def t_EQUALS(t):
    r'\='
    print(f'Soma = {t.lexer.soma}')
    pass


def t_OFF(t):
    r'(?i)off'
    t.lexer.begin('DESLIGADO')


def t_ignore_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)


def t_error(t):
    t.lexer.skip(1)


## RULES FOR STATE DESLIGADO

def t_DESLIGADO_ON(t):
    r'(?i)on'
    t.lexer.begin('INITIAL')


def t_DESLIGADO_NUMBER(t):
    r'[+\-]?\d+'
    pass


lexer = lex()
lexer.soma = 0
lexer.input(stdin.read())

for token in lexer:
    pass
