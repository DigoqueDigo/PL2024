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


    def getDistAptos(self):
        aptos = len(list(filter(lambda x : x.getResultado(), self.comunidade.values())))
        return aptos/len(self.comunidade)


    def getDistInaptos(self):
        inaptos = len(list(filter(lambda x : not x.getResultado(), self.comunidade.values())))
        return inaptos/len(self.comunidade)


    def getDistEscalao(self, gap):
        escaloes = [(range(gap*x,gap*(x+1)),0) for x in range(int(100/gap))]
        for pessoa in self.comunidade.values():
            interval, value = escaloes[int(pessoa.getIdade()/gap)]
            escaloes[int(pessoa.getIdade()/gap)] = interval, value+1
        return list(map(lambda x: (x[0],x[1]/len(self.comunidade)), escaloes))