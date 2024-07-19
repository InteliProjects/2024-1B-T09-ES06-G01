import unittest
from unittest.mock import Mock, patch
from backend.recomendacao.services import RecomendacaoService
from backend.recomendacao.models import Recomendacao
from backend.common.database import Database
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv('DB_URL')

class TesteRecomendacaoService(unittest.TestCase):
    def setUp(self):
        self.recomendacao_service = RecomendacaoService(Recomendacao)
        Database.initialize(DATABASE_URL)

    def teste_obter_todos_recomendacoes(self):
        recomendacao_service = RecomendacaoService(Recomendacao)
        recomendacoes = recomendacao_service.get_all_recomendacao()
        self.assertGreater(len(recomendacoes), 1)

    def teste_obter_recomendacao(self):
        recomendacao_service = RecomendacaoService(Recomendacao)
        recomendacao = recomendacao_service.get_recomendacao_by_id(8)
        self.assertEqual(recomendacao['id'], 8)

    def teste_criar_recomendacao(self):
        recomendacao_service = RecomendacaoService(Recomendacao)
        recomendacaoId = recomendacao_service.post_recomendacao({"ceo_id": 30, "pontuacao": 5, "projeto_id": 1000, "tipo": "coolaborativo"})
        recomendacao = recomendacao_service.get_recomendacao_by_id(recomendacaoId)
        self.assertEqual(recomendacao['ceo_id'], 30)

    def teste_atualizar_recomendacao(self):
        recomendacao_service = RecomendacaoService(Recomendacao)
        recomendacao_service.put_recomendacao(8, {"pontuacao": 1})
        recomendacao = recomendacao_service.get_recomendacao_by_id(8)
        self.assertEqual(recomendacao['pontuacao'], 1)

if __name__ == '__main__':
    unittest.main()