from flask import Blueprint, jsonify, request
from marshmallow import Schema, fields, ValidationError
from backend.projetos.services import ProjetoService
from backend.projetos.models import ProjetoModel, SubtemaModel, MacrotemaModel, InteracaoModel, AtualizaoModel
from backend.ceos.models import CeoModel
from flasgger import swag_from
from backend.common.traceability import Trace

projeto_blueprint = Blueprint('projeto', __name__)

projeto_service = ProjetoService(ProjetoModel, CeoModel, SubtemaModel, MacrotemaModel, InteracaoModel, AtualizaoModel)

# Classe do Marshmallow para a validação de dados de entrada - Criação de projetos
class PostProjetoSchema(Schema):
    ceo_id = fields.Int(required=True)
    subtema_id = fields.Int(required=True)
    nome = fields.Str(required=True)
    descricao = fields.Str(required=True)

# Classe do Marshmallow para a validação de dados de entrada - Atualização de projetos
class PutProjetoSchema(Schema):
    subtema_id = fields.Int(required=False)
    nome = fields.Str(required=False)
    descricao = fields.Str(required=False)
    estado = fields.Str(required=False)

# Classe do Marshmallow para a validação de dados de entrada - Criação de sinergia
class PostSinergiaSchema(Schema):
    ceo_id = fields.Int(required=True)
    projeto_id = fields.Int(required=True)

# Classe do Marshmallow para a validação de dados de entrada - Criação de atualizações
class PostAtualizacaoSchema(Schema):
    projeto_id = fields.Int(required=True)
    descricao = fields.Str(required=False)
    data = fields.Date(required=False)


# Retorna todos os projetos
@projeto_blueprint.route('/projetos/', methods=['GET'])
@Trace.REQ(['RF-023'])
@swag_from({
    'tags': ['Projetos'],
    'summary': 'Retorna todos os projetos',
    'operationId': 'get_projetos',
    'responses': {
        200: {
            'description': 'Lista de projetos',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'ceo_id': {'type': 'integer'},
                        'subtema_id': {'type': 'integer'},
                        'nome': {'type': 'string'},
                        'descricao': {'type': 'string'},
                        'data_criacao': {'type': 'string', 'format': 'date-time'},
                        'estado': {'type': 'string'}
                    }
                }
            }
        },
        404: {
            'description': 'Projetos não encontrados'
        }
    }
})
def get_projetos():
    projetos = projeto_service.get_projetos()
    if projetos:
        return ([projeto.to_dict() for projeto in projetos]), 200
    return jsonify({'erro': 'Projetos não encontrados'}), 404


# Retorna um projeto específico
@projeto_blueprint.route('/projetos/<int:projeto_id>', methods=['GET'])
@Trace.REQ(['RF-021', 'RF-024'])
@swag_from({
    'tags': ['Projetos'],
    'summary': 'Retorna um projeto específico com base no ID',
    'operationId': 'get_projeto',
    'parameters': [
        {
            'name': 'projeto_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do projeto'
        }
    ],
    'responses': {
        200: {
            'description': 'Detalhes do projeto',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'ceo_id': {'type': 'integer'},
                    'subtema_id': {'type': 'integer'},
                    'nome': {'type': 'string'},
                    'descricao': {'type': 'string'},
                    'data_criacao': {'type': 'string', 'format': 'date-time'},
                    'estado': {'type': 'string'},
                    'macrotema_nome': {'type': 'string'},
                    'subtema_nome': {'type': 'string'},
                    'ceos': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'biografia': {'type': 'string'},
                                'cargo': {'type': 'string'},
                                'celular': {'type': 'string'},
                                'email_contato': {'type': 'string'},
                                'empresa_link': {'type': 'string'},
                                'empresa_nome': {'type': 'string'},
                                'estado': {'type': 'string'},
                                'foto': {'type': 'string'},
                                'id': {'type': 'integer'},
                                'linkedin': {'type': 'string'},
                                'nome': {'type': 'string'},
                            }
                        }
                    }
                }
            }
        },
        404: {
            'description': 'Projeto não encontrado'
        }
    }
})
def get_projeto(projeto_id):
    projeto = projeto_service.get_projeto(projeto_id)
    if projeto:
        print('projeto: ', projeto)
        return jsonify(projeto), 200
    return jsonify({'erro': 'Projeto não encontrado'}), 404


