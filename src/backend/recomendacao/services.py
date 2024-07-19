from datetime import datetime
# Certifique-se de que o caminho para o notebook esteja correto
from bi.modelo_conteudo import gerar_recomendacoes

class RecomendacaoService:
    def __init__(self, recomendacao_model, ceo_model, projeto_model, interacao_model, subtema_model, macrotema_model):
        self.recomendacao_model = recomendacao_model
        self.ceo_model = ceo_model
        self.projeto_model = projeto_model
        self.interacao_model = interacao_model
        self.subtema_model = subtema_model
        self.macrotema_model = macrotema_model

    def gerar_recomendacao(self, usuario_id):
        rec = gerar_recomendacoes(usuario_id)
        obj = [int(projeto['id']) for projeto in rec] if rec else None

        obj = obj[:49] if obj else None

        if obj:
            query = f"SELECT * FROM Recomendacao WHERE ceo_id = {usuario_id}"
            recomendacoes = self.recomendacao_model.execute_query(query)
            recomendacoes_existentes = set(int(projeto.to_dict()['projeto_id']) for projeto in recomendacoes) if recomendacoes else set()

            novas_recomendacoes = []
            for projeto in obj:
                if projeto not in recomendacoes_existentes:
                    print(f"Projeto {projeto} não recomendado o CEO {usuario_id}")
                    novas_recomendacoes.append({'ceo_id': usuario_id, 'projeto_id': projeto, 'pontuacao': 0, 'tipo': 'recomendacao', 'data': datetime.now()})
                else:
                    print(f"Projeto {projeto} já recomendado para o CEO {usuario_id}")

            if novas_recomendacoes:
                self.post_recomendacao_bulk(novas_recomendacoes)

            recomendacoes_finais = self.recomendacao_model.execute_query(query)

            projetos_ids = [recomendacao.to_dict()['projeto_id'] for recomendacao in recomendacoes_finais]
            projetos = {projeto.id: projeto.to_dict() for projeto in self.projeto_model.find_by_ids(projetos_ids)}
            ceos = {projeto['ceo_id']: self.ceo_model.find_by_id(projeto['ceo_id']).to_dict() for projeto in projetos.values()}

            # Obter todas as interações de sinergia de uma vez
            interacoes_query = f"SELECT * FROM Interacao WHERE projeto_id IN ({','.join(map(str, projetos_ids))}) AND tipo = 'sinergia'"
            interacoes = self.interacao_model.execute_query(interacoes_query) or []

            # Mapeia as interações por projeto_id
            interacoes_por_projeto = {}
            for interacao in interacoes:
                interacao_dict = interacao.to_dict()
                projeto_id = interacao_dict['projeto_id']
                if projeto_id not in interacoes_por_projeto:
                    interacoes_por_projeto[projeto_id] = []
                interacoes_por_projeto[projeto_id].append(interacao_dict['ceo_id'])

            # Obter todos os subtemas dos projetos de uma vez
            subtemas_ids = {projeto['subtema_id'] for projeto in projetos.values()}
            subtemas = {subtema.id: subtema.to_dict() for subtema in self.subtema_model.find_by_ids(list(subtemas_ids))}

            # Obter todos os macrotemas dos subtemas de uma vez
            macrotemas_ids = {subtema['macrotema_id'] for subtema in subtemas.values()}
            macrotemas = {macrotema.id: macrotema.to_dict() for macrotema in self.macrotema_model.find_by_ids(list(macrotemas_ids))}

            # Obter todos os CEOs de sinergia de uma vez, se houver
            ceos_sinergia = {}
            ceos_sinergia_ids = {interacao.to_dict()['ceo_id'] for interacao in interacoes}
            if ceos_sinergia_ids:
                ceos_sinergia = {ceo.id: ceo.to_dict() for ceo in self.ceo_model.find_by_ids(list(ceos_sinergia_ids))}

            for i in range(len(recomendacoes_finais)):
                recomendacao = recomendacoes_finais[i].to_dict()
                projeto_id = recomendacao['projeto_id']
                projeto = projetos[projeto_id]
                subtema = subtemas[projeto['subtema_id']]
                macrotema = macrotemas[subtema['macrotema_id']]
                recomendacao["projeto"] = projeto
                recomendacao["projeto"]["subtema_nome"] = subtema['nome']
                recomendacao["projeto"]["macrotema_nome"] = macrotema['nome']

                ceos_projeto = [ceos[projeto['ceo_id']]]  # Inclui o CEO do projeto
                if projeto_id in interacoes_por_projeto:
                    for ceo_id in interacoes_por_projeto[projeto_id]:
                        if ceo_id in ceos_sinergia:
                            ceos_projeto.append(ceos_sinergia[ceo_id])

                recomendacao["ceos"] = ceos_projeto  # Adiciona todos os CEOs com sinergia
                recomendacoes_finais[i] = recomendacao

            return recomendacoes_finais

        return None


    def post_recomendacao_bulk(self, recomendacoes):
        if not recomendacoes:
            return

        values = ', '.join(
            f"({recomendacao['ceo_id']}, {recomendacao['projeto_id']}, {recomendacao['pontuacao']}, '{recomendacao['tipo']}' , '{recomendacao['data']}')"
            for recomendacao in recomendacoes
        )
        
        query = f"""
        INSERT INTO Recomendacao (ceo_id, projeto_id, pontuacao, tipo, data)
        VALUES {values}
        ON CONFLICT (ceo_id, projeto_id) DO NOTHING
        """
        
        self.recomendacao_model.execute_query(query)
    
    def get_recomendacao_by_id(self, recomendacao_id):
        rec = self.recomendacao_model.find_by_id(recomendacao_id)
        if rec:
            return rec.to_dict()
        return None

    def get_all_recomendacao(self):
        rec = self.recomendacao_model.find_all()
        if rec:
            return rec
        return None
    
    def post_recomendacao(self, dados):
        now = datetime.now()
        recomendacao = self.recomendacao_model.insert(ceo_id=dados['ceo_id'], data=now, pontuacao=dados['pontuacao'], projeto_id=dados['projeto_id'], tipo=dados['tipo'])
        if recomendacao:
            return recomendacao
        return None

    def delete_recomendacao(self, recomendacao_id):
        # Verifica se o projeto existe
        recomendacao = self.get_recomendacao_by_id(recomendacao_id)
        if not recomendacao:
            return None
        # Apaga o projeto
        self.recomendacao_model.delete(recomendacao_id)
        # Verifica se o projeto foi apagado
        recomendacao_apagada = self.get_recomendacao_by_id(recomendacao_id)
        if recomendacao_apagada:
            None
        return recomendacao_apagada
    
    def put_recomendacao(self, recomendacao_id, dados):
        campos_para_atualizar = {}
        # Lista dos campos permitidos que podem ser atualizados
        campos_permitidos = ['pontuacao']
        # Itera sobre os campos permitidos e verifica se eles estão presentes nos dados fornecidos
        campos_para_atualizar['pontuacao'] = dados['pontuacao']
        # Atualiza a recomendação apenas com os campos presentes nos dados fornecidos
        self.recomendacao_model.update(recomendacao_id, **campos_para_atualizar)
        # Verifica se a recomendação foi atualizado
        recomendacao = self.get_recomendacao_by_id(recomendacao_id)
        campos_diferentes = False
        if dados['pontuacao'] != recomendacao['pontuacao']:
            campos_diferentes = True

        if campos_diferentes:
            return None
        
    def obter_projetos_recomendados(self, ids):
        # Obtém o último ID de CEO na base de dados
        formatted_ids = ','.join(map(str, ids))
        query = f"SELECT * FROM Projeto WHERE id IN ({formatted_ids})"
        result = self.recomendacao_model.execute_query(query)
        if result:
            return result

        return None