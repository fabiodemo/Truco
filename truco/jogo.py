from .baralho import Baralho
from .jogador import Jogador
from .bot import Bot
from .pontos import MANILHA, CARTAS_VALORES
import random

class Jogo():

    def __init__(self):
        self.rodadas = []
        self.trucoPontos = 1
    
    def iniciarJogo(self):
        pass

    def criar_jogador(self, nome, baralho):
        jogador = Jogador(nome)
        jogador.criar_mao(baralho)
        return jogador

    def criar_bot(self, nome, baralho):
        bot = Bot(nome)
        bot.criar_mao(baralho)
        return bot

    def verificar_ganhador(self, carta1, carta2):
        # print("numeros: ")
        # print(str(carta1.numero))
        # print(str(carta2.numero))
        ganhador = self.verificar_carta_vencedora(carta1, carta2)
        print("\nCarta ganhadora: ")
        print(ganhador.exibir_carta())
        return ganhador
        # if self.verificar_carta_vencedora(carta1, carta2) is None:
        #     if carta1.numero == carta2.numero:
        #         ganhador = "Empate"
        #     elif CARTAS_VALORES[str(carta1.numero)] > CARTAS_VALORES[str(carta2.numero)]:
        #         ganhador = carta1
        #     else:
        #         ganhador = carta2
        #     print(ganhador)
        #     return ganhador
        # else:
        #     return self.verificar_carta_vencedora(carta1, carta2)

    
    def adicionar_rodada(self, jogador1, jogador2, carta1, carta2, ganhador):
        if ganhador == "Empate":
            jogador1.adicionar_rodada()
            jogador2.adicionar_rodada()
            return "Empate"
        
        elif ganhador == carta1:
            jogador1.adicionar_rodada()
            # ganhador.adicionar_rodada()
        
        elif ganhador == carta2:
            jogador2.adicionar_rodada()
            # ganhador.adicionar_rodada()
        
        else:
            return "Erro"

    def quem_joga_primeiro(self, jogador1, jogador2, carta1, carta2, ganhador):
        if carta1 == ganhador:
            jogador1.primeiro = True
            jogador2.primeiro = False
        
        elif carta2 == ganhador:
            jogador1.primeiro = False
            jogador2.primeiro = True
        
        elif ganhador == "Empate":
            pass

    def quem_inicia_rodada(self, jogador1, jogador2):
        if jogador1.rodadas == 0 and jogador2.rodadas == 0:
            if jogador1.ultimo == True:
                jogador2.ultimo = True
                jogador1.ultimo = False
                jogador1.primeiro = True
                jogador2.primeiro = False
            
            elif jogador2.ultimo == True:
                jogador2.ultimo = False
                jogador1.primeiro = False
                jogador2.primeiro = True

    def verificar_carta_vencedora(self, carta_jogador_01, carta_jogador_02):
        if (str(carta_jogador_01.numero)+" de "+carta_jogador_01.naipe) in MANILHA and (str(carta_jogador_02.numero)+" de "+carta_jogador_02.naipe) in MANILHA:
            if MANILHA[str(carta_jogador_01.numero)+" de "+carta_jogador_01.naipe] > MANILHA[str(carta_jogador_02.numero)+" de "+carta_jogador_02.naipe]:
                return carta_jogador_01
           
            elif MANILHA[str(carta_jogador_02.numero)+" de "+carta_jogador_02.naipe] > MANILHA[str(carta_jogador_01.numero)+" de "+carta_jogador_01.naipe]:
                return carta_jogador_02
        
        elif (str(carta_jogador_01.numero)+" de "+carta_jogador_01.naipe) in MANILHA:
            return carta_jogador_01
        
        elif (str(carta_jogador_02.numero)+" de "+carta_jogador_02.naipe) in MANILHA:
            return carta_jogador_02
        
        else:
            if CARTAS_VALORES[str(carta_jogador_01.numero)] >= CARTAS_VALORES[str(carta_jogador_02.numero)]:
                return carta_jogador_01
        
            elif CARTAS_VALORES[str(carta_jogador_01.retornar_numero())] < CARTAS_VALORES[str(carta_jogador_02.retornar_numero())]:
                return carta_jogador_02
        
            else:
                return "Empate"

    def jogador_fugiu(self, jogador, jogador1, jogador2, pontos):
        print('jogador {jogador.nome} fugiu!')
        jogador1.primeiro = True
        jogador2.primeiro = False
    

    # def trucoAceito(self, aceitou):
    #     print("Truco")
    #     if (aceitou is False and self.trucoPontos == 1):
    #         self.trucoPontos = 1
            
    #     elif (aceitou is False and self.trucoPontos != 1):
    #         self.trucoPontos -= 1

    #     elif (self.trucoPontos == 1):
    #         self.trucoPontos += 1
        
    #     else:
    #         self.trucoPontos +=2
    
    # def retornaTrucoPontos(self):
    #     return self.trucoPontos
    
    # def resetarTrucoPontos(self):
    #     self.trucoPontos = 1