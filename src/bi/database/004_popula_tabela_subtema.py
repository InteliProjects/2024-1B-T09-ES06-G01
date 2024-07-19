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

# Processamento para inserção de Subtemas
subtemas = df_projetos['setor'].unique()
for subtema in subtemas:
    # Consulta o Macrotema relacionado no DataFrame
    macrotema_relacionado = df_projetos[df_projetos['setor'] == subtema]['macrosetor'].iloc[0]

    # Busca o ID do Macrotema correspondente no banco de dados
    cursor.execute("SELECT id FROM Macrotema WHERE nome = %s", (macrotema_relacionado,))
    macrotema_id = cursor.fetchone()
    
    if macrotema_id:
        try:
            # Insere o Subtema com o ID do Macrotema correspondente
            cursor.execute("INSERT INTO Subtema (nome, descricao, macrotema_id) VALUES (%s, %s, %s)", (subtema, subtema, macrotema_id[0]))
            connection.commit()
            logging.info(f"Subtema {subtema} inserido com sucesso sob o Macrotema {macrotema_relacionado}!")
        except psycopg2.Error as e:
            logging.error(f"Erro ao inserir o Subtema {subtema}: {e}")
    else:
        logging.error(f"Macrotema {macrotema_relacionado} não encontrado para o Subtema {subtema}")

cursor.close()
connection.close()

logging.info('Dados dos Subtemas inseridos!')
