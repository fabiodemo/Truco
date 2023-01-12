import itertools
from pontos import MANILHA, CARTAS_VALORES

class Carta():

    def __init__(self, numero, naipe):
        self.numero = numero
        self.naipe = naipe

    # def verificarCarta(self, carta_jogador_01, carta_jogador_02):
    #     if self.CARTAS_VALORES[str(carta_jogador_01.numero)] > self.CARTAS_VALORES[str(carta_jogador_02.numero)]:
    #         return carta_jogador_01
    #     elif self.CARTAS_VALORES[str(carta_jogador_01.retornarNumero())] < self.CARTAS_VALORES[str(carta_jogador_02.retornarNumero())]:
    #         return carta_jogador_02
    #     else:
    #         return "Empate"

    # def verificarCarta(self, carta_jogador_01, carta_jogador_02):
    #     print(1)
    #     if (str(carta_jogador_01.numero)+" de "+carta_jogador_01.naipe) in self.MANILHA and (str(carta_jogador_02.numero)+" de "+carta_jogador_02.naipe) in self.MANILHA:
    #         print(2)
    #         if self.MANILHA[str(carta_jogador_01.numero)+" de "+carta_jogador_01.naipe] > self.MANILHA[str(carta_jogador_02.numero)+" de "+carta_jogador_02.naipe]:
    #             return carta_jogador_01
    #             print(3)
    #         elif self.MANILHA[str(carta_jogador_02.numero)+" de "+carta_jogador_02.naipe] > self.MANILHA[str(carta_jogador_01.numero)+" de "+carta_jogador_01.naipe]:
    #             return carta_jogador_02
    #             print(4)
    #     elif (str(carta_jogador_01.numero)+" de "+carta_jogador_01.naipe) in self.MANILHA:
    #         return carta_jogador_01
    #         print(5)
    #     elif (str(carta_jogador_02.numero)+" de "+carta_jogador_02.naipe) in self.MANILHA:
    #         return carta_jogador_02
    #         print(6)
    #     else:
    #         if self.CARTAS_VALORES[str(carta_jogador_01.numero)] > self.CARTAS_VALORES[str(carta_jogador_02.numero)]:
    #             return carta_jogador_01
    #         elif self.CARTAS_VALORES[str(carta_jogador_01.retornarNumero())] < self.CARTAS_VALORES[str(carta_jogador_02.retornarNumero())]:
    #             return carta_jogador_02
    #         else:
    #             return "Empate"

    def verificarCartaAlta(self, carta_jogador_01, carta_jogador_02):
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
            elif CARTAS_VALORES[str(carta_jogador_01.retornarNumero())] < CARTAS_VALORES[str(carta_jogador_02.retornarNumero())]:
                return carta_jogador_02
            else:
                return None
        
    def verificarCartaBaixa(self, carta_jogador_01, carta_jogador_02):
        if (str(carta_jogador_01.numero)+" de "+carta_jogador_01.naipe) in MANILHA and (str(carta_jogador_02.numero)+" de "+carta_jogador_02.naipe) in MANILHA:
            if MANILHA[str(carta_jogador_01.numero)+" de "+carta_jogador_01.naipe] < MANILHA[str(carta_jogador_02.numero)+" de "+carta_jogador_02.naipe]:
                return carta_jogador_01
            elif MANILHA[str(carta_jogador_02.numero)+" de "+carta_jogador_02.naipe] < MANILHA[str(carta_jogador_01.numero)+" de "+carta_jogador_01.naipe]:
                return carta_jogador_02
        elif (str(carta_jogador_01.numero)+" de "+carta_jogador_01.naipe) in MANILHA:
            return carta_jogador_01
        elif (str(carta_jogador_02.numero)+" de "+carta_jogador_02.naipe) in MANILHA:
            return carta_jogador_02
        else:
            if CARTAS_VALORES[str(carta_jogador_01.numero)] <= CARTAS_VALORES[str(carta_jogador_02.numero)]:
                return carta_jogador_01
            elif CARTAS_VALORES[str(carta_jogador_01.retornarNumero())] > CARTAS_VALORES[str(carta_jogador_02.retornarNumero())]:
                return carta_jogador_02
            else:
                return None

    def cartaManilha(self, carta):
        if(((carta.numero)+" de "+carta.naipe) in self.MANILHA):
            return True
        return False

    def classificarCarta(self, cartas):
        carta_alta = self.verificarCartaAlta(self.verificarCartaAlta(cartas[0], cartas[1]), cartas[2])
        carta_baixa = self.verificarCartaBaixa(self.verificarCartaBaixa(cartas[0], cartas[1]), cartas[2])
        lista_classificacao = ['', '', '']
        
        for i in range(len(lista_classificacao)):
            if carta_alta == cartas[i]: lista_classificacao[i] = 'Alta'
            if carta_baixa == cartas[i]: lista_classificacao[i] = 'Baixa'
            if not lista_classificacao[i]: lista_classificacao[i] = 'Média'

        return lista_classificacao

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

    def desenharCarta(self, s):
        pixel_mostrar_carta = [] 
        pixel_mostrar_carta.append("┌─────────┐")
        pixel_mostrar_carta.append("│{}{}. . .│")
        pixel_mostrar_carta.append("│. . . . .│")
        pixel_mostrar_carta.append("│. . . . .│")
        pixel_mostrar_carta.append("│. . {}. .│")
        pixel_mostrar_carta.append("│. . . . .│")
        pixel_mostrar_carta.append("│. . . . .│")
        pixel_mostrar_carta.append("│. . .{}{}│")
        pixel_mostrar_carta.append("└─────────┘")

        x = ("│.", s[:1], ". . . .│")
        pixel_mostrar_carta[1] = "".join(x)

        x = ("│. . . .", s[:1], ".│")
        pixel_mostrar_carta[7] = "".join(x)
        
        #  ["Espadas", "Ouros", "Copas", "Espadas"]
        if "Ouros" in s:
            pixel_mostrar_carta[4] = "│. . ♦ . .│"
        if "Paus" in s:
            pixel_mostrar_carta[4] = "│. . ♣ . .│"
        if "Copas" in s:
            pixel_mostrar_carta[4] = "│. . ♥ . .│"
        if "Espadas" in s:
            pixel_mostrar_carta[4] = "│. . ♠ . .│"

        return pixel_mostrar_carta
