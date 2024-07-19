import unittest
from backend.projetos.services import ProjetoService
from backend.projetos.models import PROJETO
from backend.common.database import Database
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv('DB_URL')


class TesteProjetos(unittest.TestCase):
    def setUp(self):
        self.projetos_service = ProjetoService(PROJETO)
        Database.initialize(DATABASE_URL)

    def teste_obter_todos_projetos(self):
        projeto_service = ProjetoService(PROJETO)
        projetos = projeto_service.get_projetos()
        self.assertGreater(len(projetos), 1)

    def teste_obter_projeto(self):
        projeto_service = ProjetoService(PROJETO)
        projeto = projeto_service.get_projeto(1000)
        self.assertEqual(projeto['id'], 1000)

    def teste_atualizar_projeto(self):
        projeto_service = ProjetoService(PROJETO)
        projeto_service.put_projeto(1000, {"nome": 'nome de teste 1'})
        projeto_service.put_projeto(1000, {"nome": 'nome de teste 2'})
        projeto = projeto_service.get_projeto(1000)
        self.assertEqual(projeto['nome'], 'nome de teste 2')

    def teste_criar_projeto(self):
        projeto_service = ProjetoService(PROJETO)
        projetoId = projeto_service.post_projeto({"nome": "TESTE_Projeto para teste", "descricao": "TESTE_Descricao do projetoX", "subtema_id": 1, "ceo_id": 23})
        projeto = projeto_service.get_projeto(projetoId)
        self.assertEqual(projeto['nome'], "TESTE_Projeto para teste")

    def teste_deletar_projeto(self):
        projeto_service = ProjetoService(PROJETO)
        projetoId_criado = projeto_service.post_projeto({"nome": "TESTE_Projeto para teste", "descricao": "TESTE_Descricao do projetoX", "subtema_id": 1, "ceo_id": 23})
        projetoId_deletado = projeto_service.delete_projeto(projetoId_criado)
        self.assertEqual(projetoId_criado, projetoId_deletado)
