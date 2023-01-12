import random 

class Bot():

    def __init__(self, nome):
        self.nome = nome
        self.mao = []
        self.pontos = 0
        self.rodadas = 0
        self.invido = 0
        self.primeiro = False
        self.ultimo = False
        self.flor = False
        self.indices = []

    def criarMao(self, baralho):
        self.indices = [0, 1, 2]
        for i in range(3):
            self.mao.append(baralho.retirarCarta())
        self.flor = self.checaFlor()
    
    def jogarCarta(self):
        self.AjustaIndicesMao(len(self.indices))
        carta_escolhida = random.choice(self.indices)
        self.indices.remove(carta_escolhida)
        return self.mao.pop(carta_escolhida)
    
    def AjustaIndicesMao(self, tam_mao):
        if(tam_mao) == 2:
            self.indices = [0, 1]
        if(tam_mao) == 1:
            self.indices = [0]

    def mostrarMao(self):
        i = 1
        for carta in self.mao:
            carta.printarCarta(i)
            i += 1
        

    def adicionarPonto(self):
        self.pontos += 1
    
    def adicionarRodada(self, rodadas):
        self.rodadas += rodadas
    
    def resetar(self):
        self.pontos = 0
        self.mao = []
        self.flor = False

    def checaMao(self):
        return self.mao
    
    def calculaInvido(self):
        self.invido += 1

    def checaFlor(self):
        # print('checaflor')
        if all(carta.retornarNaipe() == self.mao[0].retornarNaipe() for carta in self.mao):
            # print('Flor do Bot!')
            self.flor = True
            return True
        return False
    
    def avaliarTruco(self):
        return random.choice([True, False])