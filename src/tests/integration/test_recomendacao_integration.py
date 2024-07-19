import os
import unittest
import psycopg2
import requests
from dotenv import load_dotenv
from xmlrunner import XMLTestRunner

load_dotenv()

class RecomendacaoIntegrationTest(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://localhost:80/recomendacoes/recomendar/'
        self.conn = psycopg2.connect(
            dbname="coffee-break-database",
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            host=os.getenv('DB_HOST'),
        )
        self.cur = self.conn.cursor()

    def tearDown(self):
        self.cur.close()
        self.conn.close()

    def test_gerar_recomendacao(self):
        # Escolhe um usuário existente para gerar recomendações
        usuario_id = 1000

        response = requests.get(f"{self.base_url}{usuario_id}")
        self.assertEqual(response.status_code, 200, f"O status code foi diferente de 200: {response.status_code}")
        data = response.json()
        self.assertIsInstance(data, list, f"O tipo de retorno foi diferente de list: {type(data)}")
        self.assertGreater(len(data), 0, f"O tamanho da lista foi menor ou igual a 0: {len(data)}")

        # Pega o ID do primeiro projeto recomendado
        primeiro_projeto_id = data[0]['projeto']['id']

        # Verifica se o primeiro projeto recomendado está no banco de dados
        self.cur.execute("SELECT nome FROM Projeto WHERE id = %s", (primeiro_projeto_id,))
        projeto_nome = self.cur.fetchone()[0]  # type: ignore
        self.assertEqual(data[0]['projeto']['nome'], projeto_nome, f"O nome do projeto retornado foi diferente do nome do projeto no banco de dados")

        # Verifica se a recomendação foi inserida na tabela de Recomendacao
        self.cur.execute("SELECT ceo_id, projeto_id, pontuacao, tipo FROM Recomendacao WHERE ceo_id = %s AND projeto_id = %s", (usuario_id, primeiro_projeto_id))
        recomendacao = self.cur.fetchone()
        self.assertIsNotNone(recomendacao, "A recomendação não foi encontrada na tabela de Recomendacao")
        self.assertEqual(recomendacao[0], usuario_id, f"O ceo_id da recomendação não corresponde ao esperado: {recomendacao[0]}") # type: ignore
        self.assertEqual(recomendacao[1], primeiro_projeto_id, f"O projeto_id da recomendação não corresponde ao esperado: {recomendacao[1]}") # type: ignore
        self.assertEqual(recomendacao[2], 0, f"A pontuacao da recomendação não corresponde ao esperado: {recomendacao[2]}") # type: ignore
        self.assertEqual(recomendacao[3], 'recomendacao', f"O tipo da recomendação não corresponde ao esperado: {recomendacao[3]}") # type: ignore

if __name__ == '__main__':
    # cria um xml no mesmo diretório do arquivo de teste
    path = os.path.join(os.path.dirname(__file__), 'test_recomendacao_integration.xml')
    with open(path, 'wb') as output:
        runner = XMLTestRunner(output=output) # type: ignore
        unittest.main(testRunner=runner)
