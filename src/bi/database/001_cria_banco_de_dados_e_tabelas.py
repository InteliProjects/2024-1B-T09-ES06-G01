import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os
import logging

# Configura o logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', encoding='utf-8')

# Carrega configurações do arquivo .env
load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = "coffee-break-database"

# Função para conectar ao PostgreSQL
def connect_db(database="postgres"):
    conn = psycopg2.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=database,
        port=DB_PORT
    )
    conn.autocommit = True
    return conn

# Cria o banco de dados (se não existir)
def create_database():
    logging.info("Criando banco de dados...")
    conn = connect_db()
    cur = conn.cursor()
    # Verifica se o banco de dados já existe
    cur.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s", (DB_NAME,))
    exists = cur.fetchone()
    if not exists:
        # Se não existe, cria o banco de dados
        cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(DB_NAME)))
        logging.info("Banco de dados criado com sucesso!")
    else:
        logging.info("Banco de dados já existe, não é necessário criar.")
    cur.close()
    conn.close()

# Cria as tabelas (se não existirem)
def create_tables():
    logging.info("Criando tabelas...")
    commands = (
        """
        CREATE TABLE IF NOT EXISTS Ceo (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(255),
            biografia VARCHAR(255),
            email VARCHAR(255),
            senha VARCHAR(255),
            celular VARCHAR(255),
            foto VARCHAR(255),
            cargo VARCHAR(255),
            empresa_nome VARCHAR(255),
            empresa_link VARCHAR(255),
            email_contato VARCHAR(255),
            linkedin VARCHAR(255)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Notificacao (
            id SERIAL PRIMARY KEY,
            ceo_id INT,
            mensagem VARCHAR(255),
            status VARCHAR(255),
            timestamp TIMESTAMP,
            FOREIGN KEY (ceo_id) REFERENCES Ceo(id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Macrotema (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(255),
            descricao VARCHAR(255)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Subtema (
            id SERIAL PRIMARY KEY,
            macrotema_id INT,
            nome VARCHAR(255),
            descricao VARCHAR(255),
            FOREIGN KEY (macrotema_id) REFERENCES Macrotema(id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Projeto (
            id SERIAL PRIMARY KEY,
            subtema_id INT,
            nome VARCHAR(255),
            descricao VARCHAR(255),
            data_criacao TIMESTAMP,
            ceo_id INT,
            FOREIGN KEY (subtema_id) REFERENCES Subtema(id),
            FOREIGN KEY (ceo_id) REFERENCES Ceo(id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Interacao (
            id SERIAL PRIMARY KEY,
            ceo_id INT,
            projeto_id INT,
            tipo VARCHAR(255),
            status VARCHAR(255),
            data TIMESTAMP,
            FOREIGN KEY (ceo_id) REFERENCES Ceo(id),
            FOREIGN KEY (projeto_id) REFERENCES Projeto(id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Atualizacao (
            id SERIAL PRIMARY KEY,
            ceo_id INT,
            projeto_id INT,
            descricao VARCHAR(255),
            data TIMESTAMP,
            FOREIGN KEY (ceo_id) REFERENCES Ceo(id),
            FOREIGN KEY (projeto_id) REFERENCES Projeto(id)
        );
        """
    )
    conn = connect_db(DB_NAME)
    cur = conn.cursor()
    for command in commands:
        cur.execute(command)
    logging.info("Tabelas criadas com sucesso!")
    cur.close()
    conn.close()

if __name__ == "__main__":
    logging.info(f"Iniciando processo de criação do {DB_NAME}...")
    create_database()
    create_tables()
    logging.info(f"Processo de criação do {DB_NAME} concluído!")
