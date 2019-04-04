from flask import Flask, render_template

app=Flask(__name__)

class Livro(): 
    def __init__(self,titulo,autor,ano,editora):
        self.titulo=titulo
        self.autor=autor
        self.ano=ano
        self.editora=editora

livros=[Livro("Só os Animais Salvam","AA","2018","DarkSide"),
        Livro("O senhor dos Aneis - A sociedade do Anel","Tolkien","2000","bl")]

@app.route("/")
def listar_livros():
    return render_template("listar.html", listagem=livros)



app.run()