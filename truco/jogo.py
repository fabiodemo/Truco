from baralho import Baralho
from jogador import Jogador
import random

class Jogo():

    def __init__(self):
        self.rodadas = []
    
    def iniciarJogo(self):
        pass

    def criarJogador(self, nome, baralho):
        jogador = Jogador(nome)
        jogador.criarMao(baralho)
        return jogador

    def verificarGanhador(self, carta1, carta2):
        if carta1.numero > carta2.numero:
            ganhador = carta1
        else:
            ganhador = carta2
        print(ganhador.numero)
        return ganhador
    

    def quemJogaPrimeiro(jogador1, jogador2, carta1, carta2, ganhador):
        if carta1 == ganhador:
            jogador1.primeiro = True
            jogador2.primeiro = False
        elif carta2 == ganhador:
            jogador1.primeiro = False
            jogador2.primeiro = True
        elif ganhador == "Empate":
            pass

    def quemIniciaRodada(self, jogador1, jogador2):
        if jogador1.pontos == 0 and jogador2.pontos == 0:
            if jogador1.ultimo == True:
                jogador2.ultimo = True
                jogador1.ultimo = False
                jogador1.primeiro = True
                jogador2.primeiro = False
            elif jogador2.ultimo == True:
                jogador2.ultimo = False
                jogador1.primeiro = False
                jogador2.primeiro = True