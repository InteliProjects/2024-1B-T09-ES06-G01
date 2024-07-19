import os
import psycopg2
from dotenv import load_dotenv

# Carrega as configurações do arquivo .env
load_dotenv()

# Define as variáveis de ambiente
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = 'coffee-break-database'

# Conecta ao banco de dados
connection = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS, port=DB_PORT)
cursor = connection.cursor()

# Comando para criar a tabela Recomendacao
create_table_query = """
CREATE TABLE Recomendacao (
    id SERIAL PRIMARY KEY,
    tipo VARCHAR(255) NOT NULL,
    data TIMESTAMP NOT NULL,
    pontuacao INTEGER NOT NULL,
    ceo_id INT,
    projeto_id INT,
    FOREIGN KEY (ceo_id) REFERENCES Ceo(id),
    FOREIGN KEY (projeto_id) REFERENCES Projeto(id)
);
"""

try:
    cursor.execute(create_table_query)
    connection.commit()
    print("Tabela 'Recomendacao' criada com sucesso.")
except psycopg2.Error as e:
    print(f"Erro ao criar a tabela 'Recomendacao': {e}")
    connection.rollback()  # Desfaz a alteração em caso de erro
finally:
    cursor.close()
    connection.close()
