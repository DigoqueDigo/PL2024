from lexical import parse


class Syn:


    def __init__(self,tokens):
        self.tokens = tokens
        self.currentIndex = -1
        self.variables = dict()
        self.currentToken = None


    def advance(self):
        self.currentIndex += 1
        if self.currentIndex < len(self.tokens):
            self.currentToken = self.tokens[self.currentIndex]
        else:
            self.currentToken.type = 'END'


    def parse(self):

        self.advance()

        while self.currentToken.type in ['PRINT','READ','VARIABLE']:

            option = self.currentToken.type
            variable = self.currentToken.value
            self.advance()

            if option == 'PRINT':
                self.parsePrint()

            elif option == 'READ':
                self.parseRead()

            else:
                self.parseAssign(variable)


    def parseRead(self):
        value = float(input(f'Valor de {self.currentToken.value}: '))
        self.variables[self.currentToken.value] = value
        self.advance()


    def parsePrint(self):
        print(self.parseExpression())


    def parseAssign(self,variable):

        if self.currentToken.type != 'ASSIGN':
            raise Exception('Syntax error in assign')

        self.advance()
        self.variables[variable] = self.parseExpression()


    def parseExpression(self):

        result = self.parseTerm()

        while self.currentToken.type in ['PLUS','MINUS']:

            operation = self.currentToken.type
            self.advance()

            if operation == 'PLUS':
                result += self.parseTerm()
            else:
                result -= self.parseTerm()

        return result


    def parseTerm(self):
        result = self.parseFactor()

        while self.currentToken.type in ['TIMES','DIVIDE']:

            operation = self.currentToken.type
            self.advance()

            if operation == 'TIMES':
                result *= self.parseFactor()
            else:
                result /= self.parseFactor()

        return result


    def parseFactor(self):

        if self.currentToken.type == 'NUMBER':
            number = self.currentToken.value
            self.advance()
            return number

        elif self.currentToken.type == 'VARIABLE':
            number = self.variables[self.currentToken.value]
            self.advance()
            return number

        elif self.currentToken.type == 'LPAREN':
            self.advance()
            content = self.parseExpression()
            if self.currentToken.type != 'RPAREN':
                raise Exception('Expected closing parenthesis')
            self.advance()
            return content

        else:
            raise Exception("Syntax error in expression")


if __name__ == '__main__':

    with open('input.txt','r') as inputFile:
        tokens = parse(inputFile.read())
        Syn(tokens).parse()