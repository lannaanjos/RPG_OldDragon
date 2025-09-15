from flask import Flask
from controllers.controlador_personagem import blueprint_personagem 

app = Flask(__name__)
app.register_blueprint(blueprint_personagem) # importando e registrando blueprint do personagem


if __name__ == "__main__":
    app.run(debug=True)