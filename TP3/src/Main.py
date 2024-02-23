from sys import stdin
from Automato import Automato


if __name__ == '__main__':

    automato = Automato()
    automato.setStates()
    automato.setTransactions()
    automato.setActions()

    for line in stdin:
        automato.execute(line)

    print(f'Soma final: {automato.getSum()}')