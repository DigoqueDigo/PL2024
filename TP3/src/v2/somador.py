import re as regex
from sys import stdin


tokens = [
    ('INT', r'[+\-]?\d+'),
    ('EQUAL', r'='),
    ('ON', r'on'),
    ('OFF', r'off'),
    ('OTHERWISE', r'.')
]

expression = '|'.join(f'(?P<{nome}>{content})' for nome, content in tokens)


if __name__ == '__main__':

    soma = 0
    flag = True

    for line in stdin:

        for element in regex.finditer(expression,line,regex.IGNORECASE):

            element = element.groupdict()

            if element['INT'] and flag:
                soma += int(element['INT'])

            elif element['EQUAL']:
                print(f'Soma: {soma}')

            elif element['ON']:
                flag = True

            elif element['OFF']:
                flag = False