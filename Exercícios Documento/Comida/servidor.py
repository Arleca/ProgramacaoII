from flask import Flask, render_template,request

app=Flask(__name__)

class Comida():
    def __init__(self,nome,categoria,vencimento):
        self.nome=nome
        self.categoria=categoria
        self.vencimento=vencimento

lista=[
    Comida("Pizza Doce","Doce","04/07"),
    Comida("Batata Frita","Salgado","12/10")]

@app.route("/")
def index():
    return render_template("inicio.html")


@app.route("/listar")
def listar():
    return render_template("listar_food.html", lista_food=lista)



@app.route("/abrir_form_incluir")
def abrir_form_incluir():
    return render_template("incluir_comida.html")

@app.route("/incluir")
def incluir():
    nome=request.args.get("nome")
    categoria=request.args.get("categoria")
    vencimento=request.args.get("vencimento")
    lista.append(Comida(nome,categoria,vencimento))
    return listar()
    #mensagem="A comida incluida foi:"
    #mensagem+= nome + "," + categoria + "," + vencimento
    #return mensagem


@app.route("/excluir")
def excluir():
    excluir=None
    nome=request.args.get("nome")
    for comida in lista:
        if nome==comida.nome:
            excluir=comida
            break
    if excluir!=None:
        lista.remove(excluir)
    return listar()



app.run(debug=True)
