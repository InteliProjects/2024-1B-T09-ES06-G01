from backend.common.database import BaseModel

# Definição da classe CeoModel que herda de BaseModel, um modelo base para a interação com o banco de dados
class CeoModel(BaseModel):
    # Nome da tabela no banco de dados que esta classe representa
    nome_tabela = 'Ceo'

    # Construtor da classe, inicializa uma instância de CeoModel com os dados fornecidos
    def __init__(self, id=None, nome=None, biografia=None, email=None, senha=None, celular=None, 
                 foto=None, cargo=None, empresa_nome=None, empresa_link=None, email_contato=None,
                 linkedin=None, estado=None):
        super().__init__(id) # Chama o construtor da classe base para lidar com o ID
        self.nome = nome 
        self.biografia = biografia 
        self.email = email 
        self._senha = senha 
        self.celular = celular 
        self.foto = foto 
        self.cargo = cargo 
        self.empresa_nome = empresa_nome 
        self.empresa_link = empresa_link 
        self.email_contato = email_contato 
        self.linkedin = linkedin 
        self.estado = estado 
        
    # Método de classe para criar uma instância de CeoModel a partir de uma linha de dados do banco
    @classmethod
    def from_db_row(cls, row):
        # Se a linha contém dados, cria uma nova instância utilizando esses dados
        if row:
            return cls(id=row[0], nome=row[1], biografia=row[2], email=row[3], senha=row[4],
                       celular=row[5], foto=row[6], cargo=row[7], empresa_nome=row[8],
                       empresa_link=row[9], email_contato=row[10], linkedin=row[11], estado=row[12])
        return None # Se não há dados, retorna None
