import os
import platform
import subprocess
from multiprocessing import Process
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

def start_service(module_name, port_env_var=None):
    env = os.environ.copy()
    if port_env_var:
        port = env.get(port_env_var)
        if port is None:
            raise ValueError(f'Porta para {port_env_var} não está definida no arquivo .env')

    if platform.system() == "Windows":
        python_executable = os.path.join(env["VIRTUAL_ENV"], "Scripts", "python.exe")
    else:  # Assume macOS or Linux
        python_executable = os.path.join(env["VIRTUAL_ENV"], "bin", "python3")
    
    if module_name == 'backend.bff.run' and platform.system() != "Windows":
        command = f"echo 'senha123' | sudo -S {python_executable} -m {module_name}"
        subprocess.run(command, shell=True, env=env)
    else:
        subprocess.run([python_executable, '-m', module_name], env=env)

def main():
    # Lista de serviços a serem iniciados
    services = [
        ('backend.ceos.run', 'CEO_PORTA'),
        ('backend.projetos.run', 'PROJETO_PORTA'),
        ('backend.recomendacao.run', 'RECOMENDACAO_PORTA'),
        ('backend.bff.run', None),
    ]

    # Iniciar serviços em processos separados
    processes = []
    for module, port in services:
        p = Process(target=start_service, args=(module, port))
        p.start()
        processes.append(p)

    # Aguardar a conclusão de todos os processos
    for p in processes:
        p.join()

if __name__ == '__main__':
    main()
