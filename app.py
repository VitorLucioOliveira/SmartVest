from flask import Flask, render_template



class Topico:
    def __init__(self, nome, subscribers):
        self.nome = nome
        self.subscribers = subscribers if subscribers is not None else []


#topico1 = Topico("Topico 1", ["Alice", "Bob", "Vitor", ])
#topico2 = Topico("Topico 2", ["Alice", "Bob","Pedro"])
#topico3 = Topico("Topico 3", ["Alice", "Bob", "Vitor"])
#topico4 = Topico("Topico 4", ["Alice", "Bob", "Vitor"])
#topico5 = Topico("Topico 5", ["Alice", "Bob", "Vitor"])
#topico6 = Topico("Topico 6", ["Alice", "Bob", "Vitor"])
#topico7 = Topico("Topico 7", ["Alice", "Bob", "Vitor"])

topico1 = Topico("Topico 1", ["A1B2C", "D3E4F", "G5H6I", "J7K8L"])  # 4 subscribers
topico2 = Topico("Topico 2", ["M9N0P", "Q1R2S", "T3U4V"])  # 3 subscribers
topico3 = Topico("Topico 3", ["W5X6Y", "Z7A8B", "C9D0E", "F1G2H", "I3J4K"])  # 5 subscribers
topico4 = Topico("Topico 4", ["L5M6N", "O7P8Q"])  # 2 subscribers
topico5 = Topico("Topico 5", ["R9S0T", "U1V2W", "X3Y4Z", "A5B6C"])  # 4 subscribers
topico6 = Topico("Topico 6", ["D7E8F", "G9H0I", "J1K2L", "M3N4O", "P5Q6R"])  # 5 subscribers
topico7 = Topico("Topico 7", ["S7T8U", "V9W0X", "Y1Z2A", "B3C4D", "E5F6G", "H7I8J"])  # 6 subscribers
topico8 = Topico("Topico 8", ["K9L0M", "N1O2P", "Q3R4S", "T5U6V", "W7X8Y"])  # 5 subscribers


lista_topicos = [topico1, topico2, topico3, topico4]
lista_topicos2 = [topico1, topico2, topico3, topico4, topico5, topico6, topico7, topico8]
app = Flask(__name__)
@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html', topicos=lista_topicos)


if __name__ == '__main__':
    app.run(debug=True)
