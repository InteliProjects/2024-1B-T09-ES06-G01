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

# Comando para adicionar uma nova coluna 'avaliacao' com restrições de valor
try:
    cursor.execute("""
    ALTER TABLE Interacao 
    ADD COLUMN avaliacao INTEGER CHECK (avaliacao >= 1 AND avaliacao <= 5)
    """)
    connection.commit()
    print("Coluna 'avaliacao' adicionada com sucesso à tabela 'Interacao'.")
except psycopg2.Error as e:
    print(f"Erro ao adicionar coluna 'avaliacao': {e}")
    connection.rollback()  # Desfaz a alteração em caso de erro
finally:
    cursor.close()
    connection.close()
