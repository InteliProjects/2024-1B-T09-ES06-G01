import os
import unittest
import json
import psycopg2
import requests
from dotenv import load_dotenv
from xmlrunner import XMLTestRunner

load_dotenv()

class CeoIntegrationTest(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://localhost:80/ceos/'
        self.conn = psycopg2.connect(
            dbname="coffee-break-database",
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            host=os.getenv('DB_HOST'),
        )
        self.cur = self.conn.cursor()

    def tearDown(self):
        self.cur.execute("DELETE FROM Ceo WHERE nome = %s", ('Novo CEO Unittest',))
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def test_get_ceos(self):
        response = requests.get(self.base_url)
        self.assertEqual(response.status_code, 200, f"O status code foi diferente de 200: {response.status_code}")
        data = response.json()
        self.assertIsInstance(data['ceos'], list, f"O tipo de retorno foi diferente de list: {type(data['ceos'])}")
        self.assertGreater(len(data['ceos']), 0, f"O tamanho da lista foi menor ou igual a 0: {len(data['ceos'])}")

        # Pega o ID do primeiro CEO retornado
        primeiro_ceo_id = data['ceos'][0]['id']

        # Verifica se o primeiro CEO no banco de dados está na resposta
        self.cur.execute("SELECT nome FROM Ceo WHERE id = %s", (primeiro_ceo_id,))
        ceo_nome = self.cur.fetchone()[0] # type: ignore
        self.assertEqual(data['ceos'][0]['nome'], ceo_nome, f"O nome do CEO retornado foi diferente do nome do CEO no banco de dados")

        # Conta quantos CEOs existem no banco de dados
        # E compara com a quantidade de CEOs retornados
        self.cur.execute("SELECT COUNT(*) FROM Ceo")
        quantidade_ceos = self.cur.fetchone()[0] # type: ignore
        self.assertEqual(len(data['ceos']), quantidade_ceos, f"A quantidade de CEOs retornados foi diferente da quantidade de CEOs no banco de dados")

    def test_post_ceo(self):
        ceo_data = {
            "nome": "Novo CEO Unittest",
            "cargo": "CEO",
            "empresa_nome": "Empresa Teste",
            "estado": "ativo",
            "biografia": "Biografia do Novo CEO Unittest",
            "celular": "123456789",
            "email_contato": "teste@empresa.com",
            "empresa_link": "http://empresa.com",
            "foto": "http://empresa.com/foto.jpg",
            "linkedin": "http://linkedin.com/in/teste",
            "email": "novoceo@teste.com",
            "senha": "senha123"
        }
        response = requests.post(self.base_url, data=json.dumps(ceo_data), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 201, f"O status code foi diferente de 201: {response.status_code}")
        data = response.json()
        self.assertIsNotNone(data, f"O retorno foi None")
        self.assertIsInstance(data, dict, f"O tipo de retorno foi diferente de dict: {type(data)}")
        self.assertIn('id', data, "A chave 'id' não está presente no retorno")

        # Verifica se o CEO foi inserido no banco de dados
        self.cur.execute("SELECT nome FROM Ceo WHERE id = %s", (data['id'],))
        ceo_nome = self.cur.fetchone()[0] # type: ignore
        self.assertEqual(ceo_nome, "Novo CEO Unittest", f"O nome do CEO inserido foi diferente do nome do CEO no banco de dados")

if __name__ == '__main__':
    # cria um xml no mesmo diretório do arquivo de teste
    path = os.path.join(os.path.dirname(__file__), 'test_ceo_integration.xml')
    with open(path, 'wb') as output:
        runner = XMLTestRunner(output=output) # type: ignore
        unittest.main(testRunner=runner)
