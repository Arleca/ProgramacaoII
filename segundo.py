#Encapsulamento exemplificação


class Animal():

    def __init__(self, nome, idade, raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.__lista_vacinas_tomadas = []

    def fazer_barulho(self):
        pass

    def ficar_feliz(self):
        pass

    def tomar_injecao(self, nome_vacina):
        self.__lista_vacinas_tomadas.append(nome_vacina)
        return "Miauu"

    def imprimir_vacinas(self):
        for vacina in self.__lista_vacinas_tomadas:
            print(vacina)

    def __str__(self):
        return "Nome:" + self.nome + "Idade:" + self.idade
