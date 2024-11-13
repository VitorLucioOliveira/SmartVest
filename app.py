from flask import Flask, render_template
import json
app = Flask(__name__)


class Subscriber:
    def __init__(self, nome, temperatura, local, ar):
        self.nome = nome
        self.temperatura = temperatura
        self.local = local
        self.ar= ar


class Topico:
    def __init__(self, nome, subscribers=[]):
        self.nome = nome
        self.subscribers = subscribers


# Função para carregar tópicos do JSON
def carregar_topicos(caminho_arquivo):
    with open(caminho_arquivo, 'r') as file:
        dados = json.load(file)

    topicos = []
    for item in dados:
        nome = item['nome']
        subscribers_data = item['subscribers']
        subscribers = [
            Subscriber(sub['nome'], sub['temperatura'], sub['local'], sub['ar'])
            for sub in subscribers_data
        ]
        topico = Topico(nome, subscribers)
        topicos.append(topico)

    return topicos

# Carregar os tópicos ao iniciar o aplicativo
lista_topicos = carregar_topicos('data/topicos.json')

app = Flask(__name__)
@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html', topicos=lista_topicos)


if __name__ == '__main__':
    app.run(debug=True)
