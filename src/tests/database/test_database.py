import unittest
from backend.common.database import Database, BaseModel
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv('DB_URL')

# Define a classe Mock que herda de BaseModel
class Mock(BaseModel):
    nome_tabela = 'Mock'

    @classmethod
    def from_db_row(cls, row):
        return {'id': row[0], 'message': row[1]}

class TestDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Inicia a conexão com o banco de dados
        # e cria a tabela Mock
        Database.initialize(DATABASE_URL)
        with Database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Mock (
                    id SERIAL PRIMARY KEY,
                    message TEXT
                );
            """)
            conn.commit()

    @classmethod
    def tearDownClass(cls):
        # Deleta a tabela Mock e fecha todas as conexões
        with Database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS Mock;")
            conn.commit()
        Database.close_all_connections()

    def test_insert_and_find_by_id(self):
        # Cria um novo registro
        new_id = Mock.insert(message='Hello World')
        # Busca o registro pelo id
        teste = Mock.find_by_id(new_id)
        
        self.assertIsNotNone(teste)
        self.assertEqual(teste["message"], 'Hello World')

    def test_update_and_delete(self):
        # Cria um novo registro
        new_id = Mock.insert(message='Temporary Message')
        # Atualiza o registro criado
        Mock.update(new_id, message='Updated Message')
        # Busca o registro atualizado e valida a mensagem
        updated_teste = Mock.find_by_id(new_id)
        self.assertEqual(updated_teste['message'], 'Updated Message')
        # Deleta o registro
        Mock.delete(new_id)
        # Valida se o registro foi deletado com sucesso
        deleted_notification = Mock.find_by_id(new_id)
        self.assertIsNone(deleted_notification)

    def test_find_all(self):
        # Insere múltiplos registros
        for i in range(2):
            Mock.insert(message=f'Message {i}')
        # Busca todos os registros
        notifications = Mock.find_all()
        self.assertEqual(len(notifications), 3)

    def test_execute_query(self):
        # Insere um novo registro
        new_id = Mock.insert(message='Query Test')
        # Usa o método execute_query para buscar o registro com sql puro
        result = Mock.execute_query("SELECT * FROM Mock WHERE id = %s", (new_id,))
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['message'], 'Query Test')
