class CeoService:
    def __init__(self, usuario_model, projeto_model):
        # Inicializa o serviço com o modelo de usuário fornecido
        self.usuario_model = usuario_model
        self.projeto_model = projeto_model
        
    def get_ceo(self, usuario_id):
        ceo = self.usuario_model.find_by_id(usuario_id)
        
        # busca quantidade de projetos do CEO
        query = f"SELECT * FROM Projeto WHERE ceo_id = {usuario_id};"
        
        projetos = self.projeto_model.execute_query(query)
        
        quantidade_projetos = 0
        
        if projetos:
            quantidade_projetos = len(projetos)
        
        if ceo:
            ceo_dict = ceo.to_dict()
            
            ceo_dict['quantidade_projetos'] = quantidade_projetos
            
            return ceo_dict
            
        return None
    
    def get_ceos(self):
         # Obtém todos os CEOs
        usuarios = self.usuario_model.find_all()
        return [usuario.to_dict() for usuario in usuarios] # Converte cada objeto para um dicionário
    
    def get_last_ceo_id(self):
        # Obtém o último ID de CEO na base de dados
        query = "SELECT * FROM Ceo WHERE id = (SELECT MAX(id) FROM Ceo);"
        result = self.usuario_model.execute_query(query)
        last_id = result[0].id if result else 0 # Obtém o maior ID, ou 0 se não houver resultados
        return last_id

    def create_ceo(self, ceo):
        # Cria um novo CEO
        last_id = self.get_last_ceo_id() 
        ceo['id'] = last_id + 1 
        return self.usuario_model.insert(**ceo)
    
    def update_ceo(self, ceo_id, ceo):
        # Atualiza um CEO existente pelo ID
        return self.usuario_model.update(ceo_id, **ceo)
    
    def delete_ceo(self, ceo_id):
        # Deleta um CEO pelo ID
        return self.usuario_model.delete(ceo_id)
    
    def login(self, dados):
        # Verifica se o email e senha são válidos
        query = f"SELECT * FROM Ceo WHERE email = '{dados['email']}' AND senha = '{dados['senha']}';"
        result = self.usuario_model.execute_query(query)
        if result:
            return result[0].id
        return None
    
    def get_dashboard_ceos(self):
        query = " SELECT COUNT(Ceo.id) AS count FROM Ceo"
        result = self.projeto_model.execute_query(query, count_query=True)
        if result:
            # Acessa o valor da contagem no resultado
            ceos_count = result[0][0] if result else 0  # result[0][0] acessa o valor da contagem no primeiro registro
            return ceos_count
        return 0  # Retorna 0 caso não haja resultado

