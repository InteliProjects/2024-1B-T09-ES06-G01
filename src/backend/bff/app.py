from flask import Flask
from backend.bff.controllers import ceo_blueprint, projeto_blueprint, recomendacao_blueprint, noticia_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(ceo_blueprint)
    app.register_blueprint(projeto_blueprint)
    app.register_blueprint(recomendacao_blueprint)
    app.register_blueprint(noticia_blueprint)
    return app
