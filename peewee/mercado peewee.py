import peewee,os



db = peewee.SqliteDatabase("mercado.db")

class Produto(peewee.Model):
    nome=peewee.CharField()
    preco=peewee.IntegerField()
    class Meta:
        database=db

    def __str__(self):
        return self.nome + " " +str(self.preco)

class Item(peewee.Model):
    produto=peewee.ForeignKeyField(Produto)
    qtd=peewee.IntegerField()
    class Meta:
        database=db
    def __str__(self):
        return self.produto + str(self.qtd)

class Caixa(peewee.Model):
    data=peewee.CharField()
    hora=peewee.CharField()
    itens=[]
    class Meta:
        database=db  
    def __str__(self):
        return self.data + str(self.hora)  

    def calcular_preco(self):
        lista_item_total=[]
        for item in self.itens:
            preco=item.produto.preco
            qtd=item.qtd
            preco_total=preco*qtd
            lista_item_total.append(preco_total)
        return lista_item_total

    def calcular_total(self):
        valor_total = sum(self.calcular_preco())
        return valor_total


db.create_tables([Produto,Item,Caixa])

if __name__=="__main__":
    pizza=Produto(nome="pizza",preco=10.00)
    item1=Item(produto=pizza,qtd=2)
    c=Caixa(data="7/02",hora="4:50")
    pizza.save() 
    item1.save()
    c.save() 
    tudo1=pizza.select()
    tudo2=item1.select()
    tudo3=c.select 

    for i in tudo1:
        print(i)
    #print(c.calcular_preco())
    #print(c.calcular_total())
    
