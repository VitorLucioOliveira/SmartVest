from pydoc import importfile

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import json
import threading
import time
import os



app = Flask(__name__)
socketio = SocketIO(app)

class Subscriber:
    def __init__(self, id, alerta):
        self.id = id
        self.alerta = alerta


class Topico:
    def __init__(self, nome, subscribers=[]):
        self.nome = nome
        self.subscribers = subscribers






# Função para converter objetos Topico e Subscriber em dicionários
def topicos_para_dict(topicos):
    return [
        {
            'nome': topico.nome,
            'subscribers': [
                {'id': sub.id, 'alerta': sub.alerta}
                for sub in topico.subscribers
            ]
        }
        for topico in topicos
    ]

# Função para carregar tópicos do JSON
def carregar_topicos(caminho_arquivo):
    with open(caminho_arquivo, 'r') as file:
        dados = json.load(file)

    topicos = []
    for item in dados:
        nome = item['nome']
        subscribers_data = item['subscribers']
        subscribers = [
            Subscriber(sub['id'], sub['alerta'])
            for sub in subscribers_data
        ]
        topico = Topico(nome, subscribers)
        topicos.append(topico)

    return topicos

# Função para enviar as atualizações de tópicos apenas quando o arquivo é modificado
def atualizar_json():
    last_modified = None
    while True:
        time.sleep(3)  # Verifica mudanças a cada 3 segundos

        # Verifica o horário da última modificação no arquivo JSON
        modified_time = os.path.getmtime('data/topicos.json')
        if last_modified is None or modified_time != last_modified:
            last_modified = modified_time
            lista_topicos = carregar_topicos('data/topicos.json')
            socketio.emit('atualizacao_topicos', {'topicos': topicos_para_dict(lista_topicos)})

# Rota para iniciar a atualização automática
@socketio.on('connect')
def handle_connect():
    print("Cliente conectado")
    # Inicia uma thread que manda as atualizações periodicamente
    threading.Thread(target=atualizar_json, daemon=True).start()

@app.route('/')
def hello_world():
    # Carrega os tópicos do JSON a cada requisição
    lista_topicos = carregar_topicos('data/topicos.json')
    return render_template('index.html', topicos=lista_topicos)

if __name__ == '__main__':
    socketio.run(app, debug=True)
