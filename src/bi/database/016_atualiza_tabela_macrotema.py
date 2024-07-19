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
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', encoding='utf-8')

# Conecta ao banco de dados
connection = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS, port=DB_PORT)
cursor = connection.cursor()

# Adicionar a nova coluna
cursor.execute("""
ALTER TABLE Macrotema ADD COLUMN nome_completo VARCHAR(255);
""")
connection.commit()

# Atualizar os valores da coluna nome_completo conforme os critérios
cursor.execute("""
UPDATE Macrotema
SET nome_completo = CASE
    WHEN nome = 'bem-estar' THEN 'Bem-Estar, Saúde e Felicidade'
    WHEN nome = 'produtividade' THEN 'Produtividade e Competitividade'
    WHEN nome = 'redução' THEN 'Redução do Impacto Ambiental'
    WHEN nome = 'diversidade' THEN 'Diversidade e Inclusão'
    WHEN nome = 'integridade' THEN 'Integridade e Práticas Éticas'
    WHEN nome = 'conservação' THEN 'Conservação do Planeta'
    ELSE nome_completo
END;
""")
connection.commit()

cursor.close()
connection.close()

logging.info('Migration para adicionar a coluna nome_completo na tabela Macrotema e atualizar seus valores concluída com sucesso!')
