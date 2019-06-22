

class Produto():
    def __init__(self, nome,preco):
        self.nome=nome
        self.preco=preco


class Item():
    def __init__(self,produto,qtd):
        self.produto=produto
        self.qtd=qtd

class Caixa():
    def __init__(self,data,hora):
        self.data=data
        self.hora=hora
        self.itens=[]
        

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

if __name__=="__main__":
    pizza=Produto("pizza", 10.00)
    chocolate=Produto("chocolate", 8.00)
    c=Caixa("7/02","4:50")
    c.itens.append(Item(pizza,2))
    c.itens.append(Item(chocolate,5))
    print(c.calcular_preco())
    print(c.calcular_total())
    
