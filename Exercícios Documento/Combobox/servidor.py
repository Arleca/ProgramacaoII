from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template('combobox.html')

@app.route("/mostrar_selecao")
def mostrar_selecao():
    lista = request.args.getlist('estado')
    s = "Estados selecionados: "
    for estado in lista:
        s += estado + " "
    s+= "<br><a href=/>Retornar</a>"    
    return s     

app.run()