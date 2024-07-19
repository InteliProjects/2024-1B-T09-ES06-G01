@echo off
setlocal

REM Ativar o ambiente virtual
call venv\Scripts\activate

REM Ajustar o PYTHONPATH para incluir o diretório src
set PYTHONPATH=%CD%\src

REM Iniciar os serviços Flask
start cmd /k "python -m backend.ceos.run"
start cmd /k "python -m backend.projetos.run"
start cmd /k "python -m backend.recomendacao.run"
start cmd /k "python -m backend.bff.run"

endlocal
pause
