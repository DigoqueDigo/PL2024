class Gestor:

    def __init__(self):
        self.comunidade = dict()


    def getPessoa(self,id):
        return self.comunidade[id]


    def addPessoa(self,pessoa):
        self.comunidade[pessoa.getId()] = pessoa


    def getAllModalidades(self):
        result = set()
        for pessoa in self.comunidade.values():
            result.add(pessoa.getModalidade())
        return sorted(result)


    def getAptDist(self):
        aptos = len(list(filter(lambda x : x.getResultado(), self.comunidade.values())))
        return aptos/len(self.comunidade), len(self.comunidade)-aptos/len(self.comunidade)