# pip install requests
import requests
import random
import string


class AvatarGenerator:
    """
    Classe para gerar avatares utilizando a API DiceBear.
    
    Através desta classe, você pode gerar URLs para imagens de avatares baseadas em sementes determinísticas.
    Esta funcionalidade é útil para manter a consistência de avatares em aplicações onde os usuários
    possam escolher e manter um avatar estável ao longo do tempo.

    Atributos:
        estilo (str): Define o estilo dos avatares gerados. Pode ser alterado para qualquer estilo suportado pela API DiceBear, como 'miniavs', 'bottts', 'avataaars', etc.
    """

    def __init__(self, estilo='miniavs'):
        """
        Inicializa uma instância da classe AvatarGenerator com um estilo específico de avatar.
        
        Parâmetros:
            estilo (str): Estilo dos avatares a ser gerado. O estilo padrão é 'miniavs'.
        """
        self.base_url = "https://api.dicebear.com/8.x"
        self.estilo = estilo

    def gerar_avatar(self, semente):
        """
        Gera um avatar com base em uma semente fixa.

        Parâmetros:
            semente (str): A semente usada para gerar o avatar. Avatares com a mesma semente serão idênticos.

        Retorna:
            str: URL do avatar gerado.

        Levanta:
            Exception: Uma exceção é levantada se houver um problema com a solicitação da API.
        """
        url = f"{self.base_url}/{self.estilo}/svg?seed={semente}"
        response = requests.get(url)
        if response.status_code == 200:
            return url
        else:
            raise Exception("Erro ao gerar o avatar")

    def gerar_avatares_fixos(self, num_avatares):
        """
        Gera um dicionário de avatares usando sementes determinísticas.

        Parâmetros:
            num_avatares (int): Número de avatares para gerar. Cada avatar terá uma semente única.

        Retorna:
            dict: Um dicionário onde cada chave é uma semente e cada valor é a URL do avatar correspondente.

        Descrição:
            Este método gera múltiplos avatares, cada um com uma semente única no formato 'avatar{i}', onde i é um índice numérico.
            Isso é útil para gerar e armazenar um conjunto fixo de avatares em uma aplicação.
        """
        avatares = {}
        for i in range(num_avatares):
            semente = f"avatar{i}"
            avatares[semente] = self.gerar_avatar(semente)
        return avatares
    
    def gerar_avatares_aleatorios(self, num_avatares):
        """
        Gera um dicionário de avatares usando sementes aleatórias.

        Parâmetros:
            num_avatares (int): Número de avatares aleatórios para gerar.

        Retorna:
            dict: Um dicionário onde cada chave é uma semente aleatória e cada valor é a URL do avatar correspondente.

        Descrição:
            Este método gera múltiplos avatares com sementes geradas aleatoriamente. Cada semente é uma combinação aleatória
            de letras e números, garantindo uma grande variedade de avatares únicos.
        """
        avatares = {}
        for _ in range(num_avatares):
            semente = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            avatares[semente] = self.gerar_avatar(semente)
        return avatares

# Exemplo de uso
if __name__ == "__main__":
    avatar_generator = AvatarGenerator()
    avatar_url = avatar_generator.gerar_avatar("exemplo")
    print(avatar_url)
    avatares = avatar_generator.gerar_avatares_fixos(5)
    print(avatares)
    avatares_aleatorios = avatar_generator.gerar_avatares_aleatorios(5)
    print(avatares_aleatorios)
