from .baralho import Baralho
from .carta import Carta
from .jogador import Jogador
from .jogo import Jogo
from .cbr import Cbr
from .interface import Interface
from .dados import Dados
from .truco import Truco
from .envido import Envido
from .flor import Flor
import random
import os


def reiniciarJogo():
    jogador1.resetar()
    jogador2.resetar()
    baralho.resetarBaralho()
    baralho.criarBaralho()
    # baralho.embaralhar()
    jogador1.criarMao(baralho)
    jogador2.criarMao(baralho)
    # jogo.resetarTrucoPontos()
    truco.resetar_pontos_truco()

def turno_do_humano(jogador2):
    carta_escolhida = -1
    while (carta_escolhida > len(jogador1.checaMao()) or int(carta_escolhida) <= 1):
        print(f"\n<< {jogador1.nome} - Jogador 1 >>")
        jogador1.mostrarOpcoes()
        carta_escolhida = int(input(f"\n{jogador1.nome} Qual carta você quer jogar? "))
        
        if (carta_escolhida < len(jogador1.checaMao()) and int(carta_escolhida) >= 0):
            carta_jogador_01 = jogador1.jogarCarta(carta_escolhida)
            # interface.limpar_tela()

            # print(f'carta escolhida {carta_escolhida} \n carta_jogador_01 {carta_jogador_01}')
            break

        elif (carta_escolhida == 4):
            chamou_truco = (truco.pedir_truco(1, jogador1, jogador2))
            print(f"temp: {chamou_truco}")
            if((chamou_truco) is False):
                print('pontos truco', truco.retornar_valor_aposta())
                return -1
                break
                # jogador1.adicionarRodada()

        elif (carta_escolhida == 5 and (len(jogador2.mao) == 3)):
            print('flor')
            flor.pedir_flor(jogador1, jogador2)
            interface.border_msg(f"Jogador 1 - {jogador1.nome}: {jogador1.pontos} Pontos Acumulados\nJogador 2 - {jogador2.nome}: {jogador2.pontos} Pontos Acumulados")

        elif (carta_escolhida == 6):
            print('envido')
            Envido.pedir_envido(jogador1, jogador1, jogador2)

        elif (carta_escolhida == 7):
            jogador2.pontos += 1
            return -1
        
        else:
            print('Selecione um valor válido!')

    carta1 = Carta(carta_jogador_01.retornarNumero(), carta_jogador_01.retornarNaipe())
    return carta1

def turno_do_bot(carta_jogador_01=None):
    # print(f"\n<< {jogador2.nome} - Jogador 2 >>")
    carta_jogador_02 = jogador2.jogarCarta(cbr, truco)
    # interface.limpar_tela()

    if carta_jogador_01:
        pass

    if(carta_jogador_02 is not None):
        carta2 = Carta(carta_jogador_02.retornarNumero(), carta_jogador_02.retornarNaipe())
    return carta2


jogo = Jogo()
baralho = Baralho()
baralho.embaralhar() # Voltar a embaralhar para o jogo funcionar normalmente.
cbr = Cbr()
interface = Interface()
dados = Dados()
truco = Truco()
flor = Flor()

truco_aceito = False
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
# interface.limpar_tela()
interface.mostrar_jogador_mao(jogador1.nome)

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

    # print(f'truco fugiu: {truco_fugiu}, truco aceito {truco_aceito}')
    if jogador1.primeiro == True:
        carta_jogador_01 = turno_do_humano(jogador2)
        if (carta_jogador_01 != -1):
            interface.mostrar_carta_jogada(jogador1.nome, carta_jogador_01)
            carta_jogador_02 = turno_do_bot(carta_jogador_01)
            if (carta_jogador_02 != -1):
                interface.mostrar_carta_jogada(jogador2.nome, carta_jogador_02)

    elif jogador2.primeiro == True:
        carta_jogador_02 = turno_do_bot(None)
        if (carta_jogador_02 != -1):
            interface.mostrar_carta_jogada(jogador2.nome, carta_jogador_02)
            carta_jogador_01 = turno_do_humano(jogador2)
            if (carta_jogador_01 != -1):
                interface.mostrar_carta_jogada(jogador1.nome, carta_jogador_01)
    
    
    if (carta_jogador_01 == -1 or carta_jogador_02 == -1):
        truco_fugiu = True
        if(carta_jogador_01 == -1):
            jogo.jogador_fugiu(jogador1, jogador1, jogador2, -1)
            interface.mostrar_placar_total_jogador_fugiu(jogador1, jogador1.nome, jogador1.pontos, jogador2.nome, jogador2.pontos)
        
        else:
            jogo.jogador_fugiu(jogador2, jogador1, jogador2)
            interface.mostrar_placar_total_jogador_fugiu(jogador2, jogador1.nome, jogador1.pontos, jogador2.nome, jogador2.pontos)
        
        reiniciarJogo()

    else:
        ganhador = jogo.verificarGanhador(carta_jogador_01, carta_jogador_02)
        jogo.quemJogaPrimeiro(jogador1, jogador2, carta_jogador_01, carta_jogador_02, ganhador)
        jogo.adicionarRodada(jogador1, jogador2, carta_jogador_01, carta_jogador_02, ganhador)

    if (jogador1.rodadas == 2 or jogador2.rodadas == 2):
        ocultar_pontos_ac = True
        if jogador1.rodadas == 2:
            jogador1.adicionarPontos(truco.retornar_valor_aposta())
            interface.mostrar_ganhador_rodada(jogador1.nome)
            reiniciarJogo()

        elif jogador2.rodadas == 2:
            jogador2.adicionarPontos(truco.retornar_valor_aposta())
            interface.mostrar_ganhador_rodada(jogador2.nome)
            reiniciarJogo()

        interface.mostrar_placar_total(jogador1.nome, jogador1.pontos, jogador2.nome, jogador2.pontos)

    # Testar situação corrigida: empate em 2 pontos, e o jogo trava sem possibidade de fazer mais nada.
    if(not(jogador1.checaMao()) and not(jogador2.checaMao()) or truco_fugiu is True):
        pontos_truco = truco.retornar_valor_aposta()
        ocultar_pontos_ac = True
        if truco_fugiu is True:
            print(f'pontos truco:: {pontos_truco} | {truco.retornar_valor_aposta()}')
            # jogador1.adicionarPontos(truco.retornar_valor_aposta())
            # interface.mostrar_ganhador_rodada(jogador1.nome)
            reiniciarJogo()
        
        elif jogador1.rodadas > jogador2.rodadas:
            jogador1.adicionarPontos(truco.retornar_valor_aposta())
            interface.mostrar_ganhador_rodada(jogador1.nome)
            reiniciarJogo()

        elif jogador2.rodadas > jogador1.rodadas:
            jogador2.adicionarPontos(truco.retornar_valor_aposta())
            interface.mostrar_ganhador_rodada(jogador2.nome)
            reiniciarJogo()
        
        interface.mostrar_placar_total(jogador1.nome, jogador1.pontos, jogador2.nome, jogador2.pontos)


    if (ocultar_pontos_ac is False):
        interface.mostrar_placar_rodadas(jogador1.nome, jogador1.rodadas, jogador2.nome, jogador2.rodadas)

    if jogador1.pontos >= 12:
        interface.mostrar_ganhador_jogo(jogador1.nome)
        break

    elif jogador2.pontos >= 12:
        interface.mostrar_ganhador_jogo(jogador2.nome)
        break
'''
To do:
- Arrumar bug do placar não mostrar rodadas
- Checar funcionamento do Truco/Envido
- Diferenciar flag -1 do fugiu_truco da flag de ir ao baralho
'''