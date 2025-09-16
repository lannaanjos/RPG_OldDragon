from flask import Flask, render_template
import json
import os


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/criar_personagem")
def criar_personagem():
    return render_template("criar_personagem.html")

DATA_FILE = os.path.join("data", "personagens.json")

@app.route("/personagens_criados")
def listar_personagens():
    personagens = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", enconding="utf-8") as f:
            personagens = json.load(f)
            
    return render_template("personagens_criados.html", personagens=personagens)
        


if __name__ == "__main__":
    app.run(debug=True)