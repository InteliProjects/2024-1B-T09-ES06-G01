from flask import Blueprint, jsonify, request
from marshmallow import Schema, fields, ValidationError
from backend.recomendacao.services import RecomendacaoService
from backend.recomendacao.models import Recomendacao
from backend.ceos.models import CeoModel
from backend.projetos.models import ProjetoModel, InteracaoModel, SubtemaModel, MacrotemaModel
from backend.common.traceability import Trace

recomendacao_service = RecomendacaoService(Recomendacao, CeoModel, ProjetoModel, InteracaoModel, SubtemaModel, MacrotemaModel)

recomendacao_blueprint = Blueprint('recomendacao', __name__)

# Classe do Marshmallow para a validação de dados de entrada - Criação de recomendações
class PostRecomendacao(Schema):
    ceo_id = fields.Int(required=True)
    projeto_id = fields.Int(required=True)
    tipo = fields.Str(required=True)
    pontuacao = fields.Int(required=True)

# Classe do Marshmallow para a validação de dados de entrada - Atualização de recomendações
class PutRecomendacao(Schema):
    pontuacao = fields.Int(required=True)

class RecomendacaoSchema(Schema):

    @recomendacao_blueprint.route('/recomendacoes/recomendar/<int:usuario_id>', methods=['GET'])
    @Trace.REQ(['RF-016'])
    def gerar_recomendacao(usuario_id):
        projetos = recomendacao_service.gerar_recomendacao(usuario_id)
        if projetos:
            return [projeto for projeto in projetos], 200
        return jsonify({'message': 'Recomendação not found'}), 404
    
    @recomendacao_blueprint.route('/recomendacoes/<int:recomendacao_id>', methods=['GET'])
    def get_recomendacao(recomendacao_id):
        rec = recomendacao_service.get_recomendacao_by_id(recomendacao_id)
        if rec:
            return jsonify(rec), 200
        return jsonify({'message': 'Recomendação not found'}), 404

    @recomendacao_blueprint.route('/recomendacoes/', methods=['GET'])
    def get_recomendacoes():
        rec = recomendacao_service.get_all_recomendacao()
        if rec:
            return ([recomendacao.to_dict() for recomendacao in rec]), 200
        return jsonify({'message': 'Recomendação nott found'}), 404

    @recomendacao_blueprint.route('/recomendacoes/', methods=['POST'])
    def post_recomendacao():
        dados = request.json
        try:
            recomendacao_data = PostRecomendacao().load(dados) # type: ignore
        except ValidationError as err:
            return jsonify({'erro': err.messages}), 400
        recomendacao = recomendacao_service.post_recomendacao(recomendacao_data)
        if recomendacao:
            return jsonify(recomendacao), 200
        return jsonify({'erro': 'Erro ao criar o projeto'}), 400

    @recomendacao_blueprint.route('/recomendacoes/<int:recomendacao_id>', methods=['DELETE'])
    def delete_recomendacao(recomendacao_id): 
        recomendacaoId = recomendacao_service.delete_recomendacao(recomendacao_id)
        if recomendacaoId:
            return jsonify(recomendacaoId), 200
        return jsonify({'erro': 'Erro ao apagar a recomendação'}), 400
    
    @recomendacao_blueprint.route('/recomendacoes/<int:recomendacao_id>', methods=['PUT'])
    def put_recomendacao(recomendacao_id):
        dados = request.json
        try:
            recomendacao_data = PutRecomendacao().load(dados) # type: ignore
        except ValidationError as err:
            return jsonify({'erro': err.messages}), 400
        
        recomendacaoId = recomendacao_service.put_recomendacao(recomendacao_id, recomendacao_data)
        if recomendacaoId:
            return jsonify(recomendacaoId), 200
        
        return jsonify({'erro': 'Erro ao atualizar a recomendação'}), 400