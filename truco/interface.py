import os

class Interface():
    def __init__(self):
        pass


    def border_msg(self, msg, indent=1, width=None, title=None):
        """Exibe uma caixa em torno de determinada mensagem."""
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
  

    def limpar_tela(self):
        """Limpa a tela do usuário após determinado ponto da partida, sendo necessário adaptar pro sistema operacional utilizado."""
        # Caso rodar em Linux
        os.system("clear")
        # Caso rodar em Windows
        # os.system("cls")


    def mostrar_carta_jogada(self, jogador, carta):
        """Exibe a última carta jogada."""
        print(f"\n{jogador} jogou a carta: ")
        carta.exibir_carta()


    def mostrar_ganhador_rodada(self, jogador):
        """Exibe quem ganhou a rodada."""
        print(f"\n{jogador} ganhou a rodada")


    def mostrar_placar_total_jogador_fugiu(self, jogador_fugiu, jogador1, jogador1_pontos, jogador2, jogador2_pontos):
        """Exibe um aviso de que o jogador fugiu e o placar total,"""
        print('jogador {jogador_fugiu.nome} fugiu!')
        self.mostrar_placar_total(jogador1, jogador1_pontos, jogador2, jogador2_pontos)


    def mostrar_placar_total(self, jogador1, jogador1_pontos, jogador2, jogador2_pontos):
        """Exibe o placar total da partida."""
        self.border_msg(f"Jogador 1 - {jogador1}: {jogador1_pontos} Pontos Acumulados\nJogador 2 - {jogador2}: {jogador2_pontos} Pontos Acumulados", title='Pontuação Total')


    def mostrar_placar_rodadas(self, jogador1, jogador1_pontos, jogador2, jogador2_pontos):
        """Exibe o placar entre cada uma das rodadas."""
        self.border_msg(f"Jogador 1 - {jogador1}: Venceu {jogador1_pontos} Rodada(s)\nJogador 2 - {jogador2}: Venceu {jogador2_pontos} Rodada(s)", title='Rodadas da Partida Atual')


    def mostrar_ganhador_jogo(self, jogador):
        """Exibe o jogador que obteu a pontuação necessária para vencer o jogo."""
        print(f"\n{jogador} ganhou o jogo")
    

    def mostrar_pediu_truco(self, jogador):
        """Exibe aviso de que o pedido de truco já foi realizado."""
        print(f'{jogador} pediu truco e o pedido já foi aceito, escolha outra jogada!')


    def mostrar_jogador_mao(self, jogador):
        """Exibe as possibilidades de jogada para o jogador."""
        print(f"Jogador 1 é mão")


    def desenharCarta(self, s):
        """Exibe/desenha a carta jogada."""
        l_mostrar_carta = [] 
        l_mostrar_carta.append("┌─────────┐")
        l_mostrar_carta.append("│{}{}. . .│")
        l_mostrar_carta.append("│. . . . .│")
        l_mostrar_carta.append("│. . . . .│")
        l_mostrar_carta.append("│. . {}. .│")
        l_mostrar_carta.append("│. . . . .│")
        l_mostrar_carta.append("│. . . . .│")
        l_mostrar_carta.append("│. . .{}{}│")
        l_mostrar_carta.append("└─────────┘")

        x = ("│.", s[:1], ". . . .│")
        l_mostrar_carta[1] = "".join(x)

        x = ("│. . . .", s[:1], ".│")
        l_mostrar_carta[7] = "".join(x)
        
        #  ["Espadas", "Ouros", "Copas", "Espadas"]
        if "OUROS" in s:
            l_mostrar_carta[4] = "│. . ♦ . .│"
        if "BASTOS" in s:
            l_mostrar_carta[4] = "│. . ♣ . .│"
        if "COPAS" in s:
            l_mostrar_carta[4] = "│. . ♥ . .│"
        if "ESPADAS" in s:
            l_mostrar_carta[4] = "│. . ♠ . .│"

        return l_mostrar_carta