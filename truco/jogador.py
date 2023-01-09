class Jogador():

    def __init__(self, nome):
        self.nome = nome
        self.mao = []
        self.maoRank = []
        self.pontos = 0
        self.rodadas = 0
        self.invido = 0
        self.primeiro = False
        self.ultimo = False
        self.flor = False

    def mostrarOpcoes(self):
        self.mostrarMao()
        print('[4] Truco')
        if (len(self.mao) == 3):
            print('[5] Flor')

    def criarMao(self, baralho):
        for i in range(3):
            self.mao.append(baralho.retirarCarta())
        
        self.maoRank = self.mao[0].classificarCarta(self.mao)
        
        print(self.maoRank)    

    def jogarCarta(self, carta_escolhida):
        return self.mao.pop(carta_escolhida -1)
    
    def mostrarMao(self):
        i = 1
        for carta in self.mao:
            carta.printarCarta(i)
            i += 1

    def adicionarPonto(self):
        self.pontos += 1
    
    def adicionarRodada(self):
        self.rodadas += 1
    
    def resetar(self):
        self.pontos = 0
        self.mao = []

    def checaMao(self):
        return self.mao
    
    def calculaInvido(self):
        self.invido += 1
    
    def checaFlor(self):
        print('checaflor')
        if all(carta.retornarNaipe() == self.mao[0].retornarNaipe() for carta in self.mao):
            print('FLOOOOOOOOOOR\n\n')
            return True

            