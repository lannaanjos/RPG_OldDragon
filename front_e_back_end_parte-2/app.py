from flask import Flask
from controllers.personagens_controller import bp as personagens_bp # bp organiza as rotas em módulos e depois é chamado dentro do app.py


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mudar_dps' # protege sessões e formulários

    app.register_blueprint(personagens_bp) # conecta com o blueprint

    @app.route('/health') # verifica se o server tá de pé
    def health():
        return 'ok'

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
