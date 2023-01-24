
class Interface():
    pass

    def __init__(self):
        pass

    def border_msg(self, msg, indent=1, width=None, title=None):
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
  
    def limpar_tela(self):
        """Limpa a tela do usuário após determinado ponto da partida, necessário adaptar pro sistema operacional     utilizado"""
        # Caso rodar em Linux
        os.system("clear")
        # Caso rodar em Windows
        # os.system("cls")

    def mostrar_carta_jogada(self, jogador, carta):
        print(f"\n{jogador.nome} jogou a carta: ")
        carta.printarCarta()

    def mostrar_ganhador_rodada(self, jogador):
        print(f"\n{jogador.nome} ganhou a rodada")

    def mostrar_placar_total(self, jogador1, jogador2):
        self.border_msg(f"Jogador 1 - {jogador1.nome}: {jogador1.pontos} Pontos Acumulados\nJogador 2 - {jogador2.nome}: {jogador2.pontos} Pontos Acumulados", title='Pontuação Total')

    def mostrar_ganhador_jogo(self, jogador):
        print(f"\n{jogador.nome} ganhou o jogo")
    
    def mostrar_pediu_truco(self, jogador):
        print(f'{jogador.nome} pediu truco e o pedido já foi aceito, escolha outra jogada!')