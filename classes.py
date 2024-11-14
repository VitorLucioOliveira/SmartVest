class Subscriber:
    def __init__(self, nome, temperatura, local, ar):
        self.nome = nome
        self.temperatura = temperatura
        self.local = local
        self.ar = ar

class Topico:
    def __init__(self, nome, subscribers=[]):
        self.nome = nome
        self.subscribers = subscribers


