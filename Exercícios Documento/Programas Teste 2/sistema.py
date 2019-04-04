from flask import Flask, render_template,request 
#from pessoa import Pessoa 

app=Flask(__name__)


class Pessoa():
    def __init__(self,nome="",endereço="",telefone=""):
        self.nome=nome
        self.endereço=endereço
        self.telefone=telefone


pessoas=[]



@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/listar")
def listar_pessoas():
    return render_template("listar_pessoas.html", lista=pessoas)

@app.route("/abrir_formulario")
def abrir_formulario():
    return render_template("form_inserir_pessoa.html")    #Esse form alterar pessoa não poderia ser um link? 
                                                          #Não, pois as rotas servem justamente para dinamizar um sist. 
                                                          

@app.route("/inserir")
def inserir():
    nome=request.args.get("nome")
    endereço=request.args.get("endereço")
    telefone=request.args.get("telefone")
    novo_usuario=Pessoa(nome,endereço,telefone)
    pessoas.append(novo_usuario)
    return render_template("mensagem.html", mensagem="Pessoa Inserida com sucesso!")
    
"""
novo_usuario=[nome,endereço,telefone]
return render_template("listar_pessoas.html", novo_usuario=novo_usuario)  
#Poderia voltar para exibir_mensagem também? ()
"""

@app.route("/excluir_pessoa")
def excluir_pessoa():
    excluir=None
    nome=request.args.get("nome")
    for p in pessoas:
        if nome==p.nome:
            excluir=p
            break
    if excluir!=None:
        pessoas.remove(excluir)
    return render_template("mensagem2.html", usuarios=pessoas)
app.run(debug=True)



#As rotas estão acompanhadas com um html porque uma rota não vai redirecionar para outra rota, mas sim para uma 
#página html, atraves do render template. E uma rota que esteja sozinha vai então redirecionar para uma outra rota
#que tenha uma página html. 