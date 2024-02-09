from os import mkdir
from sys import stdin, exit
from datetime import datetime
from parser.Parser import Parser
from business.Gestor import Gestor
from business.Pessoa import Pessoa


if __name__ == '__main__':

    parser = Parser()
    gestor = Gestor()

    parser.setHeaders(stdin.readline())

    for linha in stdin:
        atributos = parser.parseLine(linha,['index'])
        gestor.addPessoa(Pessoa(
            atributos[0],
            datetime.strptime(atributos[1], '%Y-%m-%d'),
            atributos[2],
            atributos[3],
            int(atributos[4]),
            atributos[5],
            atributos[6],
            atributos[7],
            atributos[8],
            atributos[9],
            atributos[10] == 'true',
            atributos[11] == 'true'
        ))

    try:
        mkdir('resultados')

    except FileExistsError:
        pass

    except:
        exit(1)
    
    with open('resultados/modalidades','w') as fileModalidades:
        fileModalidades.write('\n'.join(gestor.getAllModalidades()))