# Cria um projeto
@projeto_blueprint.route('/projetos/', methods=['POST'])
@Trace.REQ(['RF-006'])
@swag_from({
    'tags': ['Projetos'],
    'summary': 'Cria um novo projeto',
    'operationId': 'post_projeto',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'ceo_id': {'type': 'integer', 'required': True},
                    'subtema_id': {'type': 'integer', 'required': True},
                    'nome': {'type': 'string', 'required': True},
                    'descricao': {'type': 'string', 'required': True}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Projeto criado',
            'schema': {
                'type': 'integer'
            }
        },
        400: {
            'description': 'Erro na criação do projeto'
        }
    }
})
def post_projeto():
    dados = request.json
    
    try:
        projeto_data = PostProjetoSchema().load(dados) # type: ignore
    except ValidationError as err:
        return jsonify({'erro': err.messages}), 400
    
    projetoId = projeto_service.post_projeto(projeto_data)
    
    if projetoId:
        return jsonify(projetoId), 200
    
    return jsonify({'erro': 'Erro ao criar o projeto'}), 400


# Atualiza um projeto
@projeto_blueprint.route('/projetos/<int:projeto_id>', methods=['PUT'])
@Trace.REQ(['RF-007', 'RF-021'])
@swag_from({
    'tags': ['Projetos'],
    'summary': 'Atualiza um projeto específico com base no ID',
    'operationId': 'put_projeto',
    'parameters': [
        {
            'name': 'projeto_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do projeto'
        },
        {
            'name': 'body',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'subtema_id': {'type': 'integer'},
                    'nome': {'type': 'string'},
                    'descricao': {'type': 'string'},
                    'estado': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Projeto atualizado',
            'schema': {
                'type': 'integer'
            }
        },
        400: {
            'description': 'Erro na atualização do projeto'
        }
    }
})
def put_projeto(projeto_id):
    dados = request.json
    
    try:
        projeto_data = PutProjetoSchema().load(dados) # type: ignore
    except ValidationError as err:
        return jsonify({'erro': err.messages}), 400
    
    projetoId = projeto_service.put_projeto(projeto_id, projeto_data)
    
    if projetoId:
        return jsonify(projetoId), 200
    
    return jsonify({'erro': 'Erro ao atualizar o projeto'}), 400


# Deleta um projeto
@projeto_blueprint.route('/projetos/<int:projeto_id>', methods=['DELETE'])
@Trace.REQ(['RF-008'])
@swag_from({
    'tags': ['Projetos'],
    'summary': 'Deleta um projeto específico com base no ID',
    'operationId': 'delete_projeto',
    'parameters': [
        {
            'name': 'projeto_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do projeto'
        }
    ],
    'responses': {
        200: {
            'description': 'Projeto apagado',
            'schema': {
                'type': 'integer'
            }
        },
        400: {
            'description': 'Erro ao apagar o projeto'
        }
    }
})
def delete_projeto(projeto_id): 
    projetoId = projeto_service.delete_projeto(projeto_id)
    
    if projetoId:
        return jsonify(projetoId), 200
    
    return jsonify({'erro': 'Erro ao apagar o projeto'}), 400


# Pega projetos com base em um ceo_id
@projeto_blueprint.route('/projetos/ceo/<int:ceo_id>', methods=['GET'])
@Trace.REQ(['RF-015'])
@swag_from({
    'tags': ['Projetos'],
    'summary': 'Retorna projetos com base no ID do CEO',
    'operationId': 'get_projetos_ceo',
    'parameters': [
        {
            'name': 'ceo_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do CEO'
        }
    ],
    'responses': {
        200: {
            'description': 'Lista de projetos',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'ceo_id': {'type': 'integer'},
                        'subtema_id': {'type': 'integer'},
                        'nome': {'type': 'string'},
                        'descricao': {'type': 'string'},
                        'data_criacao': {'type': 'string', 'format': 'date-time'},
                        'estado': {'type': 'string'},
                        'macrotema_nome': {'type': 'string'},
                        'subtema_nome': {'type': 'string'},
                        'ceos': {
                            'type': 'array',
                            'items': {
                                'type': 'object',
                                'properties': {
                                    'biografia': {'type': 'string'},
                                    'cargo': {'type': 'string'},
                                    'celular': {'type': 'string'},
                                    'email_contato': {'type': 'string'},
                                    'empresa_link': {'type': 'string'},
                                    'empresa_nome': {'type': 'string'},
                                    'estado': {'type': 'string'},
                                    'foto': {'type': 'string'},
                                    'id': {'type': 'integer'},
                                    'linkedin': {'type': 'string'},
                                    'nome': {'type': 'string'},
                                }
                            }
                        }
                    }
                }
            }
        },
        404: {
            'description': 'Projetos não encontrados'
        }
    }
})
def get_projetos_ceo(ceo_id):
    projetos = projeto_service.get_projetos_ceo(ceo_id)
    if projetos:
        return ([projeto for projeto in projetos]), 200
    return jsonify({'erro': 'Projetos não encontrados'}), 404


