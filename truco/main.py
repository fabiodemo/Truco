from baralho import Baralho
from carta import Carta
from jogador import Jogador
from jogo import Jogo
from cbr import Cbr
import random
import os

def reiniciarJogo():
    jogador1.resetar()
    jogador2.resetar()
    baralho.resetarBaralho()
    baralho.criarBaralho()
    baralho.embaralhar()
    jogador1.criarMao(baralho)
    jogador2.criarMao(baralho)
    jogo.resetarTrucoPontos()

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

def pedirTruco():
    if(jogador1.pediuTruco is not True and jogador2.avaliarTruco(cbr)):
        jogador1.pediuTruco = True
        jogador2.pediuTruco = False
        return True
    
    elif (jogador1.pediuTruco is True):
        print('Jogador pediu truco e o pedido foi aceito, escolha outra jogada!')

    elif (jogador2.pediuTruco is True and jogador1.pediuTruco is False):
        jogador2.pediuTruco = True
        temp = -1
        while (temp != 0 and temp != 1):
            temp = int(input('Jogador 2 pediu truco\n[0] Fugir\n[1] Aceitar'))
        
        if (temp == 0):
            return False

        if (temp == 1):
            jogador1.pediuTruco = True
            jogador2.pediuTruco = False
            return True

    else:
        print('Jogador negou o truco!')
        return False

def aumentarTruco(quemPediu):
    if(quemPediu == jogador1):
        if(jogador2.pediuTruco == True):
            opcao = jogador2.avaliarAumentarTruco()
            
            if(opcao == 0):
                return
            
            elif(opcao == 1):
                return
            
            elif(opcao == 2):
                return
            
            return jogador2.avaliarTruco(cbr)
    
    elif (jogador1.pediuTruco == True):
        opcao = -1
        while(opcao < 0 or opcao > 2):
            print(f'[0] Aceitar\n[1] Fugir\n[2] Aumentar')
            opcao = int(input(f"\n{jogador2.nome} Qual opção você deseja? "))
            
            if(opcao == 0):
                return
                
            elif(opcao == 1):
                return
                
            elif(opcao == 2):
                return

def jogadasHumanas():
    carta_escolhida = 6
    while (carta_escolhida > len(jogador1.checaMao()) or int(carta_escolhida) <= 1):
        print(f"\n<< {jogador1.nome} - Jogador 1 >>")
        jogador1.mostrarOpcoes()
        carta_escolhida = int(input(f"\n{jogador1.nome} Qual carta você quer jogar? "))
        
        if (carta_escolhida < len(jogador1.checaMao()) and int(carta_escolhida) >= 0):
            carta_jogador_01 = jogador1.jogarCarta(carta_escolhida)
            # limpar()
            print(f"\n{jogador1.nome} jogou a carta: ")
            carta_jogador_01.printarCarta(carta_escolhida)
            # print(f'carta escolhida {carta_escolhida} \n carta_jogador_01 {carta_jogador_01}')
            pontos_truco = jogo.retornaTrucoPontos()
            break

        elif (carta_escolhida == 4):
            if((jogador1.pediuTruco is False) and (pedirTruco())):
                truco_aceito = jogo.trucoAceito(True)
                pontos_truco = jogo.retornaTrucoPontos()

            else:
                truco_fugiu = True
                truco_aceito = jogo.trucoAceito(False)
                print('pontos truco', jogo.retornaTrucoPontos())
                pontos_truco = jogo.retornaTrucoPontos()
                break
                # jogador1.adicionarRodada()

        elif (carta_escolhida == 5 and len(jogador2.mao) == 3):
            print('flor')
            if (jogador1.flor and jogador2.flor):
                print('Contraflor do bot')
                jogador2.pontos += 6
            elif (jogador1.flor):
                jogador1.pontos += 3
            elif (jogador2.flor):
                jogador2.pontos += 3
            border_msg(f"Jogador 1 - {jogador1.nome}: {jogador1.pontos} Pontos Acumulados\nJogador 2 - {jogador2.nome}: {jogador2.pontos} Pontos Acumulados")

        elif (carta_escolhida == 6):
            print('envido')
        
        else:
            print('Selecione um valor válido!')

    carta1 = Carta(carta_jogador_01.retornarNumero(), carta_jogador_01.retornarNaipe())
    return carta1

def chamarJogadasBot(carta_jogador_01):
    print(f"\n<< {jogador2.nome} - Jogador 2 >>")
    carta_jogador_02 = jogador2.jogarCarta(cbr)
    # limpar()

    if carta_jogador_01:
        print(1)

    print(f"\n{jogador2.nome} jogou a carta: ")
    carta2 = Carta(carta_jogador_02.retornarNumero(), carta_jogador_02.retornarNaipe())
    carta_jogador_02.printarCarta(carta2)

    return carta2

