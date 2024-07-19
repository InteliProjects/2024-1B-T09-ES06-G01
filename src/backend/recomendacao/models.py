from backend.common.database import BaseModel


class Recomendacao(BaseModel):
    nome_tabela = 'Recomendacao'

    def __init__(self, id=None, ceo_id=None, projeto_id=None, pontuacao=None, tipo=None, data=None):
        super().__init__(id)
        self.ceo_id = ceo_id
        self.projeto_id = projeto_id
        self.pontuacao = pontuacao
        self.tipo = tipo
        self.data = data

    @classmethod
    def from_db_row(cls, row):
        if row:
            return cls(id=row[0], tipo=row[1], data=row[2],pontuacao=row[3],ceo_id=row[4],projeto_id=row[5]
                       )
        return None
    