# Cria sinergia entre projetos
@projeto_blueprint.route('/projetos/sinergia/', methods=['POST'])
@Trace.REQ(['RF-010'])
@swag_from({
    'tags': ['Projetos'],
    'summary': 'Cria sinergia entre ceo e projetos',
    'operationId': 'post_sinergia',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'ceo_id': {'type': 'integer', 'required': True},
                    'projeto_id': {'type': 'integer', 'required': True}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Sinergia criada',
            'schema': {
                'type': 'integer'
            }
        },
        400: {
            'description': 'Erro na criação da sinergia'
        }
    }
})
def post_sinergia():
    dados = request.json
    
    try:
        sinergia_data = PostSinergiaSchema().load(dados) # type: ignore
    except ValidationError as err:
        return jsonify({'erro': err.messages}), 400
    
    sinergiaId = projeto_service.post_sinergia(sinergia_data)
    
    if sinergiaId:
        return jsonify(sinergiaId), 200
    
    return jsonify({'erro': 'Erro ao criar a sinergia'}), 400


@projeto_blueprint.route('/projetos/aceitar_sinergia/', methods=['POST'])
@Trace.REQ(['RF-012', 'RF-014'])
@swag_from({
    'tags': ['Projetos'],
    'summary': 'Aceita sinergia entre ceo e projetos',
    'operationId': 'post_aceitar_sinergia',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'interacao_id': {'type': 'integer', 'required': True}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Sinergia aceita',
            'schema': {
                'type': 'integer'
            }
        },
        400: {
            'description': 'Erro na aceitação da sinergia'
        }
    }
})
def post_aceitar_sinergia():
    # pega o número da interaçã id:
    dados = request.json
    interacao_id = None
    
    try:
        interacao_id = dados['interacao_id'] # type: ignore
        
        # aceita a sinergia
        sinergiaId = projeto_service.aceitar_sinergia(interacao_id)
        
        return jsonify(sinergiaId), 200
        
    except ValidationError as err:
        return jsonify({'erro': err.messages}), 400

# Lista projetos com base em um nome de macrotema (passado como query string)
@projeto_blueprint.route('/projetos/macrotema', methods=['GET'])
@Trace.REQ(['RF-017'])
@swag_from({
    'tags': ['Projetos'],
    'summary': 'Retorna projetos com base no nome do macrotema',
    'operationId': 'get_projetos_macrotema',
    'parameters': [
        {
            'name': 'nome',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': 'Nome do macrotema'
        },
        {
            'name': 'limit',
            'in': 'query',
            'type': 'integer',
            'required': False,
            'description': 'Limite de projetos a serem retornados'
        },
        {
            'name': 'offset',
            'in': 'query',
            'type': 'integer',
            'required': False,
            'description': 'Offset de projetos a serem retornados'
        }
    ],
    'responses': {
        200: {
            'description': 'Lista de projetos',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'ceo_id': {'type': 'integer'},
                        'subtema_id': {'type': 'integer'},
                        'nome': {'type': 'string'},
                        'descricao': {'type': 'string'},
                        'data_criacao': {'type': 'string', 'format': 'date-time'},
                        'estado': {'type': 'string'},
                        'macrotema_nome': {'type': 'string'},
                        'subtema_nome': {'type': 'string'},
                        'ceos': {
                            'type': 'array',
                            'items': {
                                'type': 'object',
                                'properties': {
                                    'biografia': {'type': 'string'},
                                    'cargo': {'type': 'string'},
                                    'celular': {'type': 'string'},
                                    'email_contato': {'type': 'string'},
                                    'empresa_link': {'type': 'string'},
                                    'empresa_nome': {'type': 'string'},
                                    'estado': {'type': 'string'},
                                    'foto': {'type': 'string'},
                                    'id': {'type': 'integer'},
                                    'linkedin': {'type': 'string'},
                                    'nome': {'type': 'string'},
                                }
                            }
                        }
                    }
                }
            }
        },
        404: {
            'description': 'Projetos não encontrados'
        }
    }
})
def get_projetos_macrotema():
    macrotema = request.args.get('nome')
    limit = int(request.args.get('limit') or 10)
    offset = int(request.args.get('offset') or 0)
    if macrotema:
        projetos = projeto_service.get_projetos_macrotema(macrotema, limit, offset)
        if projetos:
            return jsonify(projetos), 200
    return jsonify({'erro': 'Projetos não encontrados'}), 404


