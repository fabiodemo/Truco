from pontos import MANILHA, CARTAS_VALORES

class Carta():

    def __init__(self, numero, naipe):
        self.numero = numero
        self.naipe = naipe

    def verificarCarta(self, carta_jogador_01, carta_jogador_02):
        if self.CARTAS_VALORES[str(carta_jogador_01.numero)] > self.CARTAS_VALORES[str(carta_jogador_02.numero)]:
            return carta_jogador_01
        elif self.CARTAS_VALORES[str(carta_jogador_01.retornarNumero())] < self.CARTAS_VALORES[str(carta_jogador_02.retornarNumero())]:
            return carta_jogador_02
        else:
            return "Empate"

    def verificarManilha(self, carta_jogador_01, carta_jogador_02):
        print(1)
        if (str(carta_jogador_01.numero)+" de "+carta_jogador_01.naipe) in self.MANILHA and (str(carta_jogador_02.numero)+" de "+carta_jogador_02.naipe) in self.MANILHA:
            print(2)
            if self.MANILHA[str(carta_jogador_01.numero)+" de "+carta_jogador_01.naipe] > self.MANILHA[str(carta_jogador_02.numero)+" de "+carta_jogador_02.naipe]:
                return carta_jogador_01
                print(3)
            elif self.MANILHA[str(carta_jogador_02.numero)+" de "+carta_jogador_02.naipe] > self.MANILHA[str(carta_jogador_01.numero)+" de "+carta_jogador_01.naipe]:
                return carta_jogador_02
                print(4)
        elif (str(carta_jogador_01.numero)+" de "+carta_jogador_01.naipe) in self.MANILHA:
            return carta_jogador_01
            print(5)
        elif (str(carta_jogador_02.numero)+" de "+carta_jogador_02.naipe) in self.MANILHA:
            return carta_jogador_02
            print(6)
        else:
            print("NOnao")
            return None

    def printarCarta(self, i=None):
        if i == None:
            i = ""
        if self.numero == 1 and self.naipe == 'Espadas':
            print(f"[{i}] ESPADÃO")
        elif self.numero == 1 and self.naipe == 'Bastos':
            print(f"[{i}] BASTIÃO")
        elif self.numero == 7 and self.naipe == 'Espadas':
            print(f"[{i}] Siete de espadas")
        elif self.numero == 7 and self.naipe == 'Ouros':
            print(f"[{i}] Siete de Ouros")
        else:
            print(f"[{i}] {self.numero} de {self.naipe}")

    def retornarNumero(self):
        return self.numero
    
    def retornarNaipe(self):
        return self.naipe