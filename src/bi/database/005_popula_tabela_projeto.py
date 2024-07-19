import os
import logging
import psycopg2
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime

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

# Processamento para inserção de Projetos
for _, row in df_projetos.iterrows():
    setor = row['setor']
    proponente_id = row['proponente_id']
    projeto = row['projeto']

    # Busca o Subtema ID correspondente
    cursor.execute("SELECT id FROM Subtema WHERE nome = %s", (setor,))
    subtema_id = cursor.fetchone()

    # Verifica se o CEO_ID existe
    cursor.execute("SELECT id FROM Ceo WHERE id = %s", (proponente_id,))
    ceo_id = cursor.fetchone()

    if subtema_id and ceo_id:
        try:
            # Insere o projeto na tabela
            cursor.execute("INSERT INTO Projeto (subtema_id, nome, descricao, data_criacao, ceo_id) VALUES (%s, %s, %s, %s, %s)",
                           (subtema_id[0], projeto, None, datetime.now(), ceo_id[0]))
            connection.commit()
            logging.info(f"Projeto {projeto} inserido com sucesso!")
        except psycopg2.Error as e:
            logging.error(f"Erro ao inserir o projeto {projeto}: {e}")
            connection.rollback()
    else:
        logging.error(f"Subtema ID ou CEO ID não encontrado para o projeto {projeto}")

cursor.close()
connection.close()

logging.info('Dados dos Projetos inseridos!')
