from flask import Flask
from controllers.personagens_controller import bp as personagens_bp


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'change-me'

    app.register_blueprint(personagens_bp)

    @app.route('/health')
    def health():
        return 'ok'

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
