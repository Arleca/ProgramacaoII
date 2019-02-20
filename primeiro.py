#Inicio meu primeiro programa no Github com um exemplo de herança
#Um dos pilares da Programação Orientada a Objeto 

class Animal(object):
    def __init__(self,idade,nome):
        self.idade=idade
        self.nome=nome


class Gato(Animal):
    def __init__(self,raça,cor_pelo,idade,nome):
        super().__init__(idade,nome)
        self.raça=raça
        self.cor_pelo=cor_pelo
        