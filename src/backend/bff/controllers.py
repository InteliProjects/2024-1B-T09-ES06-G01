import os
from flask import Flask, Blueprint, request, jsonify, Response
import requests
from dotenv import load_dotenv
from backend.external.noticias.app import consumir_API_noticias

load_dotenv()

# Blueprints para cada serviço
ceo_blueprint = Blueprint('ceo', __name__)
projeto_blueprint = Blueprint('projeto', __name__)
recomendacao_blueprint = Blueprint('recomendacao', __name__)
noticia_blueprint = Blueprint('noticia', __name__)

# Carrega as variáveis de ambiente
CEO_URL = f"{os.getenv('CEO_URL')}"
PROJETO_URL = f"{os.getenv('PROJETO_URL')}"
RECOMENDACAO_URL = f"{os.getenv('RECOMENDACAO_URL')}"

# Função para adicionar cabeçalhos CORS
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@ceo_blueprint.after_request
def after_request_ceo(response):
    return add_cors_headers(response)

@projeto_blueprint.after_request
def after_request_projeto(response):
    return add_cors_headers(response)

@recomendacao_blueprint.after_request
def after_request_recomendacao(response):
    return add_cors_headers(response)

@noticia_blueprint.after_request
def after_request_noticia(response):
    return add_cors_headers(response)

# Roteamento para o serviço de CEO
@ceo_blueprint.route('/ceos/', defaults={'subpath': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@ceo_blueprint.route('/ceos/<path:subpath>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def ceos_proxy(subpath):
    path = request.path

    query_string = request.query_string.decode('utf-8')
    full_url = f"{CEO_URL}{path}"
    if query_string:
        full_url += '?' + query_string

    resp = requests.request(
        method=request.method,
        url=full_url,
        headers={key: value for key, value in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)

    try:
        json_data = resp.json()
        return jsonify(json_data), resp.status_code
    except ValueError:
        error_message = "Erro ao processar a resposta do servidor"
        print(error_message, resp.status_code)
        return Response(error_message, status=500)

# Roteamento para o serviço de Projetos
@projeto_blueprint.route('/projetos/', defaults={'subpath': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@projeto_blueprint.route('/projetos/<path:subpath>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def projetos_proxy(subpath):
    path = request.path
    
    query_string = request.query_string.decode('utf-8')
    full_url = f"{PROJETO_URL}{path}"
    print(full_url)
    if query_string:
        full_url += '?' + query_string

    resp = requests.request(
        method=request.method,
        url=full_url,
        headers={key: value for key, value in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)
    
    try:
        json_data = resp.json()
        return jsonify(json_data), resp.status_code
    except ValueError:
        error_message = "Erro ao processar a resposta do servidor"
        print(error_message, resp.status_code)
        return Response(error_message, status=500)

# Roteamento para o serviço de Recomendações
@recomendacao_blueprint.route('/recomendacoes/', defaults={'subpath': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@recomendacao_blueprint.route('/recomendacoes/<path:subpath>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def recomendacoes_proxy(subpath):
    path = request.path

    query_string = request.query_string.decode('utf-8')
    full_url = f"{RECOMENDACAO_URL}{path}"
    if query_string:
        full_url += '?' + query_string

    resp = requests.request(
        method=request.method,
        url=full_url,
        headers={key: value for key, value in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)
    
    try:
        json_data = resp.json()
        return jsonify(json_data), resp.status_code
    except ValueError:
        error_message = "Erro ao processar a resposta do servidor"
        print(error_message, resp.status_code)
        return Response(error_message, status=500)
      
# Roteamento para o serviço de Recomendações
@noticia_blueprint.route('/noticias/<string:tema>', methods=['GET'])
def obter_noticias(tema):
    resultado = consumir_API_noticias(tema)
    return resultado