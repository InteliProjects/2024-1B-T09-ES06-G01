import unittest
from backend.external.avatar.app import AvatarGenerator


class TestAvatarGenerator(unittest.TestCase):
    def setUp(self):
        self.avatar_generator = AvatarGenerator()

    def test_gerar_avatar(self):
        """Testa se a URL do avatar é gerada corretamente."""
        semente = "testavatar"
        url = self.avatar_generator.gerar_avatar(semente)
        self.assertTrue(url.startswith(self.avatar_generator.base_url))

    def test_gerar_avatares_fixos(self):
        """Testa se o dicionário de avatares é gerado corretamente."""
        num_avatares = 5
        avatares = self.avatar_generator.gerar_avatares_fixos(num_avatares)
        self.assertEqual(len(avatares), num_avatares)
        for key, url in avatares.items():
            self.assertTrue(url.startswith(self.avatar_generator.base_url))

if __name__ == '__main__':
    unittest.main()
