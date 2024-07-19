from flask import Flask
from backend.projetos.controllers import projeto_blueprint # Importa o blueprint para o módulo de projetos
from backend.common.database import Database # Importa o módulo para manipulação do banco de dados
import os # Importa o módulo para interação com o sistema operacional
from dotenv import load_dotenv # Importa a função para carregar variáveis de ambiente
from flasgger import Swagger  # Importa o Swagger


load_dotenv() # Carrega as variáveis de ambiente do arquivo .env

DATABASE_URL = os.getenv('DB_URL') 

def create_app():
    # Inicialização do banco de dados
    Database.initialize(DATABASE_URL)
    
    app = Flask(__name__)  # Cria uma nova instância do aplicativo Flask
    app.register_blueprint(projeto_blueprint, url_prefix='/api') # Registra o blueprint dos projetos no app com prefixo de URL '/api'
    
    Swagger(app)  # Inicializa o Swagger
    
    return app # Retorna a instância do aplicativo configurada