# Lista os macrotemas
@projeto_blueprint.route('/projetos/macrotemas', methods=['GET'])
@Trace.REQ(['RF-027'])
@swag_from({
    'tags': ['Projetos'],
    'summary': 'Retorna todos os macrotemas do banco de dados',
    'operationId': 'get_macrotemas',
    'responses': {
        200: {
            'description': 'Lista de macrotemas',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'nome': {'type': 'string'},
                        'descricao': {'type': 'string'}
                    }
                }
            }
        },
        404: {
            'description': 'Macrotemas não encontrados'
        }
    }
})
def get_macrotemas():
    macrotemas = projeto_service.get_macrotemas()
    if macrotemas:
        return jsonify([macrotema.to_dict() for macrotema in macrotemas]), 200
    return jsonify({'erro': 'Macrotemas não encontrados'}), 404


# Lista os subtemas de um determinado nome de macrotema (passado como query string)
@projeto_blueprint.route('/projetos/subtemas', methods=['GET'])
@Trace.REQ(['RF-028'])
@swag_from({
    'tags': ['Projetos'],
    'summary': 'Retorna subtemas com base no nome do macrotema',
    'operationId': 'get_subtemas_macrotema',
    'parameters': [
        {
            'name': 'macrotema',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': 'Nome do macrotema'
        }
    ],
    'responses': {
        200: {
            'description': 'Lista de subtemas',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'nome': {'type': 'string'},
                        'descricao': {'type': 'string'},
                        'macrotema_id': {'type': 'integer'}
                    }
                }
            }
        },
        404: {
            'description': 'Subtemas não encontrados'
        }
    }
})
def get_subtemas_macrotema():
    macrotema = request.args.get('macrotema')
    if macrotema:
        subtemas = projeto_service.get_subtemas_por_macrotema(macrotema)
        if subtemas:
            return jsonify(subtemas), 200
    return jsonify({'erro': 'Subtemas não encontrados'}), 404


# Lista os macrotemas de um determinado ceo_id
@projeto_blueprint.route('/projetos/macrotemas/ceo/<int:ceo_id>', methods=['GET'])
@Trace.REQ(['RF-027'])
@swag_from({
    'tags': ['Projetos'],
    'summary': 'Retorna macrotemas com base no ID do CEO',
    'operationId': 'get_macrotemas_ceo',
    'parameters': [
        {
            'name': 'ceo_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do CEO'
        }
    ],
    'responses': {
        200: {
            'description': 'Lista de macrotemas',
            'schema': {
                'type': 'object',
                'properties': {
                    'macrotemas': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'integer'},
                                'nome': {'type': 'string'},
                                'descricao': {'type': 'string'}
                            }
                        }
                    },
                    'subtemas': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'integer'},
                                'nome': {'type': 'string'},
                                'descricao': {'type': 'string'},
                                'macrotema_id': {'type': 'integer'}
                            }
                        }
                    }
                }
            }
        },
        404: {
            'description': 'Macrotemas não encontrados'
        }
    }
})
def get_macrotemas_ceo(ceo_id):
    macrotemas = projeto_service.get_macrotemas_por_ceo(ceo_id)
    if macrotemas:
        return jsonify(macrotemas), 200
    return jsonify({'erro': 'Macrotemas não encontrados'}), 404


