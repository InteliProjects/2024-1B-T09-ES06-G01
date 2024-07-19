from flask import Flask
from backend.ceos.controllers import ceo_blueprint
from backend.common.database import Database
import os
from dotenv import load_dotenv
from flasgger import Swagger  # Importa o Swagger


load_dotenv()
DATABASE_URL = os.getenv('DB_URL')

def create_app():
    # Inicialização do banco de dados
    Database.initialize(DATABASE_URL)
    
    app = Flask(__name__)
    app.register_blueprint(ceo_blueprint, url_prefix='/api')
    
    Swagger(app)  # Inicializa o Swagger
    
    return app
