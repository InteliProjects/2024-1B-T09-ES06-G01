from flask import Blueprint, jsonify, request
from backend.ceos.services import CeoService
from backend.projetos.models import ProjetoModel
from backend.ceos.models import CeoModel
from marshmallow import Schema, fields, ValidationError, validate
from flasgger import swag_from
from backend.common.traceability import Trace

# Criação do blueprint para CEOs, associado ao nome 'ceo'
ceo_blueprint = Blueprint('ceo', __name__)
# Instância do serviço de CEOs, usando o modelo CeoModel para operações de banco de dados
ceo_service = CeoService(CeoModel, ProjetoModel)

# Definição de um schema usando Marshmallow para validação dos dados de entrada
class CeoSchema(Schema):
    nome = fields.Str()
    cargo = fields.Str()
    empresa_nome = fields.Str()
    estado = fields.Str(validate=validate.OneOf(['ativo', 'inativo']), default='ativo')
    biografia = fields.Str()
    celular = fields.Str()
    email_contato = fields.Str(validate=validate.Email())
    empresa_link = fields.Str()
    empresa_nome = fields.Str()
    foto = fields.Str()
    linkedin = fields.Str()
    email = fields.Str(validate=validate.Email())
    senha = fields.Str()

# Rota para obter a lista de todos os CEOs
@ceo_blueprint.route('/ceos/', methods=['GET'])
@Trace.REQ(["RF-005"])
@swag_from({
    'tags': ['CEOs'],
    'summary': 'Obtém a lista completa de CEOs',
    'operationId': 'get_ceos',
    'responses': {
        200: {
            'description': 'Lista de CEOs',
            'schema': {
                'type': 'object',
                'properties': {
                    'quantidade': {'type': 'integer'},
                    'ceos': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'integer'},
                                'nome': {'type': 'string'},
                                'cargo': {'type': 'string'},
                                'empresa_nome': {'type': 'string'},
                                'estado': {'type': 'string'},
                                'biografia': {'type': 'string'},
                                'celular': {'type': 'string'},
                                'email_contato': {'type': 'string'},
                                'empresa_link': {'type': 'string'},
                                'foto': {'type': 'string'},
                                'linkedin': {'type': 'string'}
                            }
                        }
                    }
                }
            }
        }
    }

})
def get_ceos():
    ceos = ceo_service.get_ceos()
    return jsonify({'quantidade': len(ceos), 'ceos': ceos}), 200

# Rota para obter um único CEO pelo ID
@ceo_blueprint.route('/ceos/<int:ceo_id>', methods=['GET'])
@Trace.REQ(["RF-005"])
@swag_from({
    'tags': ['CEOs'],
    'summary': 'Obtém um CEO pelo ID',
    'operationId': 'get_ceo',
    'parameters': [
        {
            'in': 'path',
            'name': 'ceo_id',
            'type': 'integer',
            'required': True
        }
    ],
    'responses': {
        200: {
            'description': 'CEO encontrado',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'nome': {'type': 'string'},
                    'cargo': {'type': 'string'},
                    'empresa_nome': {'type': 'string'},
                    'estado': {'type': 'string'},
                    'biografia': {'type': 'string'},
                    'celular': {'type': 'string'},
                    'email_contato': {'type': 'string'},
                    'empresa_link': {'type': 'string'},
                    'foto': {'type': 'string'},
                    'linkedin': {'type': 'string'}
                }
            }
        },
        404: {
            'description': 'CEO não encontrado'
        }
    }
})
def get_ceo(ceo_id):
    ceo = ceo_service.get_ceo(ceo_id)
    if ceo:
        return jsonify(ceo), 200
    return jsonify({'mensagem': 'CEO não encontrado'}), 404

# Rota para criar um novo CEO com validação de dados
@ceo_blueprint.route('/ceos/', methods=['POST'])
@Trace.REQ(["RF-001"])
@swag_from({
    'tags': ['CEOs'],
    'summary': 'Cria um novo CEO',
    'operationId': 'post_ceo',
    'parameters': [
        {
            'in': 'body',
            'name': 'ceo',
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string'},
                    'cargo': {'type': 'string'},
                    'empresa_nome': {'type': 'string'},
                    'estado': {'type': 'string'},
                    'biografia': {'type': 'string'},
                    'celular': {'type': 'string'},
                    'email_contato': {'type': 'string'},
                    'empresa_link': {'type': 'string'},
                    'foto': {'type': 'string'},
                    'linkedin': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'CEO criado',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'nome': {'type': 'string'},
                    'cargo': {'type': 'string'},
                    'empresa_nome': {'type': 'string'},
                    'estado': {'type': 'string'},
                    'biografia': {'type': 'string'},
                    'celular': {'type': 'string'},
                    'email_contato': {'type': 'string'},
                    'empresa_link': {'type': 'string'},
                    'foto': {'type': 'string'},
                    'linkedin': {'type': 'string'}
                }
            }
        },
        400: {
            'description': 'Erro de validação'
        }
    }
})
def create_ceo():
    try:
        ceo = CeoSchema().load(request.json) # type: ignore
        ceo_service.create_ceo(ceo)
        return jsonify(ceo), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

