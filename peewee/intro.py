lista_produtos = []

class Cliente():
    def __init__(self,nome,email,senha,telefone):
        self.nome= nome 
        self.email= email
        self.senha= senha
        self.telefone = telefone
        

class Animal():
    def __init__(self, nome, especie, dat_nasc, dono):
        self.nome = nome
        self.especie = especie
        self.dat_nasc = dat_nasc
        self.dono = dono

class Consulta():
    def __init__(self, horario, tipo_consulta):
        #super().__init__(self.nome, self.email, self.senha, self.telefone)
        #Animal.__init__(nome, especie, dat_nasc)
        self.horario = horario
        self.tipo_consulta = tipo_consulta

        

class Produto():
    def __init__(self,  cod_produto, nome_produto, preco):
        self.cod_produto = cod_produto
        self.nome_produto = nome_produto
        self.preco = preco


if __name__ == "__main__":
    cli = Cliente("Josefauldo","jojo7@gmail.com", "vorange", "33-4854452")
    ani = Animal("leuli", "gato", "20/05/2019", "Josefauldo")
    pro = Produto("12123", "ursinho Pooh", "300,00")
    consulta = Consulta("08:07", "pos-parto da mãe do leuli")

    print(cli.nome)
    print(ani.nome)
    print(pro.nome_produto)
    print(consulta.horario)