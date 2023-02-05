from .carta import Carta
import random


class Baralho():
    
    def __init__(self):
        # self.vira = []
        self.manilhas = []
        self.cartas = []
        self.criar_baralho() 

    def criar_baralho(self):
        for i in ["ESPADAS", "OUROS", "COPAS", "BASTOS"]:
            for n in range(1, 13):
                if n < 8 or n >= 10:
                    self.cartas.append(Carta(n, i))
    
    def embaralhar(self):
        random.shuffle(self.cartas)

    def retirar_carta(self):
        return self.cartas.pop()
    
    def resetar(self):
        self.vira = []
        self.manilhas = []
        self.cartas = []
    
    def printar_baralho(self):
        for c in self.cartas:
            c.exibir_carta()