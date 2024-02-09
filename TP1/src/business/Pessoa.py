class Pessoa:

    def __init__(self,id,dataEMD,nome,apelido,idade,genero,morada,modalidade,clube,email,federado,resultado):
        self.id = id
        self.dataEMD = dataEMD
        self.nome = nome
        self.apelido = apelido
        self.idade = idade
        self.genero = genero
        self.morada = morada
        self.modalidade = modalidade
        self.clube = clube
        self.email = email
        self.federado = federado
        self.resultado = resultado


    def __str__(self):
        return  f'ID: {self.id}'                    \
                f'\tData: {self.dataEMD}'             \
                f'\tNome: {self.nome}'              \
                f'\tApelido: {self.apelido}'        \
                f'\tIdade: {self.idade}'            \
                f'\tGenero: {self.genero}'          \
                f'\tMorada: {self.morada}'          \
                f'\tModalidade: {self.modalidade}'  \
                f'\tClube: {self.clube}'            \
                f'\tEmail: {self.email}'            \
                f'\tFederado: {self.federado}'      \
                f'\tResultado: {self.resultado}'
    

    def getId(self):
        return self.id


    def getIdade(self):
        return self.idade


    def getModalidade(self):
        return self.modalidade


    def getResultado(self):
        return self.resultado