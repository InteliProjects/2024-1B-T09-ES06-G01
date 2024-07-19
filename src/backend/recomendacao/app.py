from flask import Flask
from backend.recomendacao.controllers import recomendacao_blueprint
from backend.common.database import Database
import os
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

DATABASE_URL = os.getenv('DB_URL')

def create_app():
    # Inicialização do banco de dados
    Database.initialize(DATABASE_URL)
    
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(recomendacao_blueprint, url_prefix='/api')
    
    return app