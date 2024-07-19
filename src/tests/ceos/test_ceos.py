import unittest
from unittest.mock import Mock, patch
from backend.ceos.services import CeoService
from backend.ceos.models import CeoModel
from backend.common.database import Database
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv('DB_URL')

class TestCeoService(unittest.TestCase):
    def setUp(self):
        self.ceo_service = CeoService(CeoModel)
        Database.initialize(DATABASE_URL)

    def test_get_ceo_by_id_found(self):
        mock = {
            "biografia": None,
            "cargo": "COO",
            "celular": None,
            "email_contato": None,
            "empresa_link": None,
            "empresa_nome": "Fundação Banco do Brasil",
            "estado": "ativo",
            "foto": None,
            "id": 1,
            "linkedin": None,
            "nome": "Braian Goulart"
        }

        # Mockando o método find_by_id do modelo
        with patch.object(CeoModel, 'find_by_id', return_value=CeoModel(**mock)):
            result = self.ceo_service.get_ceo(1)
            for key in mock:
                self.assertEqual(result[key], mock[key])

    def test_get_ceo_by_id_not_found(self):
        # Mockando o método find_by_id do modelo
        with patch.object(CeoModel, 'find_by_id', return_value=None):
            result = self.ceo_service.get_ceo(9999)
            self.assertIsNone(result)

    def test_get_ceos(self):
        mock_ceos = [
            CeoModel(id=1, nome="Braian Goulart", biografia=None, cargo="COO", empresa_nome="Fundação Banco do Brasil", estado="ativo"),
            CeoModel(id=2, nome="Ana Silva", biografia=None, cargo="CEO", empresa_nome="Tech Inc", estado="ativo")
        ]

        # Mockando o método find_all do modelo
        with patch.object(CeoModel, 'find_all', return_value=mock_ceos):
            result = self.ceo_service.get_ceos()
            self.assertIsInstance(result, list)
            self.assertEqual(len(result), len(mock_ceos))
            for ceo in result:
                self.assertIn('id', ceo)
                self.assertIn('nome', ceo)
                self.assertIn('cargo', ceo)
                
    def test_create_ceo_integration(self):
        # Preparar os dados do novo CEO
        ceo_data = {
            "nome": "Novo CEO",
            "cargo": "CEO",
            "empresa_nome": "Nova Empresa",
            "estado": "ativo"
        }

        # Obter o último ID diretamente do serviço, sem mocks
        last_id = self.ceo_service.get_last_ceo_id()
        
        # Criar um novo CEO e obter o ID retornado
        new_ceo_id = self.ceo_service.create_ceo(ceo_data)
        
        # Verificar se o novo ID é o último ID incrementado por 1
        self.assertEqual(new_ceo_id, last_id + 1)
        
        # Verificar se o CEO pode ser encontrado e se os dados estão corretos
        created_ceo = self.ceo_service.get_ceo(new_ceo_id)
        for key in ceo_data:
            if key != 'id':
                self.assertEqual(created_ceo[key], ceo_data[key])
                
    def test_update_ceo_integration(self):
        # Preparar os dados do CEO a ser atualizado
        ceo_data = {
            "nome": "CEO Atualizado",
            "cargo": "CEO",
            "empresa_nome": "Empresa Atualizada",
            "estado": "ativo"
        }
        
        # Criar um novo CEO e obter o ID retornado
        new_ceo_id = self.ceo_service.create_ceo(ceo_data)
        
        # Atualizar os dados do CEO
        updated_ceo_data = {
            "nome": "CEO Atualizado 2",
            "empresa_nome": "Empresa Atualizada 2"
        }
        
        self.ceo_service.update_ceo(new_ceo_id, updated_ceo_data)
        
        # Verificar se os dados do CEO foram atualizados corretamente
        updated_ceo = self.ceo_service.get_ceo(new_ceo_id)
        for key in updated_ceo_data:
            self.assertEqual(updated_ceo[key], updated_ceo_data[key])
            
    def test_delete_ceo_integration(self):
        # Preparar os dados do CEO a ser deletado
        ceo_data = {
            "nome": "CEO Deletado",
            "cargo": "CEO",
            "empresa_nome": "Empresa Deletada",
            "estado": "ativo"
        }
        
        # Criar um novo CEO e obter o ID retornado
        new_ceo_id = self.ceo_service.create_ceo(ceo_data)
        
        # Deletar o CEO
        self.ceo_service.delete_ceo(new_ceo_id)
        
        # Verificar se o CEO foi deletado corretamente
        deleted_ceo = self.ceo_service.get_ceo(new_ceo_id)
        self.assertIsNone(deleted_ceo)


if __name__ == '__main__':
    unittest.main()
