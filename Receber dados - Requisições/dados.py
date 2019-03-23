from flask import Flask, render_template, request


app=Flask(__name__)

@app.route("/")
def abrir_inicial():
    return render_template("cadastro.html")


@app.route("/adicionar_pessoa")
def adicionar_pessoa():
    nome=request.args.get("nome")
    endereco=request.args.get("endereco")
    lista =[nome, endereco]
    return render_template ("exibir.html", usuario = lista)


app.run()