# Busca projetos com base em um termo de busca (passado como query string)
@projeto_blueprint.route('/projetos/busca', methods=['GET'])
@Trace.REQ(['RF-017', 'RF-029'])
@swag_from({
    'tags': ['Projetos'],
    'summary': 'Busca projetos com base em um termo de busca',
    'operationId': 'get_projetos_busca',
    'parameters': [
        {
            'name': 'termo',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': 'Termo de busca'
        }
    ],
    'responses': {
        200: {
            'description': 'Lista de projetos',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'ceo_id': {'type': 'integer'},
                        'subtema_id': {'type': 'integer'},
                        'nome': {'type': 'string'},
                        'descricao': {'type': 'string'},
                        'data_criacao': {'type': 'string', 'format': 'date-time'},
                        'estado': {'type': 'string'},
                        'macrotema_nome': {'type': 'string'},
                        'subtema_nome': {'type': 'string'},
                        'ceos': {
                            'type': 'array',
                            'items': {
                                'type': 'object',
                                'properties': {
                                    'biografia': {'type': 'string'},
                                    'cargo': {'type': 'string'},
                                    'celular': {'type': 'string'},
                                    'email_contato': {'type': 'string'},
                                    'empresa_link': {'type': 'string'},
                                    'empresa_nome': {'type': 'string'},
                                    'estado': {'type': 'string'},
                                    'foto': {'type': 'string'},
                                    'id': {'type': 'integer'},
                                    'linkedin': {'type': 'string'},
                                    'nome': {'type': 'string'},
                                }
                            }
                        }
                    }
                }
            }
        },
        404: {
            'description': 'Projetos não encontrados'
        }
    }
})
def get_projetos_busca():
    termo = request.args.get('termo')
    if termo:
        projetos = projeto_service.get_projetos_por_busca(termo)
        if projetos:
            return jsonify(projetos), 200
    return jsonify({'erro': 'Projetos não encontrados'}), 404


# Busca para o dashboard - Quantidade de Projetos Inativos
@projeto_blueprint.route('/projetos/inativos', methods=['GET'])
@swag_from({
    'tags': ['Projetos'],
    'summary': 'Retorna a lista de projetos inativos',
    'operationId': 'get_projetos_inativos',
    'responses': {
        200: {
            'description': 'Lista de projetos inativos retornada com sucesso',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'ceo_id': {'type': 'integer', 'example': 1002},
                                'ceos': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'biografia': {'type': 'string', 'example': "Menino travesso! Ama um burburinho!!"},
                                            'cargo': {'type': 'string', 'example': "CEEO"},
                                            'celular': {'type': 'string', 'example': "00000000000"},
                                            'email_contato': {'type': 'string', 'example': "contato@empresa.com"},
                                            'empresa_link': {'type': 'string', 'example': "https://www.exemplo.com"},
                                            'empresa_nome': {'type': 'string', 'example': "LinkedIn"},
                                            'estado': {'type': 'string', 'example': "ativo"},
                                            'foto': {'type': 'string', 'example': "https://api.dicebear.com/8.x/miniavs/svg?seed=Annie"},
                                            'id': {'type': 'integer', 'example': 1002},
                                            'linkedin': {'type': 'string', 'example': "https://www.linkedin.com/in/desconhecido/"},
                                            'nome': {'type': 'string', 'example': "Heitor Elias"}
                                        }
                                    }
                                },
                                'data_criacao': {'type': 'string', 'format': 'date-time', 'example': "Thu, 13 Jun 2024 20:43:08 GMT"},
                                'descricao': {'type': 'string', 'example': "Sim"},
                                'estado': {'type': 'string', 'example': "inativo"},
                                'id': {'type': 'integer', 'example': 1468},
                                'macrotema_nome': {'type': 'string', 'example': "bem-estar"},
                                'nome': {'type': 'string', 'example': "Oi"},
                                'subtema_id': {'type': 'integer', 'example': 1},
                                'subtema_nome': {'type': 'string', 'example': "Psicologia"}
                            }
                        }
                    }
                }
            }
        },
        404: {
            'description': 'Projetos inativos não encontrados',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'erro': {'type': 'string', 'example': 'Projetos inativos não encontrados'}
                        }
                    }
                }
            }
        }
    }
})
def get_projetos_inativos():
    projetos = projeto_service.get_projetos_inativos()
    if projetos:
        return jsonify(projetos), 200
    return jsonify({'erro': 'Projetos inativos não encontrados'}), 404


