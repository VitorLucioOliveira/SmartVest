from flask import Flask, render_template



class Topico:
    def __init__(self, nome, subscribers):
        self.nome = nome
        self.subscribers = subscribers if subscribers is not None else []


topico1 = Topico("Teste1", ["Alice", "Bob", "Vitor"])
topico2 = Topico("Teste2", ["Alice", "Bob", "Vitor"])
topico3 = Topico("Teste3", ["Alice", "Bob", "Vitor"])
topico4 = Topico("Teste4", ["Alice", "Bob", "Vitor"])
topico5 = Topico("Teste5", ["Alice", "Bob", "Vitor"])
topico6 = Topico("Teste6", ["Alice", "Bob", "Vitor"])
topico7 = Topico("Teste7", ["Alice", "Bob", "Vitor"])


lista_topicos = [topico1, topico2, topico3, topico4]
app = Flask(__name__)
@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html', topicos=lista_topicos)


if __name__ == '__main__':
    app.run()
