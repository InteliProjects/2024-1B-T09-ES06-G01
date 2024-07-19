# import pandas as pd
# from sklearn.decomposition import NMF
# from sklearn.metrics import mean_squared_error, mean_absolute_error
# import numpy as np
# from joblib import dump

# # Carrega os dados do arquivo CSV em um DataFrame Pandas
# df = pd.read_csv('./data/processed/base-de-dados-final.csv')

# # Cria uma matriz de avaliações onde cada linha representa um avaliador, 
# # cada coluna representa um projeto e os valores representam as avaliações dadas pelos avaliadores aos projetos.
# # Qualquer célula sem avaliação (NaN) é preenchida com 0.
# matriz_avaliacoes = df.pivot(index='avaliador_id', columns='projeto_id', values='avaliacao').fillna(0)

# matriz_avaliacoes

# # Define o modelo de recomendação usando NMF
# modelo = NMF(n_components=10, init='random', random_state=42)

# # Treina o modelo NMF usando as avaliações dos usuários nos projetos
# # W contém as características latentes dos usuários
# # H contém as características latentes dos projetos
# W = modelo.fit_transform(matriz_avaliacoes)
# H = modelo.components_

# # Exporta o modelo treinado para uso futuro
# # O arquivo é salvo no diretório './models' com o nome 'modelo-de-recomendacao-por-filtragem-colaborativa-por-usuario.pkl'
# dump((modelo, W, H, matriz_avaliacoes), './models/modelo-de-recomendacao-por-filtragem-colaborativa-por-usuario2.pkl')

# # Função para recomendar projetos para um usuário
# def recomendar(usuario_id):
#     # Índice do usuário na matriz
#     idx_usuario = matriz_avaliacoes.index.get_loc(usuario_id)
    
#     # Pontuações previstas para o usuário
#     pontuacoes = W[idx_usuario, :].dot(H)
    
#     # Projetos já avaliados pelo usuário
#     projetos_avaliados = matriz_avaliacoes.columns[matriz_avaliacoes.iloc[idx_usuario, :] > 0].tolist()

#     # Filtra as pontuações para excluir projetos já avaliados pelo usuário
#     # Cria uma lista de dicionários contendo o ID do projeto e sua pontuação
#     pontuacoes = [{'id': matriz_avaliacoes.columns[index], 'pontuacao': pontuacao} for index, pontuacao in enumerate(pontuacoes) if projeto_id not in projetos_avaliados]
    
#     # Ordena as recomendações por pontuação, do maior para o menor
#     pontuacoes = sorted(pontuacoes, key=lambda x: x['pontuacao'], reverse=True)
    
#     return pontuacoes

# # Obtém as previsões do modelo para todas as avaliações e arredonda os valores
# previsoes = pd.DataFrame(W.dot(H), 
#                          columns=matriz_avaliacoes.columns, 
#                          index=matriz_avaliacoes.index)

# # Calcula o RMSE e o MAE (Root Mean Square Error e Mean Absolute Error) para avaliar o desempenho do modelo
# # Primeiro, converte as matrizes reais e previstas em arrays numpy para cálculo
# avaliacoes_reais = matriz_avaliacoes.values
# avaliacoes_previstas = previsoes.values

# # Remove os valores nulos nas previsões (caso haja)
# # Isso é necessário para garantir que apenas as avaliações reais e previstas correspondentes sejam usadas nos cálculos das métricas
# avaliacoes_reais = avaliacoes_reais[~np.isnan(avaliacoes_previstas)]
# avaliacoes_previstas = avaliacoes_previstas[~np.isnan(avaliacoes_previstas)]

# # Calcula o RMSE e o MAE usando as métricas do Scikit-Learn
# rmse = mean_squared_error(avaliacoes_reais, avaliacoes_previstas, squared=False)
# mae = mean_absolute_error(avaliacoes_reais, avaliacoes_previstas)

# import pandas as pd
# from dotenv import load_dotenv
# import os
# from sqlalchemy import create_engine
# from sklearn.decomposition import NMF
# from joblib import dump
# from datetime import datetime

# def retreinar_modelo():
#     load_dotenv()

#     # Definir a string de conexão
#     DATABASE_URI = os.getenv('DB_URL').replace('postgres', 'postgresql')

#     engine = create_engine(DATABASE_URI)

#     # Consultas para carregar os dados
#     query_ratings = 'SELECT * FROM Interacao WHERE avaliacao IS NOT NULL'

#     # Carregar dados em DataFrames
#     df_ratings = pd.read_sql(query_ratings, engine)

#     # Criar a matriz de avaliações dos usuários nos projetos
#     matriz_avaliacoes = df_ratings.pivot(index='ceo_id', columns='projeto_id', values='avaliacao').fillna(0)

#     if matriz_avaliacoes.shape[0] == 0 or matriz_avaliacoes.shape[1] == 0:
#         return None
    
#     # Define o modelo de recomendação usando NMF
#     modelo = NMF(n_components=10, init='random', random_state=42)

#     # Treina o modelo NMF usando as avaliações dos usuários nos projetos
#     W = modelo.fit_transform(matriz_avaliacoes)
#     H = modelo.components_

#     # Adiciona timestamp ao nome do arquivo
#     timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
#     modelo_path = f'./models/modelo-de-recomendacao-por-filtragem-colaborativa-{timestamp}.pkl'

#     # Exporta o modelo treinado para uso futuro
#     dump((modelo, W, H, matriz_avaliacoes), modelo_path)

#     return modelo_path


# import os
# from joblib import load

# def get_latest_model_path(models_dir='./models'):
#     # Lista todos os arquivos no diretório de modelos
#     model_files = [f for f in os.listdir(models_dir) if f.startswith('modelo-de-recomendacao-por-filtragem-colaborativa')]
    
#     # Ordena os arquivos por timestamp
#     model_files.sort(reverse=True)
    
#     # Retorna o caminho do arquivo mais recente
#     latest_model_path = os.path.join(models_dir, model_files[0])
    
#     return latest_model_path

# def gerar_recomendacoes(usuario_id):
#     # Carregar o modelo mais recente
#     latest_model_path = get_latest_model_path()
    
#     _, W, H, matriz_avaliacoes = load(latest_model_path)

#     # Índice do usuário na matriz
#     idx_usuario = matriz_avaliacoes.index.get_loc(usuario_id)
    
#     # Pontuações previstas para o usuário
#     pontuacoes = W[idx_usuario, :].dot(H)
    
#     # Projetos já avaliados pelo usuário
#     projetos_avaliados = matriz_avaliacoes.columns[matriz_avaliacoes.iloc[idx_usuario, :] > 0].tolist()

#     # Filtra as pontuações para excluir projetos já avaliados pelo usuário
#     # Cria uma lista de dicionários contendo o ID do projeto e sua pontuação
#     pontuacoes = [{'id': matriz_avaliacoes.columns[index], 'pontuacao': pontuacao} for index, pontuacao in enumerate(pontuacoes) if matriz_avaliacoes.columns[index] not in projetos_avaliados]
    
#     # Ordena as recomendações por pontuação, do maior para o menor
#     pontuacoes = sorted(pontuacoes, key=lambda x: x['pontuacao'], reverse=True)
    
#     return pontuacoes


