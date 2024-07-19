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

# Funções para preencher valores nulos
def preencher_nulos():
    try:
        cursor.execute("""
            UPDATE Projeto
            SET 
                nome = COALESCE(nome, 'Nome Desconhecido'),
                descricao = COALESCE(descricao, 'Descrição não disponível'),
                estado = COALESCE(estado, 'Desconhecido')
            WHERE
                nome IS NULL OR
                descricao IS NULL OR
                estado IS NULL
        """)
        logging.info("Valores nulos preenchidos com sucesso!")
    except Exception as e:
        logging.error(f"Erro ao preencher valores nulos: {e}")

# Executa a função de preenchimento de nulos
preencher_nulos()

# Commita as alterações e fecha a conexão
connection.commit()
cursor.close()
connection.close()

logging.info('Migration para preencher valores nulos dos projetos concluída com sucesso!')