# Busca para o dashboard - Quantidade de Projetos por macrotema
@projeto_blueprint.route('/projetos/projetosxmacrotema', methods=['GET'])
@swag_from({
    'tags': ['Projetos'],
    'summary': 'Retorna a quantidade de projetos por macrotema',
    'operationId': 'get_dashboard_projetos_macrotema',
    'responses': {
        200: {
            'description': 'Quantidade de projetos por macrotema retornada com sucesso',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'additionalProperties': {
                            'type': 'integer',
                            'example': 159
                        },
                        'examples': {
                            'response': {
                                'value': {
                                    'bem-estar': 159,
                                    'conservação': 224,
                                    'diversidade': 219,
                                    'integridade': 17,
                                    'produtividade': 756,
                                    'redução': 75
                                }
                            }
                        }
                    }
                }
            }
        },
        404: {
            'description': 'Projetos por macrotemas não encontrados',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'erro': {'type': 'string', 'example': 'Projetos por macrotemas não encontrados'}
                        }
                    }
                }
            }
        }
    }
})
def get_dashboard_projetos_macrotema():
    projetos = projeto_service.get_dashboard_projetos_macrotema()
    if projetos:
        return jsonify(projetos), 200
    return jsonify({'erro': 'Projetos por macrotemas não encontrados'}), 404


# Busca para o dashboard - Quantidade de sinergias
@projeto_blueprint.route('/projetos/sinergias', methods=['GET'])
@swag_from({
    'tags': ['Projetos'],
    'summary': 'Retorna a quantidade de sinergias',
    'operationId': 'get_dashboard_sinergias',
    'responses': {
        200: {
            'description': 'Quantidade de sinergias retornada com sucesso',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'sinergias': {
                                'type': 'integer',
                                'example': 30
                            }
                        }
                    }
                }
            }
        },
        404: {
            'description': 'Quantidade de sinergias não encontrada',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'erro': {
                                'type': 'string',
                                'example': 'Quantidade de sinergias não encontrados'
                            }
                        }
                    }
                }
            }
        }
    }
})
def get_dashboard_sinergias():
    sinergia_count = projeto_service.get_dashboard_sinergias()
    if sinergia_count is not None:
        return jsonify({'sinergias': sinergia_count}), 200
    return jsonify({'erro': 'Quantidade de sinergias não encontrados'}), 404


# Busca para o dashboard - Quantidade de Projetos
@projeto_blueprint.route('/projetos/dash', methods=['GET'])
@swag_from({
    'tags': ['Projetos'],
    'summary': 'Retorna a quantidade de projetos',
    'operationId': 'get_dashboard_projetos',
    'responses': {
        200: {
            'description': 'Quantidade de projetos retornada com sucesso',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'projetos': {
                                'type': 'integer',
                                'example': 1450
                            }
                        }
                    }
                }
            }
        },
        404: {
            'description': 'Quantidade de projetos não encontrada',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'erro': {
                                'type': 'string',
                                'example': 'Quantidade de projetos não encontrada'
                            }
                        }
                    }
                }
            }
        }
    }
})
def get_dashboard_projetos():
    projetos_count = projeto_service.get_dashboard_projetos()
    if projetos_count is not None:
        return jsonify({'projetos': projetos_count}), 200
    return jsonify({'erro': 'Quantidade de projetos não encontrada'}), 404


# Busca para o dashboard - Quantidade de Sinergias por macrotema
@projeto_blueprint.route('/projetos/sinergiaxmacrotema', methods=['GET'])
@swag_from({
    'tags': ['Projetos'],
    'summary': 'Retorna a quantidade de sinergias por macrotema',
    'operationId': 'get_dashboard_sinergia_macrotema',
    'responses': {
        200: {
            'description': 'Quantidade de sinergias por macrotema retornada com sucesso',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'additionalProperties': {
                            'type': 'integer',
                            'example': 13
                        },
                        'examples': {
                            'response': {
                                'value': {
                                    'bem-estar': 13,
                                    'conservação': 3,
                                    'diversidade': 1,
                                    'produtividade': 12,
                                    'redução': 1
                                }
                            }
                        }
                    }
                }
            }
        },
        404: {
            'description': 'Sinergias por macrotemas não encontradas',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'erro': {
                                'type': 'string',
                                'example': 'Sinergias por macrotemas não encontradas'
                            }
                        }
                    }
                }
            }
        }
    }
})
def get_dashboard_sinergia_macrotema():
    projetos = projeto_service.get_dashboard_sinergias_macrotema()  # Obtenha os projetos
    if projetos:
        return jsonify(projetos), 200
    return jsonify({'erro': 'Sinergias por macrotemas não encontradas'}), 404


