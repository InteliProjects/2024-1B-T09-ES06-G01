from .app import create_app
from backend.common.traceability import Trace

app = create_app()

if __name__ == '__main__':
    print(Trace.matrix())
    # Rodar o servidor acessível em toda a rede
    app.run(host='0.0.0.0', port=80)
