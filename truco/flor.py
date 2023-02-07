class Flor():
    def __init__(self):
        self.valor_flor = 3
        self.quem_pediu_flor = 0
        self.quem_pediu_contraflor = 0
        self.quem_pediu_contraflor_resto = 0
        self.quem_venceu_flor = 0


    def pedir_flor(self, quem_pediu, jogador1, jogador2):
        if (quem_pediu == 2):
            jogador2.pediu_flor = True
        else:
            jogador1.pediu_flor = True
            
        if (jogador1.flor and jogador2.flor):
            print("contraflor")
            if (jogador2.pontos < int((jogador1.pontos/1.5))):
                self.pedir_contraflor_resto(2, jogador1, jogador2)
            else: 
                self.pedir_contraflor(2, jogador1, jogador2)
            
            return

        elif (jogador1.flor):
            jogador1.pontos += self.valor_flor
            self.quem_venceu_flor = 1
        
        elif (jogador2.flor):
            jogador2.pontos += self.valor_flor
            self.quem_venceu_flor = 2


    def pedir_contraflor(self, quem_pediu, jogador1, jogador2):
        self.valor_flor = 6
        jogador1_pontos = jogador1.retorna_pontos_envido()
        jogador2_pontos = jogador2.retorna_pontos_envido()

        if jogador1_pontos > jogador2_pontos:
            jogador1.pontos += self.valor_flor
            self.quem_venceu_flor = 1

        elif jogador2_pontos > jogador1_pontos:
            jogador2.pontos += self.valor_flor
            self.quem_venceu_flor = 2

        else:
            jogador1.pontos += self.valor_flor
            self.quem_venceu_flor = 1


    def pedir_contraflor_resto(self, quem_pediu, jogador1, jogador2):
        jogador1_pontos = jogador1.retorna_pontos_envido()
        jogador2_pontos = jogador2.retorna_pontos_envido()

        if (quem_pediu == 1):
            self.valor_envido = self.valor_flor
            
        else:
            self.valor_envido = self.valor_flor

        if jogador1_pontos > jogador2_pontos:
            jogador1.pontos += self.valor_flor
            self.quem_venceu_flor = 1

        elif jogador2_pontos > jogador1_pontos:
            jogador2.pontos += self.valor_flor
            self.quem_venceu_flor = 2

        else:
            jogador1.pontos += self.valor_flor
            self.quem_venceu_flor = 1


    def resetar_flor(self):
        self.valor_flor = 3
        self.quem_pediu_flor = 0
        self.quem_pediu_contraflor = 0
        self.quem_pediu_contraflor_resto = 0
        self.quem_pediu_flor = 0
