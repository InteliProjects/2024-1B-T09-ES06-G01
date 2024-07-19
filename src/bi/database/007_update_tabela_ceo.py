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

# Comando para atualizar o estado de todos os Ceo para 'ativo'
try:
    cursor.execute("UPDATE Ceo SET estado = 'ativo'")
    connection.commit()
    print("Todos os CEOs foram atualizados para o estado 'ativo'.")
except psycopg2.Error as e:
    print(f"Erro ao atualizar o estado dos CEOs: {e}")
    connection.rollback()  # Desfaz a alteração em caso de erro
finally:
    cursor.close()
    connection.close()
