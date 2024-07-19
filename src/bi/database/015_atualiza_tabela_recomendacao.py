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

# Identificar registros duplicados
cursor.execute("""
SELECT ceo_id, projeto_id, COUNT(*)
FROM Recomendacao
GROUP BY ceo_id, projeto_id
HAVING COUNT(*) > 1;
""")
duplicados = cursor.fetchall()

if duplicados:
    print("Registros duplicados encontrados:", duplicados)
    # Remover registros duplicados
    cursor.execute("""
    DELETE FROM Recomendacao
    WHERE ctid NOT IN (
        SELECT min(ctid)
        FROM Recomendacao
        GROUP BY ceo_id, projeto_id
    );
    """)
    connection.commit()
    print("Registros duplicados removidos.")

# Adicionar a restrição única
cursor.execute("""
ALTER TABLE Recomendacao ADD CONSTRAINT unique_ceo_projeto UNIQUE (ceo_id, projeto_id);
""")
connection.commit()
print("Restrição única adicionada.")

cursor.close()
connection.close()

logging.info('Migration para adicionar constraint unique na tabela de Recomendacao concluída com sucesso!')
