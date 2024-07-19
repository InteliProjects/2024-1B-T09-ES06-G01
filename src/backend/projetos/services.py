from datetime import datetime
from collections import defaultdict
import requests
import json
from datetime import date
from datetime import datetime


class NotificacaoService:
    def enviar_notificacao(self, evento, dados, sala):
        url = "http://localhost:5000/send_notification"
        payload = {
            "evento": evento,
            "dados": dados,
            "sala": sala
        }
        
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Notificação enviada com sucesso!")
        else:
            print("Falha ao enviar notificação.")


class ProjetoService:
    def __init__(self, projeto_model, ceo_model, subtema_model, macrotema_model, interacao_model, atualizacao_model):
        self.projeto_model = projeto_model
        self.subtema_model = subtema_model
        self.macrotema_model = macrotema_model
        self.interacao_model = interacao_model
        self.ceo_model = ceo_model
        self.notificacao_service = NotificacaoService()
        self.atualizacao_model = atualizacao_model
        
    def enviar_notificacao(self, evento, dados, sala):
        self.notificacao_service.enviar_notificacao(evento, dados, sala)


    def get_projeto(self, projeto_id):
        projeto = self.projeto_model.find_by_id(projeto_id)
        

    def get_projeto(self, projeto_id):
        projeto = self.projeto_model.find_by_id(projeto_id)
        
        if projeto:
            projeto_dict = projeto.to_dict()
            
            subtema = self.subtema_model.find_by_id(projeto_dict['subtema_id'])
            macrotema = self.macrotema_model.find_by_id(subtema.to_dict()['macrotema_id'])
            ceo_principal = self.ceo_model.find_by_id(projeto_dict['ceo_id'])
            
            # Obtém todas as atualizações relacionadas ao projeto
            query = f"SELECT * FROM Atualizacao WHERE projeto_id = {projeto_dict['id']}"
            atualizacoes = self.atualizacao_model.execute_query(query)
            
            # Inicializa a lista de CEOs com o CEO principal
            ceos = [ceo_principal.to_dict()]
            
            # Busca na tabela de interações se existe alguma sinergia
            query = f"SELECT * FROM Interacao WHERE projeto_id = {projeto_id} AND tipo = 'sinergia'"
            interacoes = self.interacao_model.execute_query(query)
            
            if interacoes:
                for interacao in interacoes:
                    ceo = self.ceo_model.find_by_id(interacao.to_dict()['ceo_id'])
                    if ceo:  # Verifique se o CEO existe
                        ceos.append(ceo.to_dict())
            
            projeto_dict['subtema_nome'] = subtema.to_dict()['nome']
            projeto_dict['macrotema_nome'] = macrotema.to_dict()['nome']
            projeto_dict['ceos'] = ceos
            
            # Inicializa a lista de atualizações no projeto_dict
            projeto_dict['atualizacoes'] = []
            
            # Converte a data para o formato brasileiro
            if atualizacoes:
                for atualizacao in atualizacoes:
                    atualizacao_dict = atualizacao.to_dict()
                    data = atualizacao_dict['data'] 
                    if isinstance(data, datetime):
                        atualizacao_dict['data'] = data.strftime("%d/%m/%Y")
                    projeto_dict['atualizacoes'].append(atualizacao_dict)
            
            return projeto_dict
            
        return None




    def get_projetos(self):
        projetos = self.projeto_model.find_all()
        if projetos:
            return projetos
        return None
    
    def post_projeto(self, dados):
        estado = 'inativo'

        # Obtém o objeto datetime atual
        now = datetime.now()

        projeto = self.projeto_model.insert(ceo_id=dados['ceo_id'], subtema_id=dados['subtema_id'], nome=dados['nome'], descricao=dados['descricao'], data_criacao=now, estado=estado)

        return projeto
    
    def put_projeto(self, projeto_id, dados):
        campos_para_atualizar = {}

        # Lista dos campos permitidos que podem ser atualizados
        campos_permitidos = ['subtema_id', 'nome', 'descricao', 'data_criacao', 'estado']

        # Itera sobre os campos permitidos e verifica se eles estão presentes nos dados fornecidos
        for campo in campos_permitidos:
            if campo in dados:
                campos_para_atualizar[campo] = dados[campo]

        # Atualiza o projeto apenas com os campos presentes nos dados fornecidos
        self.projeto_model.update(projeto_id, **campos_para_atualizar)

        # Verifica se o projeto foi atualizado
        projeto = self.get_projeto(projeto_id)

        campos_diferentes = False

        for campo in campos_permitidos:
            if campo in dados:
                if dados[campo] != projeto[campo]: # type: ignore
                    campos_diferentes = True

        if campos_diferentes:
            return None

        return projeto_id
    
    def delete_projeto(self, projeto_id):
        # Verifica se o projeto existe
        projeto = self.get_projeto(projeto_id)

        if not projeto:
            return None

        # Apaga o projeto
        self.projeto_model.delete(projeto_id)

        # Verifica se o projeto foi apagado
        projeto_apagado = self.get_projeto(projeto_id)

        if projeto_apagado:
            return None

        return projeto_id

    def get_projetos_ceo(self, ceo_id):
        query = f"SELECT * FROM Projeto WHERE ceo_id = {ceo_id}"
        
        projetos = self.projeto_model.execute_query(query)
        
        if projetos:
            # adiciona os subtemas e macrotemas aos projetos
            for i in range(len(projetos)):
                projeto_dict = projetos[i].to_dict()
                subtema = self.subtema_model.find_by_id(projeto_dict['subtema_id'])
                subtema_dict = subtema.to_dict()
                macrotema = self.macrotema_model.find_by_id(subtema_dict['macrotema_id'])
                macrotema_dict = macrotema.to_dict()
                ceo_principal = self.ceo_model.find_by_id(projeto_dict['ceo_id'])
                
                query = f"SELECT * FROM Interacao WHERE projeto_id = {projeto_dict['id']} AND tipo = 'sinergia'"
                
                interacoes = self.interacao_model.execute_query(query)
                
                ceos = [ceo_principal.to_dict()]
                
                if interacoes:
                    for interacao in interacoes:
                        ceo = self.ceo_model.find_by_id(interacao.to_dict()['ceo_id'])
                        ceos.append(ceo.to_dict())
                
                projeto_dict['subtema_nome'] = subtema_dict['nome']
                projeto_dict['macrotema_nome'] = macrotema_dict['nome']
                projeto_dict['ceos'] = ceos
                projetos[i] = projeto_dict
                
            
            return projetos
        
    def post_sinergia(self, dados):
        # uma sinergia é uma interação do tipo 'sinergia'
        # que, incialmente, é criada com o status 'pendente'
        # e a data atual
        tipo = 'sinergia'
        status = 'pendente'

        # Obtém o objeto datetime atual
        now = datetime.now()
        
        # primeiro, valida se já não foi solicitada uma sinergia
        # entre o CEO e o projeto
        query = f"SELECT * FROM Interacao WHERE ceo_id = {dados['ceo_id']} AND projeto_id = {dados['projeto_id']} AND tipo = 'sinergia'"
        
        interacao_existente = self.interacao_model.execute_query(query)
        
        if interacao_existente:
            print('Já existe uma sinergia entre o CEO e o projeto')
            return None
        
        interacao = self.interacao_model.insert(ceo_id=dados['ceo_id'], projeto_id=dados['projeto_id'], tipo=tipo, estado=status, data=now)
        
        # busca informações do ceo dono do projeto
        projeto_alvo = self.projeto_model.find_by_id(dados['projeto_id']).to_dict()
        
        # remove data_criacao e estado do projeto
        projeto_alvo.pop('data_criacao')
        
        ceo_dono_projeto = self.ceo_model.find_by_id(projeto_alvo['ceo_id']).to_dict()
        
        ceo_origem = self.ceo_model.find_by_id(dados['ceo_id']).to_dict()

        dados = {
            'mensagem': 'Deseja realizar uma nova sinergia',
            'projeto': projeto_alvo,
            'ceo': ceo_origem
        }
        
        if interacao:
            self.enviar_notificacao('nova_sinergia', dados, sala=f'ceo_{ceo_dono_projeto["id"]}')
        
        return interacao
    
    def aceitar_sinergia(self, interacao_id):
        # busca a interação
        interacao = self.interacao_model.find_by_id(interacao_id)
        
        if interacao and interacao.to_dict()['tipo'] == 'sinergia' and interacao.to_dict()['estado'] == 'pendente':
            # atualiza o estado da interação para 'aceito'
            self.interacao_model.update(interacao_id, estado='aceito')
            
            # busca informações do projeto
            projeto = self.projeto_model.find_by_id(interacao.to_dict()['projeto_id']).to_dict()
            
            # remove data_criacao e estado do projeto
            projeto.pop('data_criacao')
            
            # busca informações do ceo dono do projeto
            ceo_dono_projeto = self.ceo_model.find_by_id(projeto['ceo_id']).to_dict()
            
            # busca informações do ceo que solicitou a sinergia
            ceo_origem = self.ceo_model.find_by_id(interacao.to_dict()['ceo_id']).to_dict()
            
            dados = {
                'mensagem': 'Sinergia aceita',
                'projeto': projeto,
                'ceo_origem': ceo_origem,
                'interacao_id': interacao_id,
                'estado': 'aceito',
                'ceo_dono_projeto': ceo_dono_projeto
            }
            
            #self.enviar_notificacao('sinergia_aceita', dados, sala=f'ceo_{ceo_dono_projeto["id"]}')
            
            return dados
        
        else:
            if interacao.to_dict()['estado'] == 'aceito' and interacao.to_dict()['tipo'] == 'sinergia':
                return {'mensagem': 'Sinergia já aceita'}
        
        return None
    
    def get_subtemas(self):
        subtemas = self.subtema_model.find_all()
        if subtemas:
            # Remove duplicados
            subtemas = list({subtema.id: subtema for subtema in subtemas}.values())

            # Extrai todos os IDs de macrotemas
            macrotema_ids = {subtema.macrotema_id for subtema in subtemas}

            # Obtém todos os macrotemas de uma vez
            macrotemas = {macrotema.id: macrotema.to_dict() for macrotema in self.macrotema_model.find_by_ids(list(macrotema_ids))}

            # Adiciona o nome do macrotema a cada subtema
            for i in range(len(subtemas)):
                subtemas[i] = subtemas[i].to_dict()
                macrotema_id = subtemas[i]['macrotema_id']
                if macrotema_id in macrotemas:
                    subtemas[i]['macrotema_nome'] = macrotemas[macrotema_id]['nome']

            return subtemas
        return None

    def get_projetos_macrotema(self, nome_macrotema, limit=10, offset=0):
        # Primeiro, obtenha todos os projetos que correspondem ao macrotema
        query_projetos = f"""
        SELECT Projeto.*
        FROM Projeto
        JOIN Subtema ON Projeto.subtema_id = Subtema.id
        JOIN Macrotema ON Subtema.macrotema_id = Macrotema.id
        WHERE Macrotema.nome = %s
        LIMIT {limit} OFFSET {offset}
        """
        
        projetos = self.projeto_model.execute_query(query_projetos, (nome_macrotema,))
        
        if projetos:
            subtemas_ids = {projeto.subtema_id for projeto in projetos}

            # Obtenha todos os subtemas de uma vez
            subtemas = {subtema.id: subtema.to_dict() for subtema in self.subtema_model.find_by_ids(list(subtemas_ids))}
            
            # Obtenha todos os macrotemas de uma vez
            macrotemas_ids = {subtema['macrotema_id'] for subtema in subtemas.values()}
            macrotemas = {macrotema.id: macrotema.to_dict() for macrotema in self.macrotema_model.find_by_ids(list(macrotemas_ids))}
            
            # Prepare a lista final de projetos com as informações necessárias
            projetos_finais = []
            for projeto in projetos:
                
                ceo_principal = self.ceo_model.find_by_id(projeto.to_dict()['ceo_id'])
                
                projeto_dict = projeto.to_dict()
                subtema = subtemas.get(projeto_dict['subtema_id'])
                macrotema = macrotemas.get(subtema['macrotema_id']) # type: ignore
                
                query = f"SELECT * FROM Interacao WHERE projeto_id = {projeto_dict['id']} AND tipo = 'sinergia'"
            
                interacoes = self.interacao_model.execute_query(query)
                
                ceos = [ceo_principal.to_dict()]
                
                if interacoes:
                    for interacao in interacoes:
                        ceo = self.ceo_model.find_by_id(interacao.to_dict()['ceo_id'])
                        ceos.append(ceo.to_dict())
                
                projeto_dict['subtema_nome'] = subtema['nome'] # type: ignore
                projeto_dict['macrotema_nome'] = macrotema['nome'] # type: ignore
                projeto_dict['macrotema_nome_completo'] = macrotema['nome_completo'] # type: ignore
                projeto_dict['ceos'] = ceos
                
                projetos_finais.append(projeto_dict)
                
            return projetos_finais
        
        return None

    def get_subtemas_por_macrotema(self, nome_macrotema):
        query = f"""
        SELECT Subtema.*
        FROM Subtema
        JOIN Macrotema ON Subtema.macrotema_id = Macrotema.id
        WHERE Macrotema.nome = %s
        """
        
        subtemas = self.subtema_model.execute_query(query, (nome_macrotema,))
        
        if subtemas:
            # Remove duplicados
            subtemas = list({subtema.id: subtema for subtema in subtemas}.values())
            
            return [subtema.to_dict() for subtema in subtemas]
        
        return None
    
    def get_macrotemas(self):
        macrotemas = self.macrotema_model.find_all()
        if macrotemas:
            # deixa somente macrotemas únicos com base no nome
            macrotemas = list({macrotema.nome: macrotema for macrotema in macrotemas}.values())
            return macrotemas
        return None
    
    def get_macrotemas_por_ceo(self, ceo_id):
        query = f"SELECT * FROM Projeto WHERE ceo_id = {ceo_id}"
        
        projetos = self.projeto_model.execute_query(query)
        
        query = f"SELECT * FROM Interacao WHERE ceo_id = {ceo_id} AND tipo = 'sinergia'"
        
        interacoes = self.interacao_model.execute_query(query)
        
        if interacoes:
            for interacao in interacoes:
                projeto = self.projeto_model.find_by_id(interacao.to_dict()['projeto_id'])
                projetos.append(projeto)
                
        result = {}
                
        if projetos:
            subtemas_ids = {projeto.to_dict()['subtema_id'] for projeto in projetos}
            
            subtemas = {subtema.id: subtema.to_dict() for subtema in self.subtema_model.find_by_ids(list(subtemas_ids))}
            
            result['subtemas'] = list(subtemas.values())
            
            macrotemas_ids = {subtema['macrotema_id'] for subtema in subtemas.values()}
            
            macrotemas = {macrotema.id: macrotema.to_dict() for macrotema in self.macrotema_model.find_by_ids(list(macrotemas_ids))}
            
            macrotemas = list({macrotema['nome']: macrotema for macrotema in macrotemas.values()}.values())
            
            result['macrotemas'] = macrotemas
            
            return result
        
        return None
    
    def get_projetos_por_busca(self, termo):
        #  busca tanto pelo nome do projeto quanto pelo nome do CEO
        # bem como pelo nome do subtema e do macrotema
        query = f"""
        SELECT Projeto.*
        FROM Projeto
        JOIN CEO ON Projeto.ceo_id = CEO.id
        JOIN Subtema ON Projeto.subtema_id = Subtema.id
        JOIN Macrotema ON Subtema.macrotema_id = Macrotema.id
        WHERE Projeto.nome LIKE %s
        OR Projeto.descricao LIKE %s
        OR CEO.nome LIKE %s
        OR Subtema.nome LIKE %s
        OR Macrotema.nome LIKE %s
        """
        
        projetos = self.projeto_model.execute_query(query, (f'%{termo}%', f'%{termo}%', f'%{termo}%', f'%{termo}%', f'%{termo}%'))
        
        if projetos:
            subtemas_ids = {projeto.subtema_id for projeto in projetos}
            
            subtemas = {subtema.id: subtema.to_dict() for subtema in self.subtema_model.find_by_ids(list(subtemas_ids))}
            
            macrotemas_ids = {subtema['macrotema_id'] for subtema in subtemas.values()}
            
            macrotemas = {macrotema.id: macrotema.to_dict() for macrotema in self.macrotema_model.find_by_ids(list(macrotemas_ids))}
            
            projetos_finais = [] 
            
            for projeto in projetos:
                ceo_principal = self.ceo_model.find_by_id(projeto.to_dict()['ceo_id'])
                
                projeto_dict = projeto.to_dict()
                subtema = subtemas.get(projeto_dict['subtema_id'])
                macrotema = macrotemas.get(subtema['macrotema_id']) # type: ignore
                
                query = f"SELECT * FROM Interacao WHERE projeto_id = {projeto_dict['id']} AND tipo = 'sinergia'"
                
                interacoes = self.interacao_model.execute_query(query)
                
                ceos = [ceo_principal.to_dict()]
                
                if interacoes:
                    for interacao in interacoes:
                        ceo = self.ceo_model.find_by_id(interacao.to_dict()['ceo_id'])
                        ceos.append(ceo.to_dict())
                        
                projeto_dict['subtema_nome'] = subtema['nome'] # type: ignore
                projeto_dict['macrotema_nome'] = macrotema['nome'] # type: ignore
                projeto_dict['ceos'] = ceos
                
                projetos_finais.append(projeto_dict)
                
            return projetos_finais

    def get_projetos_inativos(self):
        query = f"SELECT * FROM Projeto WHERE estado = 'inativo'"
        projetos = self.projeto_model.execute_query(query)

        if projetos:
            # adiciona os subtemas e macrotemas aos projetos
            for i in range(len(projetos)):
                projeto_dict = projetos[i].to_dict()
                subtema = self.subtema_model.find_by_id(projeto_dict['subtema_id'])
                subtema_dict = subtema.to_dict()
                macrotema = self.macrotema_model.find_by_id(subtema_dict['macrotema_id'])
                macrotema_dict = macrotema.to_dict()
                ceo_principal = self.ceo_model.find_by_id(projeto_dict['ceo_id'])
                
                query = f"SELECT * FROM Interacao WHERE projeto_id = {projeto_dict['id']} AND tipo = 'sinergia'"
                
                interacoes = self.interacao_model.execute_query(query)
                
                ceos = [ceo_principal.to_dict()]
                
                if interacoes:
                    for interacao in interacoes:
                        ceo = self.ceo_model.find_by_id(interacao.to_dict()['ceo_id'])
                        ceos.append(ceo.to_dict())
                
                projeto_dict['subtema_nome'] = subtema_dict['nome']
                projeto_dict['macrotema_nome'] = macrotema_dict['nome']
                projeto_dict['ceos'] = ceos
                projetos[i] = projeto_dict
                
        return projetos

    def get_dashboard_projetos_macrotema(self):
        query = """
        SELECT COUNT(Projeto.id) AS count, Macrotema.nome 
        FROM Macrotema 
        INNER JOIN Subtema ON Subtema.macrotema_id = Macrotema.id 
        INNER JOIN Projeto ON Projeto.subtema_id = Subtema.id 
        GROUP BY Macrotema.nome;
        """
        result = self.projeto_model.execute_query(query, count_query=True)
        if result:
            resultado_json = {row[1]: row[0] for row in result}
            return resultado_json
        return {}

    def get_dashboard_sinergias(self):
        query = "SELECT COUNT(*) as sinergia_count FROM Interacao WHERE tipo = 'sinergia'"
        result = self.projeto_model.execute_query(query, count_query=True)
        if result:
            # Acessa o valor da contagem no resultado
            sinergia_count = result[0][0] if result else 0  # result[0][0] acessa o valor da contagem no primeiro registro
            return sinergia_count
        return 0  # Retorna 0 caso não haja resultado
    
    def get_dashboard_projetos(self):
        query = " SELECT COUNT(Projeto.id) AS count FROM Projeto"
        result = self.projeto_model.execute_query(query, count_query=True)
        if result:
            # Acessa o valor da contagem no resultado
            proejtos_count = result[0][0] if result else 0  # result[0][0] acessa o valor da contagem no primeiro registro
            return proejtos_count
        return 0  # Retorna 0 caso não haja resultado

    def get_dashboard_sinergias_macrotema(self):
        query = """
            SELECT Macrotema.nome, COUNT(Interacao.id) AS count 
            FROM Interacao
            INNER JOIN Projeto ON Interacao.projeto_id = Projeto.id
            INNER JOIN Subtema ON Projeto.subtema_id = Subtema.id
            INNER JOIN Macrotema ON Subtema.macrotema_id = Macrotema.id
            WHERE Interacao.tipo = 'sinergia'
            GROUP BY Macrotema.nome;
        """
        result = self.projeto_model.execute_query(query, count_query=True)
        if result:
            resultado_json = {row[0]: row[1] for row in result}
            return resultado_json
        return {}
    
    # Função auxiliar para converter chaves de date para string
    def convert_date_keys_to_str(self, d):
        if isinstance(d, dict):
            return {str(k) if isinstance(k, date) else k: self.convert_date_keys_to_str(v) for k, v in d.items()}
        elif isinstance(d, list):
            return [self.convert_date_keys_to_str(i) for i in d]
        else:
            return d
    
    def get_dashboard_sinergias_tempo(self, filtro):

        match filtro:
            case 'all_time':
                query = """SELECT DATE(data) AS dia, COUNT(*) AS quantidade
                            FROM Interacao
                            WHERE tipo = 'sinergia'
                            GROUP BY DATE(data)
                            ORDER BY dia;"""
            case 'last_month':
                query = """SELECT DATE(data) AS dia, COUNT(*) AS quantidade
                            FROM Interacao
                            WHERE data >= DATE_TRUNC('month', CURRENT_DATE)
                            AND data < DATE_TRUNC('month', CURRENT_DATE) + INTERVAL '1 month'
                            AND tipo = 'sinergia'
                            GROUP BY DATE(data)
                            ORDER BY dia;"""
            case 'last_week':
                query = """SELECT DATE(data) AS dia, COUNT(*) AS quantidade
                            FROM Interacao
                            WHERE data >= DATE_TRUNC('week', CURRENT_DATE) - INTERVAL '1 week'
                            AND data < DATE_TRUNC('week', CURRENT_DATE)
                            AND tipo = 'sinergia'
                            GROUP BY DATE(data)
                            ORDER BY dia;"""
            case _:
                query = None
                
        if query:
            result = self.projeto_model.execute_query(query, count_query=True)
            if result:
                resultado_json = {row[0]: row[1] for row in result}
                resultado_json = self.convert_date_keys_to_str(resultado_json)  # Convertendo chaves de date para string
                return resultado_json
            return {}

    def post_curtida(self, dados):
        # uma sinergia é uma interação do tipo 'curtida'
        # e a data atual
        tipo = 'curtida'


        # Obtém o objeto datetime atual
        now = datetime.now()
       
        # primeiro, valida se já não foi solicitada uma sinergia
        # entre o CEO e o projeto
        query = f"SELECT * FROM Interacao WHERE ceo_id = {dados['ceo_id']} AND projeto_id = {dados['projeto_id']} AND tipo = 'curtida'"
       
        interacao_existente = self.interacao_model.execute_query(query)
       
        if interacao_existente:
            interacao_existente = interacao_existente[0].to_dict()


            if interacao_existente["avaliacao"] == 5:
                self.interacao_model.update(interacao_existente["id"], avaliacao=1)


                return interacao_existente["id"]
            else:
                self.interacao_model.update(interacao_existente["id"], avaliacao=5)


                return interacao_existente["id"]
       


        interacao = self.interacao_model.insert(ceo_id=dados['ceo_id'], projeto_id=dados['projeto_id'], tipo=tipo, avaliacao=5, data=now)
       
        return interacao
   
    def post_salvos(self, dados):
        # uma sinergia é uma interação do tipo 'curtida'
        # e a data atual
        tipo = 'salvos'


        # Obtém o objeto datetime atual
        now = datetime.now()
       
        # primeiro, valida se já não foi solicitada uma sinergia
        # entre o CEO e o projeto
        query = f"SELECT * FROM Interacao WHERE ceo_id = {dados['ceo_id']} AND projeto_id = {dados['projeto_id']} AND tipo = 'salvos'"
       
        interacao_existente = self.interacao_model.execute_query(query)
       
        if interacao_existente:
            interacao_existente = interacao_existente[0].to_dict()


            if interacao_existente["avaliacao"] == 5:
                self.interacao_model.update(interacao_existente["id"], avaliacao=1)


                return interacao_existente["id"]
            else:
                self.interacao_model.update(interacao_existente["id"], avaliacao=5)


                return interacao_existente["id"]
       
        print("AAAAAAAAAAAAAAAAAAAAAAAAA")


        interacao = self.interacao_model.insert(ceo_id=dados['ceo_id'], projeto_id=dados['projeto_id'], tipo=tipo, avaliacao=5, data=now)
       
        return interacao
   
    def get_curtidos(self, ceo_id):
        print(ceo_id)
        query = f"""
        SELECT * FROM Projeto
        JOIN Interacao on Projeto.id = Interacao.projeto_id
        WHERE Interacao.tipo = 'curtida' AND Interacao.ceo_id = {ceo_id};
        """
       
        projetos = self.projeto_model.execute_query(query)


        print(projetos[0].to_dict())
       
        if projetos:
            # adiciona os subtemas e macrotemas aos projetos
            for i in range(len(projetos)):
                projeto_dict = projetos[i].to_dict()
                subtema = self.subtema_model.find_by_id(projeto_dict['subtema_id'])
                subtema_dict = subtema.to_dict()
                macrotema = self.macrotema_model.find_by_id(subtema_dict['macrotema_id'])
                macrotema_dict = macrotema.to_dict()
                ceo_principal = self.ceo_model.find_by_id(projeto_dict['ceo_id'])
               
                query = f"SELECT * FROM Interacao WHERE projeto_id = {projeto_dict['id']} AND tipo = 'curtida'"
               
                interacoes = self.interacao_model.execute_query(query)
               
                ceos = [ceo_principal.to_dict()]
               
                if interacoes:
                    for interacao in interacoes:
                        ceo = self.ceo_model.find_by_id(interacao.to_dict()['ceo_id'])
                        ceos.append(ceo.to_dict())
               
                projeto_dict['subtema_nome'] = subtema_dict['nome']
                projeto_dict['macrotema_nome'] = macrotema_dict['nome']
                projeto_dict['ceos'] = ceos
                projetos[i] = projeto_dict
               
           
            return projetos
       
    def get_salvos(self, ceo_id):
        print(ceo_id)
        query = f"""
        SELECT * FROM Projeto
        JOIN Interacao on Projeto.id = Interacao.projeto_id
        WHERE Interacao.tipo = 'salvos' AND Interacao.ceo_id = {ceo_id};
        """
       
        projetos = self.projeto_model.execute_query(query)


        print(projetos[0].to_dict())
       
        if projetos:
            # adiciona os subtemas e macrotemas aos projetos
            for i in range(len(projetos)):
                projeto_dict = projetos[i].to_dict()
                subtema = self.subtema_model.find_by_id(projeto_dict['subtema_id'])
                subtema_dict = subtema.to_dict()
                macrotema = self.macrotema_model.find_by_id(subtema_dict['macrotema_id'])
                macrotema_dict = macrotema.to_dict()
                ceo_principal = self.ceo_model.find_by_id(projeto_dict['ceo_id'])
               
                query = f"SELECT * FROM Interacao WHERE projeto_id = {projeto_dict['id']} AND tipo = 'salvos'"
               
                interacoes = self.interacao_model.execute_query(query)
               
                ceos = [ceo_principal.to_dict()]
               
                if interacoes:
                    for interacao in interacoes:
                        ceo = self.ceo_model.find_by_id(interacao.to_dict()['ceo_id'])
                        ceos.append(ceo.to_dict())
               
                projeto_dict['subtema_nome'] = subtema_dict['nome']
                projeto_dict['macrotema_nome'] = macrotema_dict['nome']
                projeto_dict['ceos'] = ceos
                projetos[i] = projeto_dict
               
           
            return projetos
        
        
    def post_atualizacao(self, dados):
        # Obtém o objeto datetime atual
        atualizacao = self.atualizacao_model.insert(projeto_id=dados['projeto_id'], descricao=dados['descricao'], data=dados['data'])
        return atualizacao