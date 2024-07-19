from newsapi import NewsApiClient
from datetime import datetime, timedelta

def consumir_API_noticias(macroTema):
    # API KEY
    newsapi = NewsApiClient(api_key='5d1e4c95ba2c40d9b1a69e7e8752c519')

    # Definir as datas dinamicamente
    today = datetime.now()
    from_date = (today - timedelta(days=1)).strftime('%Y-%m-%d')
    to_date = today.strftime('%Y-%m-%d')
    
    # Parâmetros da requisição
    try:
        all_articles = newsapi.get_everything(
            q=macroTema,
            from_param=from_date,
            to=to_date,
            sort_by='relevancy',
            language='pt',
            page=1
        )

        # Verificar a resposta e extrair apenas os artigos
        if all_articles['status'] == 'ok':
            articles = all_articles['articles'][:5]  # Alterado aqui
            return {'status': 'success', 'data': articles}
        else:
            return {'status': 'error', 'message': f"Erro na requisição de notícias: {all_articles['message']}"}

    except Exception as e:
        return {'status': 'error', 'message': "Ocorreu um erro na requisição de notícias"}