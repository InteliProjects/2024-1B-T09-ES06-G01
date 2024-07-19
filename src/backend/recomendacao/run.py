from .app import create_app # Importa a função create_app do módulo app dentro do mesmo pacote
import os # Importa o módulo os para interação com o sistema operacional
from dotenv import load_dotenv # Importa a função load_dotenv do pacote dotenv
from flask_cors import CORS
from backend.common.traceability import Trace

load_dotenv() # Carrega as variáveis de ambiente do arquivo .env para o ambiente atual

app = create_app() # Cria uma instância do aplicativo Flask usando a função importada

# Bloco condicional que verifica se o script está sendo executado como script principal
if __name__ == '__main__':
    print(Trace.matrix())
    # Executa o aplicativo Flask com configurações de debug e porta específicas
    app.run(debug=True, port=os.getenv('RECOMENDACAO_PORTA'))