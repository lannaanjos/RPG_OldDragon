# controlador recebe requisições e decide o que deve ser feito

from flask import Blueprint, render_template, request
from models.personagem import Personagem   
from models.dados import rola_dados

blueprint_personagem = Blueprint("personagem", __name__)

@blueprint_personagem.route("/")
def index():
    return render_template("index.html")

# cria o personagem e mostra na tela
@blueprint_personagem.route("/criar_personagem", methods=["GET", "POST"])
def criacao_personagem():
    if request.method == "POST":
        nome = request.form['Nome']
        opcao = request.form['Opcao']
        raca = request.form["Raca"]
        classe = request.form["Classe"]
        
        atributos = rola_dados(opcao)
        
        personagem = Personagem(nome, atributos, raca, classe)
        
        return render_template("criar_personagem.html", personagem=personagem)
    
    return render_template("criar_personagem.html", personagem=None)