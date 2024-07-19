from flask import Flask, request, jsonify
from flask_socketio import SocketIO, join_room, leave_room
from backend.common.traceability import Trace

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('connect')
def handle_connect():
    print('Cliente conectado')

@socketio.on('disconnect')
def handle_disconnect():
    print('Cliente desconectado')

@socketio.on('join')
def on_join(data):
    room = data['room']
    join_room(room)
    print(f'Entrou na sala: {room}')

@socketio.on('leave')
def on_leave(data):
    room = data['room']
    leave_room(room)
    print(f'Saiu da sala: {room}')

@app.route('/send_notification', methods=['POST'])
@Trace.REQ(['RF-013'])
def send_notification():
    data = request.json
    print(data)
    if data is not None:
        evento = data.get('evento') 
        dados = data.get('dados')
        sala = data.get('sala')
        print(f'Enviando notificação para {sala}')
        socketio.emit(evento, dados, to=sala)
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    print(Trace.matrix())
    print('Servidor rodando....')
    socketio.run(app, host='0.0.0.0', port=5000, reloader_options={'reload': True}) # type: ignore
