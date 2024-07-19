import os
import pandas as pd
import logging
import psycopg2
from dotenv import load_dotenv

# Carrega configurações do arquivo .env
load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = "coffee-break-database"

# Configuração do logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', encoding='utf-8')

logging.info('Configurando os dataframes...')

# Obter o diretório atual onde este script está sendo executado
diretorio_atual = os.getcwd()

# Navegar para o diretório do arquivo de dados a partir do diretório atual
caminho_arquivo_raw = os.path.join(diretorio_atual, 'src', 'bi', 'data', 'raw', 'base-de-dados.xlsx')

# Cria os dataframes a partir do arquivo
df_ceos = pd.read_excel(caminho_arquivo_raw, sheet_name='ds-c-levels', header=0)

logging.info('Dataframes configurados com sucesso!')

# Selecionar colunas específicas relevantes para a tabela 'Ceo'
df_ceos = df_ceos[['id', 'proponente', 'nome da empresa', 'cargo']]

# Renomear colunas para corresponder à tabela de banco de dados
df_ceos.rename(columns={
    'proponente': 'nome',
    'nome da empresa': 'empresa_nome',
    'cargo': 'cargo',
}, inplace=True)

# Exibindo os dados dos CEOs
logging.info('Dados dos CEOs:')
logging.info(df_ceos)

connection = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS, port=DB_PORT)
cursor = connection.cursor()

# Para cada linha do dataframe, insere os dados na tabela 'Ceo'
for index, row in df_ceos.iterrows():
    try:
        cursor.execute(
            """
            INSERT INTO Ceo (id, nome, biografia, email, senha, celular, foto, cargo, empresa_nome, empresa_link, email_contato, linkedin) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """,
            (row['id'], row['nome'], None, None, None, None, None, row['cargo'], row['empresa_nome'], None, None, None)
        )
    # Erro de pk duplicada
    except:
        logging.error(f"CEO {row['nome']} já cadastrado.")

# Commita as alterações
connection.commit()
cursor.close()
connection.close()

logging.info('Dados dos CEOs inseridos!')