# Busca para o dashboard - Quantidade de Sinergias ao longo do tempo
@projeto_blueprint.route('/projetos/sinergiaxtempo/<string:filtro>', methods=['GET'])
@swag_from({
    'tags': ['Projetos'],
    'summary': 'Retorna a quantidade de sinergias ao longo do tempo',
    'operationId': 'get_dashboard_sinergia_tempo',
    'parameters': [
        {
            'in': 'path',
            'name': 'filtro',
            'schema': {
                'type': 'string',
                'enum': ['all_time', 'last_month', 'last_week'],
                'default': 'all_time'
            },
            'required': True,
            'description': 'Filtro para selecionar o período de tempo dos dados retornados'
        }
    ],
    'responses': {
        200: {
            'description': 'Quantidade de sinergias ao longo do tempo retornada com sucesso',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'additionalProperties': {
                            'type': 'integer',
                            'example': {
                                "2024-06-07": 2,
                                "2024-06-11": 4,
                                "2024-06-12": 24
                            }
                        },
                        'examples': {
                            'response': {
                                'value': {
                                    '2024-06-07': 2,
                                    '2024-06-11': 4,
                                    '2024-06-12': 24
                                }
                            }
                        }
                    }
                }
            }
        },
        404: {
            'description': 'Projetos por tempo não encontrados',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'erro': {
                                'type': 'string',
                                'example': 'Projetos por tempo não encontrados'
                            }
                        }
                    }
                }
            }
        }
    }
})
def get_dashboard_sinergia_tempo(filtro):
    projetos = projeto_service.get_dashboard_sinergias_tempo(filtro)  # Obtenha os projetos
    if projetos:
        return jsonify(projetos), 200
    return jsonify({'erro': 'Projetos por tempo não encontrados'}), 404

# Curte e descurte projetos
@projeto_blueprint.route('/projetos/curtida/', methods=['POST'])
@Trace.REQ(['RF-009'])
@swag_from({
    'tags': ['Projetos'],
    'summary': 'Curte ou descurte um projeto',
    'operationId': 'post_curtida',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'ceo_id': {'type': 'integer', 'required': True},
                    'projeto_id': {'type': 'integer', 'required': True}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Curtida registrada',
            'schema': {
                'type': 'integer'
            }
        },
        400: {
            'description': 'Erro ao curtir projeto'
        }
    }
})
def post_curtida():
    dados = request.json
   
    try:
        curtida_data = PostCurtidaSchema().load(dados) # type: ignore
    except ValidationError as err:
        return jsonify({'erro': err.messages}), 400
   
    curtida_id = projeto_service.post_curtida(curtida_data)
   
    if curtida_id:
        return jsonify(curtida_id), 200
   
    return jsonify({'erro': 'Erro ao curtir projeto'}), 400


# Adiciona o projeto em salvos e remove projeto em salvos
@projeto_blueprint.route('/projetos/salvos/', methods=['POST'])
@Trace.REQ(['RF-011'])
@swag_from({
    'tags': ['Projetos'],
    'summary': 'Adiciona o projeto em salvos e remove projeto em salvos',
    'operationId': 'post_salvos',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'ceo_id': {'type': 'integer', 'required': True},
                    'projeto_id': {'type': 'integer', 'required': True}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Projeto salvo',
            'schema': {
                'type': 'integer'
            }
        },
        400: {
            'description': 'Erro ao salvar projeto'
        }
    }
})
def post_salvos():
    dados = request.json
   
    try:
        salvos_data = PostSalvosSchema().load(dados) # type: ignore
    except ValidationError as err:
        return jsonify({'erro': err.messages}), 400
   
    salvos_id = projeto_service.post_salvos(salvos_data)
   
    if salvos_id:
        return jsonify(salvos_id), 200
   
    return jsonify({'erro': 'Erro ao salvar projeto'}), 400


