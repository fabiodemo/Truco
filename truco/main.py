from baralho import Baralho
from carta import Carta
from jogador import Jogador
from jogo import Jogo
import random
import os

def reiniciarJogo():
    jogador1.resetar()
    jogador2.resetar()
    baralho.resetarBaralho()
    baralho.criarBaralho()
    baralho.embaralhar()
    # baralho.definirVira(baralho)
    # manilha = baralho.definirManilha()
    # baralho.definirManilhas(manilha)
    jogador1.criarMao(baralho)
    jogador2.criarMao(baralho)

def limpar():
    os.system("clear")

def border_msg(msg, indent=1, width=None, title=None):
    """Print message-box with optional title."""
    lines = msg.split('\n')
    space = " " * indent
    if not width:
        width = max(map(len, lines))
    box = f'╔{"═" * (width + indent * 2)}╗\n'  # upper_border
    if title:
        box += f'║{space}{title:<{width}}{space}║\n'  # title
        box += f'║{space}{"-" * len(title):<{width}}{space}║\n'  # underscore
    box += ''.join([f'║{space}{line:<{width}}{space}║\n' for line in lines])
    box += f'╚{"═" * (width + indent * 2)}╝'  # lower_border
    print(box)

if __name__ == '__main__':
    jogo = Jogo()
    baralho = Baralho()
    # baralho.embaralhar() # Voltar a embaralhar para o jogo funcionarnormalmente.
    # baralho.definirVira(baralho)
    # manilha = baralho.definirManilha()
    # baralho.definirManilhas(manilha)

    carta1 = 0
    carta2 = 0
    ganhador = 0

    nome = str(input("Nome Jogador 1: "))
    jogador1 = jogo.criarJogador(nome, baralho)

    nome = str(input("Nome Jogador 2: "))
    jogador2 = jogo.criarBot(nome, baralho)

    # limpar()

    while True:

        # print("\nCarta que virou: ")
        # baralho.printarVira()

        # print("\nManilhas: ")
        # baralho.printarManilhas()

        #Sorteio pra ver quem joga na primeira rodada
        # if jogador1.rodadas == 0 and jogador2.rodadas == 0:
        #     if jogador1.pontos == 0 and jogador2.pontos == 0:
        #         jogadores = ["jogador1", "jogador2"]
        #         sorteado = random.choice(jogadores)
        #         if sorteado == "jogador1":
        #             jogador1.primeiro = True
        #             jogador2.ultimo = True
        #         elif sorteado == "jogador2":
        #             jogador2.primeiro = True
        #             jogador1.ultimo = True
        # print(f"Sorteio pra ver quem joga na primeira rodada\n Ganhador: {sorteado}")
        jogador1.primeiro = True
        jogador2.ultimo = True
        print(f"Jogador 1 é mão")
        # baralho.printarManilhas()

        if jogador1.primeiro == True:
            print(f"\n<< {jogador1.nome} - Jogador 1 >>")
            
            jogador1.mostrarOpcoes()
            carta_escolhida = int(input(f"\n{jogador1.nome} Qual carta você quer jogar? "))
            carta_jogador_01 = jogador1.jogarCarta(carta_escolhida)
            # limpar()
            print(f"\n{jogador1.nome} jogou a carta: ")
            carta_jogador_01.printarCarta(carta_escolhida)
            
            print(f"\n<< {jogador2.nome} - Jogador 2 >>")
            if(jogador1.flor and jogador2.flor):
                print('Contraflor do bot')
                jogador2.rodadas += 6
            elif (jogador2.flor):
                jogador2.rodadas += 3
            jogador2.mostrarMao()
            # carta_escolhida = int(input(f"\n{jogador2.nome} Qual carta você quer jogar? "))
            carta_jogador_02 = jogador2.jogarCarta()
            # limpar()
            print(f"\n{jogador2.nome} jogou a carta: ")
            carta_jogador_02.printarCarta(carta_jogador_02)

        elif jogador2.primeiro == True:
            print(f"\n<< {jogador2.nome} - Jogador 2 >>")
            jogador2.mostrarMao()
            # carta_escolhida = int(input(f"\n{jogador2.nome} Qual carta você quer jogar? "))
            carta_jogador_02 = jogador2.jogarCarta()
            # limpar()
            print(f"\n{jogador2.nome} jogou a carta: ")
            carta_jogador_02.printarCarta(carta_jogador_02)

            print(f"\n<< {jogador1.nome} - Jogador 1 >>")
            jogador1.mostrarOpcoes()
            carta_escolhida = int(input(f"\n{jogador1.nome} Qual carta você quer jogar? "))
            carta_jogador_01 = jogador1.jogarCarta(carta_escolhida)
            # limpar()
            print(f"\n{jogador1.nome} jogou a carta: ")
            carta_jogador_01.printarCarta(carta_escolhida)
        else:
            print("Erro")

        # limpar()

        print(f"\n>> {jogador1.nome} jogou a carta: ")
        carta_jogador_01.printarCarta()
        print(f">> {jogador2.nome} jogou a carta: ")
        carta_jogador_02.printarCarta()

        carta1 = Carta(carta_jogador_01.retornarNumero(), carta_jogador_01.retornarNaipe())
        carta2 = Carta(carta_jogador_02.retornarNumero(), carta_jogador_02.retornarNaipe())

        print("\nCarta ganhadora: ")
        ganhador = jogo.verificarGanhador(carta1, carta2)
        jogo.quemJogaPrimeiro(jogador1, jogador2, carta1, carta2, ganhador)
        jogo.adicionarPonto(jogador1, jogador2, carta1, carta2, ganhador)

        if jogador1.pontos == 2:
            jogador1.adicionarRodada()
            print(f"\n{jogador1.nome} ganhou a rodada")
            reiniciarJogo()

        elif jogador2.pontos == 2:
            jogador2.adicionarRodada()
            print(f"\n{jogador2.nome} ganhou a rodada")
            reiniciarJogo()

        # Testar situação corrigida: empate em 2 rodadas, e o jogo trava sem possibidade de fazer mais nada.
        elif(not(jogador1.checaMao()) and not(jogador2.checaMao())):
            if jogador1.pontos > jogador2.pontos:
                jogador1.adicionarRodada()
                print(f"\n{jogador1.nome} ganhou a rodada")
                reiniciarJogo()

            elif jogador2.pontos > jogador1.pontos:
                jogador2.adicionarRodada()
                print(f"\n{jogador2.nome} ganhou a rodada")
                reiniciarJogo()

        border_msg(f"Jogador 1 - {jogador1.nome}: Venceu {jogador1.pontos} Rodada(s), {jogador1.rodadas} Pontos Acumulados\nJogador 2 - {jogador2.nome}: Venceu {jogador2.pontos} Rodada(s), {jogador2.rodadas} Pontos Acumulados")

        jogo.quemIniciaRodada(jogador1, jogador2)

        if jogador1.rodadas >= 12:
            print(f"\n{jogador1.nome} ganhou o jogo")
            break

        elif jogador2.rodadas >= 12:
            print(f"\n{jogador2.nome} ganhou o jogo")
            break

'''
To do:
- Implementar classificação das cartas [baixa, média, alta];
- Implementar envido;
- Implementar real envido;
- Implementar fata envido;
- Implementar negação do envido
- Implementar Truco;
- Implementar Retruco;
- Implementar negação do Truco;
- Implementar Flor;
- Implementar Contra-flor;
- Implementar Contra-flor e Resto;
'''