# Rota para atualizar um CEO existente pelo ID com validação de dados
@ceo_blueprint.route('/ceos/<int:ceo_id>', methods=['PUT'])
@Trace.REQ(["RF-002"])
@swag_from({
    'tags': ['CEOs'],
    'summary': 'Atualiza um CEO pelo ID',
    'operationId': 'put_ceo',
    'parameters': [
        {
            'in': 'path',
            'name': 'ceo_id',
            'type': 'integer',
            'required': True
        },
        {
            'in': 'body',
            'name': 'ceo',
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string'},
                    'cargo': {'type': 'string'},
                    'empresa_nome': {'type': 'string'},
                    'estado': {'type': 'string'},
                    'biografia': {'type': 'string'},
                    'celular': {'type': 'string'},
                    'email_contato': {'type': 'string'},
                    'empresa_link': {'type': 'string'},
                    'foto': {'type': 'string'},
                    'linkedin': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'CEO atualizado',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'nome': {'type': 'string'},
                    'cargo': {'type': 'string'},
                    'empresa_nome': {'type': 'string'},
                    'estado': {'type': 'string'},
                    'biografia': {'type': 'string'},
                    'celular': {'type': 'string'},
                    'email_contato': {'type': 'string'},
                    'empresa_link': {'type': 'string'},
                    'foto': {'type': 'string'},
                    'linkedin': {'type': 'string'}
                }
            }
        },
        400: {
            'description': 'Erro de validação'
        }
    }
})
def update_ceo(ceo_id):
    try:
        ceo = CeoSchema().load(request.json) # type: ignore
        ceo_service.update_ceo(ceo_id, ceo)
        return jsonify(ceo), 200
    except ValidationError as err:
        return jsonify(err.messages), 400

# Rota para deletar um CEO pelo ID
@ceo_blueprint.route('/ceos/<int:ceo_id>', methods=['DELETE'])
@Trace.REQ(["RF-004"])
@swag_from({
    'tags': ['CEOs'],
    'summary': 'Deleta um CEO pelo ID',
    'operationId': 'delete_ceo',
    'parameters': [
        {
            'in': 'path',
            'name': 'ceo_id',
            'type': 'integer',
            'required': True
        }
    ],
    'responses': {
        200: {
            'description': 'CEO deletado'
        }
    }
})
def delete_ceo(ceo_id):
    ceo_service.delete_ceo(ceo_id)
    return jsonify({'mensagem': 'CEO deletado'}), 200

# Rota para verificar a autenticação de um CEO
@ceo_blueprint.route('/ceos/login', methods=['POST'])
@Trace.REQ(["RF-003"])
@swag_from({
    'tags': ['CEOs'],
    'summary': 'Realiza login de um CEO',
    'operationId': 'login',
    'parameters': [
        {
            'in': 'body',
            'name': 'login',
            'schema': {
                'type': 'object',
                'properties': {
                    'email': {'type': 'string'},
                    'senha': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Login realizado',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'}
                }
            }
        },
        401: {
            'description': 'Credenciais inválidas'
        }
    }
})
def login():
    dados = request.json
    id = ceo_service.login(dados)

    if id:
        return jsonify({'id': id}), 200

    return jsonify({'mensagem': 'erro'}), 401


# Busca para o dashboard - Quantidade de Projetos
@ceo_blueprint.route('/ceos/dash', methods=['GET'])
@swag_from({
    'tags': ['CEOs'],
    'summary': 'Retorna a quantidade de CEOs',
    'operationId': 'get_dashboard_ceos',
    'responses': {
        200: {
            'description': 'Quantidade de CEOs retornada com sucesso',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'ceos': {
                                'type': 'integer',
                                'example': 1451
                            }
                        }
                    }
                }
            }
        },
        404: {
            'description': 'Quantidade de CEOs não encontrada',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'erro': {
                                'type': 'string',
                                'example': 'Quantidade de Ceos não encontrada'
                            }
                        }
                    }
                }
            }
        }
    }
})
def get_dashboard_ceos():
    ceos_count = ceo_service.get_dashboard_ceos()
    if ceos_count is not None:
        return jsonify({'ceos': ceos_count}), 200
    return jsonify({'erro': 'Quantidade de Ceos não encontrada'}), 404
