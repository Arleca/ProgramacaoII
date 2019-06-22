class Projeto_Integrador():
    def __init__(self,titulo,ano,aluno,professor):
        self.titulo=titulo
        self.ano=ano
        self.aluno=aluno
        self.professor=professor 


class Aluno():
    def __init__(self,nome,turma):
        self.nome=nome
        self.turma=turma 

class Professor():
    def __init__(self,nome,tipo_atuacao, tipo_envio):
        self.nome = nome
        self.tipo_atuacao = tipo_atuacao
        self.tipo_envio = tipo_envio

class Periodico():
    def __init__(self, editora, INNS, local_apresentacao):
        self.editora = editora
        self.INNS = INNS
        self.local_apresentacao = local_apresentacao


class Evento():
    def __init__(self,nome,local,data)


