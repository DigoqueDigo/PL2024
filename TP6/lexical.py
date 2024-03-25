from ply.lex import lex


tokens = [
    'PRINT',
    'READ',
    'ASSIGN',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'NUMBER',
    'VARIABLE',
]


t_PRINT = r'\!'
t_READ = r'\?'
t_ASSIGN = r'\='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_VARIABLE = r'[a-zA-Z_]'
t_ignore = ' \t'


def t_NUMBER(t):
    r'[+\-]?\d+(\.\d+)?'
    t.value = float(t.value)
    return t


def t_ignore_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f'Invalid character {t.value[0]}')
    t.lexer.skip(1)


def parse(text):
    result = []
    lexer = lex()
    lexer.input(text)
    while token := lexer.token():
        result.append(token)
    return result


if __name__ == '__main__':

    with open('input.txt','r') as inputFile:
        print(parse(inputFile.read()))