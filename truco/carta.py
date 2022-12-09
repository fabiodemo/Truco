class Carta():

    CARTAS_VALORES = {
        "3": 10,
        "2": 9,
        "1": 8,
        "12": 7,
        "11": 6,
        "10": 5,
        "7": 4,
        "6": 3,
        "5": 2,
        "4": 1
    }

    NAIPES_VALORES = {
        "Espadas": 4,
        "Ouros": 3,
        "Copas": 2,
        "Bastos": 1
    }

    MANILHA = {
        "1 de Espadas": 14,
        "1 de Bastos": 13,
        "7 de Espadas": 12,
        "7 de Ouros": 11
    }

    def __init__(self, numero, naipe):
        self.numero = numero
        self.naipe = naipe

    def verificarCarta(self, carta_jogador_01, carta_jogador_02):
        if verificarManilha(carta_jogador_01, carta_jogador_02) is None:
            if self.CARTAS_VALORES[str(carta_jogador_01.numero)] > self.CARTAS_VALORES[str(carta_jogador_02.numero)]:
                return carta_jogador_01
            elif self.CARTAS_VALORES[str(carta_jogador_01.retornarNumero())] < self.CARTAS_VALORES[str(carta_jogador_02.retornarNumero())]:
                return carta_jogador_02
            else:
                return "Empate"
        else:
            return verificarManilha(carta_jogador_01, carta_jogador_02)

    def verificarManilha(self, carta_jogador_01, carta_jogador_02):
        if self.MANILHA[carta_jogador_01.numero+" de "+carta_jogador_01.naipe] and self.MANILHA[carta_jogador_02.numero+" de "+carta_jogador_02.naipe] in MANILHA:
            if self.MANILHA[carta_jogador_01.numero+" de "+carta_jogador_01.naipe] > self.MANILHA[carta_jogador_02.numero+" de "+carta_jogador_02.naipe]:
                return carta_jogador_01
            elif self.MANILHA[carta_jogador_02.numero+" de "+carta_jogador_02.naipe] > self.MANILHA[carta_jogador_01.numero+" de "+carta_jogador_01.naipe]:
                return carta_jogador_02
        elif self.MANILHA[carta_jogador_01.numero+" de "+carta_jogador_01.naipe]:
            return carta_jogador_01
        elif self.MANILHA[carta_jogador_02.numero+" de "+carta_jogador_02.naipe]:
            return carta_jogador_02
        else:
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