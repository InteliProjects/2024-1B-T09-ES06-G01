import os
import logging
import psycopg2
from dotenv import load_dotenv

# Carrega configurações do arquivo .env
load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = 'coffee-break-database'

# Configuração do logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', encoding='utf-8')

# Conecta ao banco de dados
connection = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS, port=DB_PORT)
cursor = connection.cursor()

# Remover a coluna ceo_id da tabela Atualizacao
cursor.execute("""
ALTER TABLE Atualizacao
DROP COLUMN ceo_id;
""")
connection.commit()

cursor.close()
connection.close()

logging.info('Migration para remover a coluna ceo_id na tabela Atualizacao concluída com sucesso!')