if __name__ == '__main__':
    jogo = Jogo()
    baralho = Baralho()
    baralho.embaralhar() # Voltar a embaralhar para o jogo funcionarnormalmente.
    cbr = Cbr()

    truco_aceito = False
    truco_fugiu = False
    pontos_truco = 0
    carta_jogador_01 = 0
    carta_jogador_02 = 0
    ganhador = 0

    nome = str(input("Nome Jogador 1: "))
    jogador1 = jogo.criarJogador(nome, baralho)
    nome = str(input("Nome Jogador 2 (Bot): "))
    jogador2 = jogo.criarBot(nome, baralho)
    jogador1.primeiro = True
    jogador2.ultimo = True
    # limpar()
    print(f"Jogador 1 é mão")

    while True:
        truco_fugiu = False
        ocultar_pontos_ac = False
        # jogo.resetarTrucoPontos()
        #Sorteio pra ver quem joga na primeira rodada
        # if jogador1.pontos == 0 and jogador2.pontos == 0:
        #     if jogador1.rodadas == 0 and jogador2.rodadas == 0:
        #         jogadores = ["jogador1", "jogador2"]
        #         sorteado = random.choice(jogadores)
        #         if sorteado == "jogador1":
        #             jogador1.primeiro = True
        #             jogador2.ultimo = True
        #         elif sorteado == "jogador2":
        #             jogador2.primeiro = True
        #             jogador1.ultimo = True
        # print(f"Sorteio pra ver quem joga na primeira rodada\n Ganhador: {sorteado}")

        print(f'truco fugiu: {truco_fugiu}, truco aceito {truco_aceito}')
        if jogador1.primeiro == True:
            carta_jogador_01 = jogadasHumanas()
            carta_jogador_02 = chamarJogadasBot(carta_jogador_01)

        elif jogador2.primeiro == True:
            carta_jogador_02 = chamarJogadasBot(None)
            carta_jogador_01 = jogadasHumanas()

        if (truco_fugiu is False):
            # carta2 = chamarJogadasBot(carta_jogador_01)
            ganhador = jogo.verificarGanhador(carta_jogador_01, carta_jogador_02)
            print("\nCarta ganhadora: ")
            jogo.quemJogaPrimeiro(jogador1, jogador2, carta_jogador_01, carta_jogador_02, ganhador)
            jogo.adicionarRodada(jogador1, jogador2, carta_jogador_01, carta_jogador_02, ganhador)

        if (jogador1.rodadas == 2 or jogador2.rodadas == 2):
            ocultar_pontos_ac = True
            if jogador1.rodadas == 2:
                jogador1.adicionarPontos(jogo.retornaTrucoPontos())
                print(f"\n{jogador1.nome} ganhou a rodada")
                reiniciarJogo()

            elif jogador2.rodadas == 2:
                jogador2.adicionarPontos(jogo.retornaTrucoPontos())
                print(f"\n{jogador2.nome} ganhou a rodada")
                reiniciarJogo()

            print(jogador1.pontos)
            border_msg(f"Jogador 1 - {jogador1.nome}: {jogador1.pontos} Pontos Acumulados\nJogador 2 - {jogador2.nome}: {jogador2.pontos} Pontos Acumulados")

        # Testar situação corrigida: empate em 2 pontos, e o jogo trava sem possibidade de fazer mais nada.
        if(not(jogador1.checaMao()) and not(jogador2.checaMao()) or truco_fugiu is True):
            pontos_truco = jogo.retornaTrucoPontos()
            ocultar_pontos_ac = True
            if truco_fugiu is True:
                print(f'pontos truco:: {pontos_truco} | {jogo.retornaTrucoPontos()}')
                jogador1.adicionarPontos(jogo.retornaTrucoPontos())
                print(f"\n{jogador1.nome} ganhou a rodada")
                reiniciarJogo()
            
            elif jogador1.rodadas > jogador2.rodadas:
                jogador1.adicionarPontos(jogo.retornaTrucoPontos())
                print(f"\n{jogador1.nome} ganhou a rodada")
                reiniciarJogo()

            elif jogador2.rodadas > jogador1.rodadas:
                jogador2.adicionarPontos(jogo.retornaTrucoPontos())
                print(f"\n{jogador2.nome} ganhou a rodada")
                reiniciarJogo()
            
            border_msg(f"Jogador 1 - {jogador1.nome}: {jogador1.pontos} Pontos Acumulados\nJogador 2 - {jogador2.nome}: {jogador2.pontos} Pontos Acumulados")

        if (ocultar_pontos_ac is False):
            border_msg(f"Jogador 1 - {jogador1.nome}: Venceu {jogador1.rodadas} Rodada(s)\nJogador 2 - {jogador2.nome}: Venceu {jogador2.rodadas} Rodada(s)")

        if jogador1.pontos >= 12:
            print(f"\n{jogador1.nome} ganhou o jogo")
            break

        elif jogador2.pontos >= 12:
            print(f"\n{jogador2.nome} ganhou o jogo")
            break
'''
To do:
- Implementar classificação das cartas para o bot;
- Implementar envido;
- Implementar real envido;
- Implementar falta envido;
- Implementar negação do envido
- Checar funcionamento do Truco
'''