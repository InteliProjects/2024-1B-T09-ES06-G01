import os
import unittest
import json
import psycopg2
import requests
from dotenv import load_dotenv
from xmlrunner import XMLTestRunner

load_dotenv()

class SinergiaIntegrationTest(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://localhost:80/projetos/sinergia/'
        self.conn = psycopg2.connect(
            dbname="coffee-break-database",
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            host=os.getenv('DB_HOST'),
        )
        self.cur = self.conn.cursor()

    def tearDown(self):
        self.cur.execute("DELETE FROM Interacao WHERE tipo = %s AND ceo_id = %s AND projeto_id = %s", ('sinergia', 1, 1))
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def test_post_sinergia(self):
        sinergia_data = {
            "ceo_id": 1,
            "projeto_id": 1
        }
        response = requests.post(self.base_url, data=json.dumps(sinergia_data), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200, f"O status code foi diferente de 200: {response.status_code}")
        data = response.json()
        self.assertIsNotNone(data, f"O retorno foi None")
        self.assertIsInstance(data, int, f"O tipo de retorno foi diferente de int: {type(data)}")

        # Verifica se a sinergia foi inserida no banco de dados
        self.cur.execute("SELECT tipo, estado FROM Interacao WHERE id = %s", (data,))
        interacao = self.cur.fetchone()
        self.assertEqual(interacao[0], 'sinergia', f"O tipo da interação inserida foi diferente do esperado: {interacao[0]}") # type: ignore
        self.assertEqual(interacao[1], 'pendente', f"O estado da interação inserida foi diferente do esperado: {interacao[1]}") # type: ignore

if __name__ == '__main__':
    # cria um xml no mesmo diretório do arquivo de teste
    path = os.path.join(os.path.dirname(__file__), 'test_sinergia_integration.xml')
    with open(path, 'wb') as output:
        runner = XMLTestRunner(output=output) # type: ignore
        unittest.main(testRunner=runner)
