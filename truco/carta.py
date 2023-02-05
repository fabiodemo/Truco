import itertools
from .pontos import MANILHA, CARTAS_VALORES, ENVIDO

class Carta():

    def __init__(self, numero, naipe):
        self.numero = numero
        self.naipe = naipe

    # def verificarCarta(self, carta_01, carta_02):
    #     if self.CARTAS_VALORES[str(carta_01.numero)] > self.CARTAS_VALORES[str(carta_02.numero)]:
    #         return carta_01
    #     elif self.CARTAS_VALORES[str(carta_01.retornar_numero())] < self.CARTAS_VALORES[str(carta_02.retornar_numero())]:
    #         return carta_02
    #     else:
    #         return "Empate"

    # def verificarCarta(self, carta_01, carta_02):
    #     print(1)
    #     if (str(carta_01.numero)+" de "+carta_01.naipe) in self.MANILHA and (str(carta_02.numero)+" de "+carta_02.naipe) in self.MANILHA:
    #         print(2)
    #         if self.MANILHA[str(carta_01.numero)+" de "+carta_01.naipe] > self.MANILHA[str(carta_02.numero)+" de "+carta_02.naipe]:
    #             return carta_01
    #             print(3)
    #         elif self.MANILHA[str(carta_02.numero)+" de "+carta_02.naipe] > self.MANILHA[str(carta_01.numero)+" de "+carta_01.naipe]:
    #             return carta_02
    #             print(4)
    #     elif (str(carta_01.numero)+" de "+carta_01.naipe) in self.MANILHA:
    #         return carta_01
    #         print(5)
    #     elif (str(carta_02.numero)+" de "+carta_02.naipe) in self.MANILHA:
    #         return carta_02
    #         print(6)
    #     else:
    #         if self.CARTAS_VALORES[str(carta_01.numero)] > self.CARTAS_VALORES[str(carta_02.numero)]:
    #             return carta_01
    #         elif self.CARTAS_VALORES[str(carta_01.retornar_numero())] < self.CARTAS_VALORES[str(carta_02.retornar_numero())]:
    #             return carta_02
    #         else:
    #             return "Empate"

    def verificar_carta_alta(self, carta_01, carta_02):
        if (str(carta_01.numero)+" de "+carta_01.naipe) in MANILHA and (str(carta_02.numero)+" de "+carta_02.naipe) in MANILHA:
            if MANILHA[str(carta_01.numero)+" de "+carta_01.naipe] > MANILHA[str(carta_02.numero)+" de "+carta_02.naipe]:
                return carta_01
            elif MANILHA[str(carta_02.numero)+" de "+carta_02.naipe] > MANILHA[str(carta_01.numero)+" de "+carta_01.naipe]:
                return carta_02
        elif (str(carta_01.numero)+" de "+carta_01.naipe) in MANILHA:
            print('in manilha')
            return carta_01
        elif (str(carta_02.numero)+" de "+carta_02.naipe) in MANILHA:
            print('in manilha')
            return carta_02
        else:
            if CARTAS_VALORES[str(carta_01.numero)] > CARTAS_VALORES[str(carta_02.numero)]:
                return carta_01
            else:
                return carta_02
        return carta_01
        
    def verificar_carta_baixa(self, carta_01, carta_02):
        if (str(carta_01.numero)+" de "+carta_01.naipe) in MANILHA and (str(carta_02.numero)+" de "+carta_02.naipe) in MANILHA:
            if MANILHA[str(carta_01.numero)+" de "+carta_01.naipe] < MANILHA[str(carta_02.numero)+" de "+carta_02.naipe]:
                return carta_01
            elif MANILHA[str(carta_02.numero)+" de "+carta_02.naipe] < MANILHA[str(carta_01.numero)+" de "+carta_01.naipe]:
                return carta_02
        elif (str(carta_01.numero)+" de "+carta_01.naipe) in MANILHA:
            return carta_02
        elif (str(carta_02.numero)+" de "+carta_02.naipe) in MANILHA:
            return carta_01
        else:
            if CARTAS_VALORES[str(carta_01.numero)] < CARTAS_VALORES[str(carta_02.numero)]:
                return carta_01
            else:
                return carta_02
        return carta_01

    def carta_manilha(self, carta):
        if (((carta.numero)+" de "+carta.naipe) in self.MANILHA):
            return True
        return False

    
    def retornar_pontos_carta(self, carta):
        if (str(carta.numero)+" de "+carta.naipe) in MANILHA:
            return MANILHA[str(carta.numero)+" de "+carta.naipe]
        else:
            return CARTAS_VALORES[str(carta.numero)]

    def classificar_carta(self, cartas):
        carta_alta = self.verificar_carta_alta(self.verificar_carta_alta(cartas[0], cartas[1]), cartas[2])
        carta_baixa = self.verificar_carta_baixa(self.verificar_carta_baixa(cartas[0], cartas[1]), cartas[2])
        lista_classificacao = ['', '', '']
        lista_pontos = ['', '', '']
        
        for i in range(len(lista_classificacao)):
            if carta_alta == cartas[i]: 
                lista_pontos[i] = self.retornar_pontos_carta(cartas[i])
                lista_classificacao[i] = 'Alta'
            
            if carta_baixa == cartas[i]: 
                lista_pontos[i] = self.retornar_pontos_carta(cartas[i])
                lista_classificacao[i] = 'Baixa'
            
            if not lista_classificacao[i]: 
                lista_pontos[i] = self.retornar_pontos_carta(cartas[i])
                lista_classificacao[i] = 'Media'


        return lista_pontos, lista_classificacao

    def exibir_carta(self, i=None):
        if i == None:
            i = ""
        if self.numero == 1 and self.naipe == 'Espadas':
            print(f"[{i}] ESPADÃO +")
        elif self.numero == 1 and self.naipe == 'Bastos':
            print(f"[{i}] BASTIÃO +")
        elif self.numero == 7 and self.naipe == 'Espadas':
            print(f"[{i}] Sete de espadas +")
        elif self.numero == 7 and self.naipe == 'Ouros':
            print(f"[{i}] Sete de Ouros +")
        else:
            print(f"[{i}] {self.numero} de {self.naipe}")
    
    def retornar_pontos_envido(self, carta):
        # print(carta.retornar_numero())
        return ENVIDO[str(carta.retornar_numero())]

    def retornar_numero(self):
        return self.numero
    
    def retornar_naipe(self):
        return self.naipe


