# controlador recebe requisições e decide o que deve ser feito
import os
import json
from flask import render_template, request
from models.personagem import Personagem   
from models.dados import rola_dados

DATA_FILE = os.path.join("data" "personagens.json")

def criar_personagem():
    if request.method == "POST":
        nome = request.form["nome"]
        raca = request.form["raca"]
        classe = request.form["classe"]
        atributos = request.form["atributos"]
        
        personagem = Personagem(nome, raca, classe, atributos)
        
        # 1 - garante que a pasta existe
        os.makedirs("data", exist_ok=True)
        
        personagens = []
        if os.path.exists(DATA_FILE): # 2 - carrega o json
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                personagens = json.load(f)
                
        personagens.append(personagem.__dict__) # adciona o personagem
        
        with open(DATA_FILE, "w", encoding="utf-8") as f: # salva json
            json.dump(personagens, f, indent=4, ensure_ascii=False)
            
        return render_template("criar_personagem.html", personagem=personagem)
    
    return render_template("criar_personagem.html")
                
            