# Listar projetos curtidos
@projeto_blueprint.route('/projetos/curtidos/<int:ceo_id>', methods=['GET'])
@Trace.REQ(['RF-018'])
@swag_from({
    'tags': ['Projetos'],
    'summary': 'Retorna todos os projetos curtidos com base no ID do CEO',
    'operationId': 'get_curtidos',
    'parameters': [
        {
            'name': ' ceo_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do CEO'
        }
    ],
    'responses': {
        200: {
            'description': 'Detalhes do projeto',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'ceo_id': {'type': 'integer'},
                    'subtema_id': {'type': 'integer'},
                    'nome': {'type': 'string'},
                    'descricao': {'type': 'string'},
                    'data_criacao': {'type': 'string', 'format': 'date-time'},
                    'estado': {'type': 'string'},
                    'macrotema_nome': {'type': 'string'},
                    'subtema_nome': {'type': 'string'},
                    'ceos': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'biografia': {'type': 'string'},
                                'cargo': {'type': 'string'},
                                'celular': {'type': 'string'},
                                'email_contato': {'type': 'string'},
                                'empresa_link': {'type': 'string'},
                                'empresa_nome': {'type': 'string'},
                                'estado': {'type': 'string'},
                                'foto': {'type': 'string'},
                                'id': {'type': 'integer'},
                                'linkedin': {'type': 'string'},
                                'nome': {'type': 'string'},
                            }
                        }
                    }
                }
            }
        },
        404: {
            'description': 'CEO não encontrado'
        }
    }
})
def get_curtidos(ceo_id):
    curtidos = projeto_service.get_curtidos(ceo_id)
    if curtidos:
        print('curtidos: ', curtidos)
        return jsonify(curtidos), 200
    return jsonify({'erro': 'CEO não encontrado'}), 404


# Listar projetos salvos
@projeto_blueprint.route('/projetos/salvos/<int:ceo_id>', methods=['GET'])
@Trace.REQ(['RF-020'])
@swag_from({
    'tags': ['Projetos'],
    'summary': 'Retorna todos os projetos salvos com base no ID do CEO',
    'operationId': 'get_salvos',
    'parameters': [
        {
            'name': ' ceo_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do CEO'
        }
    ],
    'responses': {
        200: {
            'description': 'Detalhes do projeto',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'ceo_id': {'type': 'integer'},
                    'subtema_id': {'type': 'integer'},
                    'nome': {'type': 'string'},
                    'descricao': {'type': 'string'},
                    'data_criacao': {'type': 'string', 'format': 'date-time'},
                    'estado': {'type': 'string'},
                    'macrotema_nome': {'type': 'string'},
                    'subtema_nome': {'type': 'string'},
                    'ceos': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'biografia': {'type': 'string'},
                                'cargo': {'type': 'string'},
                                'celular': {'type': 'string'},
                                'email_contato': {'type': 'string'},
                                'empresa_link': {'type': 'string'},
                                'empresa_nome': {'type': 'string'},
                                'estado': {'type': 'string'},
                                'foto': {'type': 'string'},
                                'id': {'type': 'integer'},
                                'linkedin': {'type': 'string'},
                                'nome': {'type': 'string'},
                            }
                        }
                    }
                }
            }
        },
        404: {
            'description': 'CEO não encontrado'
        }
    }
})
def get_salvos(ceo_id):
    salvos = projeto_service.get_salvos(ceo_id)
    if salvos:
        print('salvos: ', salvos)
        return jsonify(salvos), 200
    return jsonify({'erro': 'CEO não encontrado'}), 404


# Cria uma atualizacao
@projeto_blueprint.route('/projetos/atualizacao', methods=['POST'])
@swag_from({
    'tags': ['Projetos'],
    'summary': 'Cria uma nova atualização de projeto',
    'operationId': 'post_atualizacao',
    'requestBody': {
        'description': 'Dados para criação de uma atualização',
        'required': True,
        'content': {
            'application/json': {
                'schema': {
                    'type': 'object',
                    'properties': {
                        'campo1': {'type': 'string', 'description': 'Descrição do campo1'},
                        'campo2': {'type': 'integer', 'description': 'Descrição do campo2'},
                        # Adicione mais campos conforme necessário
                    },
                    'example': {
                        'campo1': 'Exemplo de valor',
                        'campo2': 123,
                        # Exemplo de valores adicionais
                    }
                }
            }
        }
    },
    'responses': {
        200: {
            'description': 'ID da atualização criada',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'integer',
                        'example': 2
                    }
                }
            }
        },
        400: {
            'description': 'Erro de validação ou erro ao criar a atualização',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'erro': {'type': 'string'}
                        },
                        'example': {'erro': 'Mensagem de erro detalhada'}
                    }
                }
            }
        }
    }
})
def post_atualizacao():
    dados = request.json 
    try:
        atuaizacao_data = PostAtualizacaoSchema().load(dados) # type: ignore
    except ValidationError as err:
        return jsonify({'erro': err.messages}), 400
    
    atualizacaoId = projeto_service.post_atualizacao(atuaizacao_data)
    
    if atualizacaoId:
        return jsonify(atualizacaoId), 200
    
    return jsonify({'erro': 'Erro ao criar uma atualizaçaõ'}), 400