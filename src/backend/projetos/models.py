from backend.common.database import BaseModel


class ProjetoModel(BaseModel):
    nome_tabela = 'Projeto'

    def __init__(self, id=None, ceo_id=None, subtema_id=None, nome=None, descricao=None, data_criacao=None, estado=None):
        super().__init__(id)
        self.ceo_id = ceo_id
        self.subtema_id = subtema_id
        self.nome = nome
        self.descricao = descricao
        self.data_criacao = data_criacao
        self.estado = estado

    @classmethod
    def from_db_row(cls, row):
        if row:
            return cls(id=row[0], ceo_id=row[5], subtema_id=row[1], nome=row[2],
                       descricao=row[3], data_criacao=row[4], estado=row[6])
        return None
    
    @classmethod
    def from_db_row_projetoxmacrotema(cls, row):
        if row:
            return {'count': row[0], 'nome': row[1]}
        return None



class SubtemaModel(BaseModel):
    nome_tabela = 'Subtema'

    def __init__(self, id=None, nome=None, descricao=None, macrotema_id=None):
        super().__init__(id)
        self.nome = nome
        self.descricao = descricao
        self.macrotema_id = macrotema_id

    @classmethod
    def from_db_row(cls, row):
        if row:
            return cls(id=row[0], nome=row[2], descricao=row[3], macrotema_id=row[1])
        return None
    
    
class MacrotemaModel(BaseModel):
    nome_tabela = 'Macrotema'

    def __init__(self, id=None, nome=None, descricao=None, nome_completo=None):
        super().__init__(id)
        self.nome = nome
        self.descricao = descricao
        self.nome_completo = nome_completo

    @classmethod
    def from_db_row(cls, row):
        if row:
            return cls(id=row[0], nome=row[1], descricao=row[2], nome_completo=row[4])
        return None
    
    
class InteracaoModel(BaseModel):
    nome_tabela = 'Interacao'

    def __init__(self, id=None, ceo_id=None, projeto_id=None, tipo=None, estado=None, data=None, atualizacao=None):
        super().__init__(id)
        self.ceo_id = ceo_id
        self.projeto_id = projeto_id
        self.tipo = tipo
        self.estado = estado
        self.data = data
        self.atualizacao = atualizacao
        
    @classmethod
    def from_db_row(cls, row):
        if row:
            return cls(id=row[0], ceo_id=row[1], projeto_id=row[2], tipo=row[3], estado=row[4], data=row[5], atualizacao=row[6])
        return None

class AtualizaoModel(BaseModel):
    nome_tabela = 'Atualizacao'

    def __init__(self, id=None, data=None, projeto_id=None, descricao=None):
        super().__init__(id)
        self.projeto_id = projeto_id
        self.descricao = descricao
        self.data = data
        
    @classmethod
    def from_db_row(cls, row):
        if row:
            return cls(id=row[0], projeto_id=row[1], descricao=row[2], data=row[3])
        return None
    
    
