import csv
import os

class Trace:
    # Dicionário para armazenar a relação entre métodos e códigos de requisitos.
    requirements_dict = {}

    # Dicionário para armazenar a relação entre testes e códigos de requisitos.
    test_requirements_dict = {}

    @staticmethod
    def REQ(req_code):
        """
        Método decorador para anotar métodos com um código de requisito específico.
        :param req_code: O código do requisito a ser associado ao método.
        :return: Um decorador que anota o método com o código de requisito.
        """
        def decorator(func):
            # Armazena o nome do método e o código do requisito associado no dicionário.
            Trace.requirements_dict[func.__name__] = req_code
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            wrapper.__name__ = func.__name__
            return wrapper
        return decorator

    @staticmethod
    def get_req_code(func):
        """
        Retorna o código do requisito associado a um método.
        :param func: A função cujo código de requisito é desejado.
        :return: O código do requisito se existir, ou "None" se não for encontrado.
        """
        return Trace.requirements_dict.get(func.__name__, "None")

    @staticmethod
    def matrix():
        """
        Gera uma matriz de rastreabilidade mapeando métodos aos códigos de requisitos.
        :return: Um dicionário representando a matriz de rastreabilidade.
        """
        matrix = {}

        csv_file_path = '../docs/outros/traceability_matrix.csv'
        
        # Se o arquivo existir, carregue o conteúdo existente.
        if os.path.exists(csv_file_path):
            with open(csv_file_path, mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader, None)  # Pula o cabeçalho
                for row in reader:
                    if len(row) == 2:
                        method, req_code = row
                        matrix[method] = req_code
        
        # Atualiza o conteúdo existente com os novos dados.
        for method, req_code in Trace.requirements_dict.items():
            matrix[method] = req_code
        
        # Escreve os dados atualizados de volta no arquivo CSV.
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Escreve o cabeçalho.
            writer.writerow(['Método', 'Código do Requsito'])
            # Escreve os dados dos métodos e códigos de requisitos.
            for method, req_code in matrix.items():
                writer.writerow([method, req_code])
            
        return matrix
