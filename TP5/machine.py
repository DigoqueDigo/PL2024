import re as regex
from ply.lex import lex
from sys import stdin, exit


tokens = ['LISTAR', 'MOEDA', 'SELECIONAR', 'SAIR', 'CONSULTAR']

t_ignore = ' \t'


def t_LISTAR(t):
    r'(?i)listar'
    for product in t.lexer.products:
        print(f'{product} :: {t.lexer.products[product]}')


def t_MOEDA(t):
    r'(?i)moeda .*'
    for moeda in regex.findall(r'(\d+(\.\d+)?)',t.value):
        t.lexer.saldo += float(moeda[0])


def t_SELECIONAR(t):
    r'(?i)selecionar\s\d+'
    product = int(regex.search(r'\d+',t.value).group(0))

    if product in t.lexer.products:
        price = t.lexer.products[product][1]

        if price > t.lexer.saldo:
            print("Saldo Insuficiente")

        else:
           t.lexer.saldo -= price

    else:
        print('Produto inválido')


def t_CONSULTAR(t):
    r'(?i)consultar'
    print(f'Saldo :: {t.lexer.saldo}')


def t_SAIR(t):
    r'(?i)sair'
    print('Volte Sempre')
    exit(0)


def t_ignore_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)


def t_error(t):
    t.lexer.skip(1)


lexer = lex()

lexer.saldo = 0
lexer.products = {
    1 : ('Agua', 1.2),
    2 : ('Bolo', 1.3),
    3 : ('Sumo', 2.4),
    4 : ('Pastel', 0.9)
}

lexer.input(stdin.read())

for token in lexer:
    pass