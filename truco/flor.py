class Flor():

    def __init__(self):
        self.valor_flor = 3
        self.quem_pediu_flor = 0
        self.quem_pediu_contraflor = 0
        self.quem_pediu_contraflor_resto = 0

    def pedir_flor(self, quem_pediu, jogador1, jogador2):
        if (quem_pediu == jogador2):
            jogador2.pediu_flor = True
            
        if (jogador1.flor and jogador2.flor):
            print("contraflor")
            self.pedir_contraflor()

        elif (jogador1.flor):
            jogador1.pontos += self.valor_flor
        
        elif (jogador2.flor):
            jogador2.pontos += self.valor_flor


    def pedir_contraflor(self, quem_pediu, jogador1, jogador2):
        self.valor_flor = 6
        jogador1_pontos = jogador1.retorna_pontos_envido()
        jogador2_pontos = jogador2.retorna_pontos_envido()
        if jogador1_pontos > jogador2_pontos:
            jogador1.pontos += self.valor_flor
        elif jogador2_pontos > jogador1_pontos:
            jogador2.pontos += self.valor_flor
        else:
            quem_pediu.pontos += self.valor_flor

    def pedir_contraflor_resto(self, quem_pediu, jogador1, jogador2):
        jogador1_pontos = jogador1.retorna_pontos_envido()
        jogador2_pontos = jogador2.retorna_pontos_envido()
        if jogador1_pontos > jogador2_pontos:
            jogador1.pontos += 12 - jogador2.pontos
        elif jogador2_pontos > jogador1_pontos:
            jogador2.pontos += 12 - jogador1.pontos
        else:
            quem_pediu.pontos += self.valor_flor

    def resetar_flor(self):
        self.valor_flor = 3
        self.quem_pediu_flor = 0
        self.quem_pediu_contraflor = 0
        self.quem_pediu_contraflor_resto = 0
