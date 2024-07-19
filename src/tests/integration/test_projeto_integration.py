import os
import unittest
import json
import psycopg2
import requests
from dotenv import load_dotenv
from xmlrunner import XMLTestRunner

load_dotenv()


class ProjetoIntegrationTest(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://localhost:80/projetos/'
        self.conn = psycopg2.connect(
            dbname="coffee-break-database",
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            host=os.getenv('DB_HOST'),
        )
        self.cur = self.conn.cursor()
        self.dir = os.path.dirname(__file__)

    def tearDown(self):
        self.cur.execute("DELETE FROM Projeto WHERE nome = %s", ('Novo Projeto Unittest',))
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def test_get_projetos(self):
        response = requests.get(self.base_url)
        self.assertEqual(response.status_code, 200,  f"O status code foi diferente de 200: {response.status_code}")
        data = response.json()
        self.assertIsInstance(data, list, f"O tipo de retorno foi diferente de list: {type(data)}")
        self.assertGreater(len(data), 0, f"O tamanho da lista foi menor ou igual a 0: {len(data)}")

        # Pega o ID do primeiro projeto retornado
        primeiro_projeto_id = data[0]['id']

        # Verifica se o primeiro projeto no banco de dados está na resposta
        self.cur.execute("SELECT nome FROM Projeto WHERE id = %s", (primeiro_projeto_id,))
        projeto_nome = self.cur.fetchone()[0] # type: ignore
        self.assertEqual(data[0]['nome'], projeto_nome, f"O nome do projeto retornado foi diferente do nome do projeto no banco de dados")
        
        # Conta quantos projetos existem no banco de dados
        # E compara com a quantidade de projetos retornados
        self.cur.execute("SELECT COUNT(*) FROM Projeto")
        quantidade_projetos = self.cur.fetchone()[0] # type: ignore
        self.assertEqual(len(data), quantidade_projetos, f"A quantidade de projetos retornados foi diferente da quantidade de projetos no banco de dados")
        
    def test_post_projeto(self):
        projeto_data = {
            "ceo_id": 1,
            "subtema_id": 1,
            "nome": "Novo Projeto Unittest",
            "descricao": "Descrição do Novo Projeto Unittest",
        }
        response = requests.post(self.base_url, data=json.dumps(projeto_data), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200, f"O status code foi diferente de 200: {response.status_code}")
        data = response.json()
        self.assertIsNotNone(data, f"O retorno foi None")
        self.assertIsInstance(data, int, f"O tipo de retorno foi diferente de int: {type(data)}")

        # Verifica se o projeto foi inserido no banco de dados
        self.cur.execute("SELECT nome FROM Projeto WHERE id = %s", (data,))
        projeto_nome = self.cur.fetchone()[0] # type: ignore
        self.assertEqual(projeto_nome, "Novo Projeto Unittest", f"O nome do projeto inserido foi diferente do nome do projeto no banco de dados")

if __name__ == '__main__':
    # cria um xml no mesmo diretório do arquivo de teste
    path = os.path.join(os.path.dirname(__file__), 'test_projeto_integration.xml')
    with open(path, 'wb') as output:
        runner = XMLTestRunner(output=output) # type: ignore
        unittest.main(testRunner=runner)
