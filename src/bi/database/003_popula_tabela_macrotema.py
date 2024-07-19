import os
import logging
import psycopg2
from dotenv import load_dotenv
import pandas as pd

# Carrega configurações do arquivo .env
load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = "coffee-break-database"

# Configuração do logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', encoding='utf-8')

# Obter o diretório atual onde este script está sendo executado
diretorio_atual = os.getcwd()

# Navegar para o diretório do arquivo de dados a partir do diretório atual
caminho_arquivo_raw = os.path.join(diretorio_atual, 'src', 'bi', 'data', 'raw', 'base-de-dados.xlsx')

# Cria o dataframe a partir do arquivo
df_projetos = pd.read_excel(caminho_arquivo_raw, sheet_name='ds-projetos', header=0)

connection = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS, port=DB_PORT)
cursor = connection.cursor()

# Pega os dados únicos da coluna macrosetor
macrotemas = df_projetos['macrosetor'].unique()

# Insere nome e descrição do macrotema na tabela
for macrotema in macrotemas:
    try:
        cursor.execute(f"INSERT INTO Macrotema (nome, descricao) VALUES ('{macrotema}', '{macrotema}')")
        logging.info(f"Macrotema {macrotema} inserido com sucesso!")
    except:
        logging.error(f"Macrotema {macrotema} já cadastrado.")

# Commita as alterações
connection.commit()
cursor.close()
connection.close()

logging.info('Dados dos Macrotemas inseridos!')
