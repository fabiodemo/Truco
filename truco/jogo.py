from baralho import Baralho
from jogador import Jogador
import random
from carta import Carta

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
        print("numeros: ")
        print(str(carta1.numero))
        print(str(carta2.numero))
        if Carta.verificarManilha(carta1, carta2) is None:
            if carta1.numero > carta2.numero:
                ganhador = carta1
            else:
                ganhador = carta2
            print(ganhador.numero)
            return ganhador
        else:
            return Carta.verificarManilha(None, carta1, carta2)

    
    def adicionarPonto(self, jogador1, jogador2, carta1, carta2, ganhador):
        if ganhador == "Empate":
            jogador1.adicionarPonto()
            jogador2.adicionarPonto()
            return "Empate"
        elif ganhador == carta1:
            jogador1.adicionarPonto()
            ganhador.printarCarta()
        elif ganhador == carta2:
            jogador2.adicionarPonto()
            ganhador.printarCarta()
        else:
            return "Erro"

    def quemJogaPrimeiro(self, jogador1, jogador2, carta1, carta2, ganhador):
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