from peewee import * 
import datetime
# Galeria de Arte 
arquivo="bancodedados.db"
db=SqliteDatabase(arquivo)

class BaseModelo(Model): 
    class Meta: 
        database=db


class Obra(BaseModelo): 
    nome_obra = CharField() 
    movm_artistico = CharField() 
    preco_obra = FloatField() 

class Autor(BaseModelo): 
    nome_autor = CharField() 
    obra=CharField()
    

class Exposicao(BaseModelo): 
    nome_expos = CharField() 
    data_expos = DateTimeField() 
    autores = ManyToManyField(Autor)
    

class Galeria(BaseModelo): 
    nome_galeria = CharField() 
    localizacao = CharField()
    exposicoes=ManyToManyField(Exposicao)
    
class Visitante(BaseModelo): 
    nome_visitante = CharField() 
    obra_comprada = ForeignKeyField(Obra)

class Ingresso(BaseModelo): 
    preco_ingresso = FloatField() 
    tipo_ingresso = CharField() 

class IngressoDaGaleria(BaseModelo): 
    galeria = ForeignKeyField(Galeria) 
    ingresso = ForeignKeyField(Ingresso) 
    quantidade = IntegerField()

class Funcionario(BaseModelo): 
    nome_funcionario = CharField() 
    
class Venda(BaseModelo): 
    obra_vendida= CharField()

class VendaDoFuncionario(BaseModelo): 
    funcionario = ForeignKeyField(Funcionario) 
    venda = ForeignKeyField(Venda) 
    data = DateTimeField() 

db.connect()

db.create_tables([Galeria, Galeria.exposicoes.get_through_model(),Obra, Autor, Exposicao,Exposicao.autores.get_through_model(), Visitante, Ingresso, IngressoDaGaleria, Funcionario, Venda, VendaDoFuncionario])

galeria1 = Galeria.create(nome_galeria="Galeria Belas Artes", localizacao = "Sao Paulo")

galeria2 = Galeria.create(nome_galeria="Galeria Moderna", localizacao="Santa Catarina")

obra1 = Obra.create(nome_obra="Noite Estrelada", movm_artistico="Pos-Impressionismo", preco_obra=4789.544)

autor1=Autor.create(nome_autor="Van Gogh", obra="Noite Estrelada")

exposicao1 = Exposicao.create(nome_expos="Exposicao de Inverno", data_expos='12/14/2019')

exposicao2 = Exposicao.create(nome_expos="Exposicao de Verao", data_expos='11/25/2019')

visitante1 = Visitante.create(nome_visitante="Ana", obra_comprada=obra1)

ingresso1 = Ingresso.create(preco_ingresso=19.90, tipo_ingresso="Comercial") 

ingresso_da_galeria = IngressoDaGaleria.create(galeria = galeria1, ingresso = ingresso1, quantidade = 25 )

funcionario1 = Funcionario.create(nome_funcionario="Roberto")

venda1 = Venda.create(obra_vendida="Noite Estrelada")

vendadofuncionario = VendaDoFuncionario.create(funcionario= funcionario1, venda = venda1, data="11/25/2019")


exposicao1.galerias.add(galeria1)
exposicao2.galerias.add(galeria2)
exposicao1.autores.add(autor1)


for galeria in exposicao1.galerias:
    print("Nome da Galeria: ",galeria.nome_galeria, "Endereco: ",galeria.localizacao)

for galeria in exposicao2.galerias:
    print("Nome da Galeria: ",galeria.nome_galeria, "Endereco: ",galeria.localizacao)

for autor in exposicao1.autores:
    print("Nome do Autor: ", autor.nome_autor)