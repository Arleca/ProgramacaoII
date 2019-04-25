from flask import Flask, render_template,request, redirect, url_for,session

app=Flask(__name__)

class Comida():
    def __init__(self,nome,categoria,vencimento):
        self.nome=nome
        self.categoria=categoria
        self.vencimento=vencimento

lista=[
    Comida("Pizza Doce","Doce","04/07"),
    Comida("Batata Frita","Salgado","12/10")]

app.config["SECRET_KEY"]="nsei"

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


@app.route("/form_editar_comida")
def abrir_form_editar():
    nome=request.args.get("nome")
    for c in lista:
        if c.nome==nome:
            return render_template("form_editar_comida.html", food=c)
    return "Comida não encontrada"


@app.route("/editar")
def editar():
    procurar=request.args.get("nome_original")
    nome=request.args.get("nome")
    categoria=request.args.get("categoria")
    vencimento=request.args.get("vencimento")
    nova_comida=Comida(nome,categoria,vencimento)
    for i in range(len(lista)):
        if lista[i].nome ==procurar:
            lista[i]=nova_comida
            return redirect(url_for("listar"))
    return "Comida não encontrada" + procurar

@app.route("/form_login")
def form_login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    login = request.form["login"]
    senha = request.form["senha"]
    if login == "adm" and senha=="123":
        session["usuario"] = login
        return redirect("/")
    else:
        return "não deu!"


@app.route("/logout")
def logout():
    session.pop("usuario")
    return redirect("/")


app.run(debug=True)
