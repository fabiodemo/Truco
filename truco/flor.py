class Flor():

    def __init__(self):
        self.valor_flor = 3

    def pedir_flor(self, jogador1, jogador2):
        if (jogador1.flor and jogador2.flor):
            print("contraflor")
            self.pedir_contraflor()

        elif (jogador1.flor):
            jogador1.pontos += self.valor_flor
        
        elif (jogador2.flor):
            jogador2.pontos += self.valor_flor


    def pedir_contraflor(self, quem_pediu, jogador1, jogador2):
        self.valor_flor = 6
        jogador1_pontos = jogador1.calculaEnvido()
        jogador2_pontos = jogador2.calculaEnvido()
        if jogador1_pontos > jogador2_pontos:
            jogador1.pontos += self.valor_flor
        elif jogador2_pontos > jogador1_pontos:
            jogador1.pontos += self.valor_flor
        else:
            quem_pediu.pontos += self.valor_flor