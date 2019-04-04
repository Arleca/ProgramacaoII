from flask import Flask, render_template,request 
from pessoa import Pessoa 

app=Flask(__name__)


@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/listar")
def listar_pessoas():
    pessoas=[
        Pessoa("Ana","Rua 123","9250-5273"),
        Pessoa("Maria","Rua 456","9191-9191"),
        Pessoa("Amanda","Rua 789","7878-7878")]
    return render_template("listar_pessoas.html", lista=pessoas)

@app.route("/abrir_formulario")
def abrir_formulario():
    return render_template("form_inserir_pessoa.html")

@app.route("/inserir")
def inserir():
    nome=request.args.get("nome")
    endereço=request.args.get("endereço")
    telefone=request.args.get("telefone")
    mensagem="Os seguintes dados do formulário foram recebeidos"
    mensagem+= nome + " ," + endereço +" ," + telefone 
    return mensagem
    
    """
    novo_usuario=[name,adress,telephone]
    return render_template("listar_pessoas.html", novo_usuario=novo_usuario)  
    #Poderia voltar para exibir_mensagem também? ()
    
    """



app.run()



