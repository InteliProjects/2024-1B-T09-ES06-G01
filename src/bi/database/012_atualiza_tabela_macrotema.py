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
DB_NAME = "coffee-break-database"

# Configuração do logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', encoding='utf-8')

# Mapeamento de macrossetor para macrotema e caminho do ícone
macrossetor_para_macrotema = {
    "Educação": ("produtividade", "produtividade.svg"),
    "Serviços Sociais": ("diversidade", "diversidade.svg"),
    "Tecnologia e Inovação": ("produtividade", "produtividade.svg"),
    "Sustentabilidade": ("conservação", "conservacao.svg"),
    "Saúde e Bem-estar": ("bem-estar", "bem-estar.svg"),
    "Meio Ambiente": ("conservação", "conservacao.svg"),
    "Ciência e Pesquisa": ("produtividade", "produtividade.svg"),
    "Tecnologia e Informação": ("produtividade", "produtividade.svg"),
    "Transporte e Logística": ("redução", "reducao.svg"),
    "Arte e Cultura": ("diversidade", "diversidade.svg"),
    "Energia e Recursos": ("redução", "reducao.svg"),
    "Empreendedorismo e Inovação": ("produtividade", "produtividade.svg"),
    "Desenvolvimento Urbano e Infraestrutura": ("produtividade", "produtividade.svg"),
    "Engenharia": ("produtividade", "produtividade.svg"),
    "Desenvolvimento Econômico e Empresarial": ("produtividade", "produtividade.svg"),
    "Desenvolvimento Comunitário": ("diversidade", "diversidade.svg"),
    "Agricultura e Alimentação": ("conservação", "conservacao.svg"),
    "Economia e Finanças": ("produtividade", "produtividade.svg"),
    "Gestão e Recursos Humanos": ("produtividade", "produtividade.svg"),
    "Direito e Governança": ("integridade", "integridade.svg"),
    "Tecnologia e Dados": ("produtividade", "produtividade.svg"),
    "Transporte e Tecnologia": ("redução", "reducao.svg"),
    "Educação e Meio Ambiente": ("conservação", "conservacao.svg"),
    "Tecnologia e Educação": ("produtividade", "produtividade.svg"),
    "Tecnologia e Meio Ambiente": ("conservação", "conservacao.svg"),
    "Tecnologia e Saúde": ("bem-estar", "bem-estar.svg"),
    "Estratégia e Gestão": ("produtividade", "produtividade.svg"),
    "Comunicação e Mídia": ("produtividade", "produtividade.svg"),
    "Tecnologia e Comunicação": ("produtividade", "produtividade.svg"),
    "Saúde e Infraestrutura": ("bem-estar", "bem-estar.svg"),
    "Saúde e Pesquisa": ("bem-estar", "bem-estar.svg"),
    "Geral e Diversificado": ("diversidade", "diversidade.svg"),
    "Turismo e Lazer": ("bem-estar", "bem-estar.svg"),
    "Desporto e Lazer": ("bem-estar", "bem-estar.svg"),
    "Desenvolvimento Internacional": ("diversidade", "diversidade.svg"),
    "Turismo e Tecnologia": ("bem-estar", "bem-estar.svg"),
    "Saúde e Indústria": ("bem-estar", "bem-estar.svg"),
    "Saúde e Tecnologia": ("bem-estar", "bem-estar.svg"),
    "Saúde e Inovação": ("bem-estar", "bem-estar.svg"),
    "Marketing e Comunicação": ("produtividade", "produtividade.svg")
}

# Conecta ao banco de dados
connection = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS, port=DB_PORT)
cursor = connection.cursor()

# Adiciona a nova coluna caminho_icone
try:
    cursor.execute("ALTER TABLE Macrotema ADD COLUMN caminho_icone VARCHAR(255);")
    logging.info("Coluna caminho_icone adicionada com sucesso!")
except Exception as e:
    logging.error(f"Erro ao adicionar coluna caminho_icone: {e}")

# Atualiza os registros da tabela Macrotema
for macrossetor, (macrotema, caminho_icone) in macrossetor_para_macrotema.items():
    try:
        cursor.execute(
            """
            UPDATE Macrotema
            SET nome = %s, caminho_icone = %s
            WHERE nome = %s
            """,
            (macrotema, caminho_icone, macrossetor)
        )
        logging.info(f"Macrotema {macrossetor} atualizado para {macrotema} com ícone {caminho_icone} com sucesso!")
    except Exception as e:
        logging.error(f"Erro ao atualizar macrotema {macrossetor} para {macrotema} com ícone {caminho_icone}: {e}")

# Commita as alterações
connection.commit()
cursor.close()
connection.close()

logging.info('Dados dos Macrotemas atualizados!')
