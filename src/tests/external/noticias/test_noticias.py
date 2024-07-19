import unittest
from backend.external.noticias.app import consumir_API_noticias

# Teste unitários da API de Notícias
class TesteNoticias(unittest.TestCase):
    def teste_obter_todos_noticias(self):
        resposta = consumir_API_noticias('saude')
        self.assertIn('status', resposta, "Resposta não contém o campo 'status'")
        self.assertEqual(resposta['status'], 'success', f"Esperado status 'success', mas recebeu {resposta['status']}")
        self.assertIn('data', resposta, "Resposta não contém o campo 'data'")

    def teste_obter_todos_noticias_erro(self):
        resposta = consumir_API_noticias('')
        self.assertIn('status', resposta, "Resposta não contém o campo 'status'")
        self.assertEqual(resposta['status'], 'error', f"Esperado status 'error', mas recebeu {resposta['status']}")
        self.assertIn('message', resposta, "Resposta não contém o campo 'message'")

if __name__ == '__main__':
    unittest.main()
