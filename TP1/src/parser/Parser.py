class Parser:

    def __init__(self):
        self.headers = list()


    def setHeaders(self,line):
        self.headers = list(map(lambda x : x.strip(), line.split(',')))


    def parseLine(self,line,ignore = []):
        result = list(map(lambda x : x.strip(), line.split(',')))
        for element in ignore:
            result.pop(self.headers.index(element))
        return result