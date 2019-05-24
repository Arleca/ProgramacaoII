class Produto():
    def __init__(self, nome,preco):
        self.nome=nome
        self.preco=preco


class Item():
    def __init__(self,produto,qtd):
        self.produto=produto
        self.qtd=qtd

class Caixa():
    def __init__(self,data,hora,produto,qtd,nome,preco):
        self.produtos=Produto(nome,preco)
        self.item = Item(produto,qtd)
        self.data=data
        self.hora=hora
        self.itens=[]

    def calcular_preco(self,preco,qtd):
        preco_prod = preco*qtd
        self.itens.append(preco_prod)
        return preco_prod

    def calcular_total(self,itens):
        valor_total = sum(self.itens)
        return valor_total




if __name__=="__main__":
    pizza=Produto("pizza", 10.00)
    chocolate=Produto("chocolate", 3.00)
    batata=Produto("batata", 4.0)
    compra=Caixa("08/05","8:00",pizza,2,"pizza",10.00)
    

