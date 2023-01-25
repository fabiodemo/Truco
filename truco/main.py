from baralho import Baralho
from carta import Carta
from jogador import Jogador
from jogo import Jogo
from cbr import Cbr
from interface import Interface
from dados import Dados
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
            # interface.limpar_tela()

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
            interface.border_msg(f"Jogador 1 - {jogador1.nome}: {jogador1.pontos} Pontos Acumulados\nJogador 2 - {jogador2.nome}: {jogador2.pontos} Pontos Acumulados")

        elif (carta_escolhida == 6):
            print('envido')
        
        else:
            print('Selecione um valor válido!')

    carta1 = Carta(carta_jogador_01.retornarNumero(), carta_jogador_01.retornarNaipe())
    return carta1

def chamarJogadasBot(carta_jogador_01=None):
    # print(f"\n<< {jogador2.nome} - Jogador 2 >>")
    carta_jogador_02 = jogador2.jogarCarta(cbr)
    # interface.limpar_tela()

    if carta_jogador_01:
        pass

    carta2 = Carta(carta_jogador_02.retornarNumero(), carta_jogador_02.retornarNaipe())
    return carta2

if __name__ == '__main__':
    jogo = Jogo()
    baralho = Baralho()
    baralho.embaralhar() # Voltar a embaralhar para o jogo funcionar normalmente.
    cbr = Cbr()
    interface = Interface()
    dados = Dados()

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
    # interface.limpar_tela()
    interface.mostrar_jogador_mao(jogador1.nome)

    while True:
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
            carta_jogador_01 = jogadasHumanas()
            interface.mostrar_carta_jogada(jogador1.nome)
            carta_jogador_01.printarCarta()
            carta_jogador_02 = chamarJogadasBot(carta_jogador_01)
            interface.mostrar_carta_jogada(jogador2.nome)
            carta_jogador_02.printarCarta()

        elif jogador2.primeiro == True:
            carta_jogador_02 = chamarJogadasBot(None)
            interface.mostrar_carta_jogada(jogador2.nome)
            carta_jogador_02.printarCarta()
            carta_jogador_01 = jogadasHumanas()
            interface.mostrar_carta_jogada(jogador1.nome)
            carta_jogador_01.printarCarta()
        
        if (truco_fugiu is False):
            ganhador = jogo.verificarGanhador(carta_jogador_01, carta_jogador_02)
            jogo.quemJogaPrimeiro(jogador1, jogador2, carta_jogador_01, carta_jogador_02, ganhador)
            jogo.adicionarRodada(jogador1, jogador2, carta_jogador_01, carta_jogador_02, ganhador)

        if (jogador1.rodadas == 2 or jogador2.rodadas == 2):
            ocultar_pontos_ac = True
            if jogador1.rodadas == 2:
                jogador1.adicionarPontos(jogo.retornaTrucoPontos())
                interface.mostrar_ganhador_rodada(jogador1.nome)
                reiniciarJogo()

            elif jogador2.rodadas == 2:
                jogador2.adicionarPontos(jogo.retornaTrucoPontos())
                interface.mostrar_ganhador_rodada(jogador2.nome)
                reiniciarJogo()

            interface.mostrar_placar_total(jogador1.nome, jogador1.pontos, jogador2.nome, jogador2.pontos)

        # Testar situação corrigida: empate em 2 pontos, e o jogo trava sem possibidade de fazer mais nada.
        if(not(jogador1.checaMao()) and not(jogador2.checaMao()) or truco_fugiu is True):
            pontos_truco = jogo.retornaTrucoPontos()
            ocultar_pontos_ac = True
            if truco_fugiu is True:
                print(f'pontos truco:: {pontos_truco} | {jogo.retornaTrucoPontos()}')
                jogador1.adicionarPontos(jogo.retornaTrucoPontos())
                interface.mostrar_ganhador_rodada(jogador1.nome)
                reiniciarJogo()
            
            elif jogador1.rodadas > jogador2.rodadas:
                jogador1.adicionarPontos(jogo.retornaTrucoPontos())
                interface.mostrar_ganhador_rodada(jogador1.nome)
                reiniciarJogo()

            elif jogador2.rodadas > jogador1.rodadas:
                jogador2.adicionarPontos(jogo.retornaTrucoPontos())
                interface.mostrar_ganhador_rodada(jogador2.nome)
                reiniciarJogo()
            
            interface.mostrar_placar_total(jogador1.nome, jogador1.pontos, jogador2.nome, jogador2.pontos)


        if (ocultar_pontos_ac is False):
            interface.mostrar_placar_rodadas(jogador1.nome, jogador1.pontos, jogador2.nome, jogador2.pontos)

        if jogador1.pontos >= 12:
            interface.mostrar_ganhador_jogo(jogador1.nome)
            break

        elif jogador2.pontos >= 12:
            interface.mostrar_ganhador_jogo(jogador2.nome)
            break
'''
To do:
- Implementar envido;
- Implementar real envido;
- Implementar falta envido;
- Implementar Negação do envido
- Checar funcionamento do Truco
'''