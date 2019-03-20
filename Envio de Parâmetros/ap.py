from flask import Flask, render_template
from pessoa import Pessoa

app = Flask(__name__)

@app.route("/")
def listar():
    lista=[Pessoa("Ana", "rua 08", "54654185418"),
        Pessoa("Amanda", "rua 09", "54654185555"),
        Pessoa("Maria", "rua 78", "5465418999999")]
    return render_template("listar.html", usuarios=lista)

app.run() 