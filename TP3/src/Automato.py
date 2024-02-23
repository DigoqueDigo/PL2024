class Automato:

    def __init__(self):
        self.sum = 0
        self.switch = 0
        self.actions = dict()
        self.transactions = dict()
        self.states = list()
        self.currentState = 'T'


    def setStates(self):
        self.states = ['T', 'N', 'ON', 'ON_COMPLETE', 'OFF', 'OFF_COMPLETE', '=']


    def setTransactions(self):

        self.transactions['T'] = {
            '0': 'N', '1': 'N', '2': 'N', '3': 'N', '4': 'N', '5': 'N', '6': 'N', '7': 'N', '8': 'N', '9': 'N', '-': 'N',
            'o': 'ON', 'O': 'ON',
            '=': '='
        }

        self.transactions['ON'] = {
            '0': 'N', '1': 'N', '2': 'N', '3': 'N', '4': 'N', '5': 'N', '6': 'N', '7': 'N', '8': 'N', '9': 'N', '-': 'N',
            'o': 'ON', 'O': 'ON',
            'f': 'OFF', 'F': 'OFF',
            'n': 'ON_COMPLETE', 'N' : 'ON_COMPLETE',
            '=': '='
        }

        self.transactions['OFF'] = {
            '0': 'N', '1': 'N', '2': 'N', '3': 'N', '4': 'N', '5': 'N', '6': 'N', '7': 'N', '8': 'N', '9': 'N', '-': 'N',
            'o': 'ON', 'O': 'ON',
            'f': 'OFF_COMPLETE', 'F' : 'OFF_COMPLETE',
            '=': '='
        }

        self.transactions['N'] = self.transactions['T']
        self.transactions['='] = self.transactions['T']
        self.transactions['ON_COMPLETE'] = self.transactions['T']
        self.transactions['OFF_COMPLETE'] = self.transactions['T']


    def turnOn(self):
        self.switch = True


    def turnOff(self):
        self.switch = False


    def add(self,value):
        if self.switch:
            self.sum += value


    def getSum(self):
        return self.sum


    def setActions(self):
        self.actions['T'] = lambda : None
        self.actions['N'] = lambda : None
        self.actions['ON'] = lambda : None
        self.actions['OFF'] = lambda : None
        self.actions['ON_COMPLETE'] = lambda : self.turnOn()
        self.actions['OFF_COMPLETE'] = lambda : self.turnOff()
        self.actions['='] = lambda : print(f'Soma: {self.sum}')


    def execute(self,line):

        accWord = ''

        for character in line:

            self.currentState = self.transactions[self.currentState].get(character,'T')

            if self.currentState == 'N':
                accWord += character
                if character == '-':
                    self.add(int(accWord.rstrip('-') or 0))
                    accWord = character

            else:
                self.add(int(accWord.rstrip('-') or 0))
                accWord = ''

            self.actions[self.currentState]()