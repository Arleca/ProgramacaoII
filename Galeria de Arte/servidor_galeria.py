from flask import Flask, json, jsonify
from flask import request
from playhouse.shortcuts import model_to_dict
from peewee import * 
from galeria import *

app = Flask(__name__)



@app.route('/')
def index():
    return "Backend; <a href=/listar_exposicoes>Clique aqui para ver a lista de exposições!</a> <br> <a href=/listar_galerias>Clique aqui para ver a lista de galerias!</a>"


@app.route('/listar_exposicoes')
def listar_exposicoes():
    autores= list(map(model_to_dict, Exposicao.select()))
    response = jsonify({"lista": autores})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/listar_galerias')
def listar_galerias():
    exposicoes= list(map(model_to_dict, Galeria.select()))
    response = jsonify({"lista": exposicoes})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response




app.run(debug=True, port=4999)