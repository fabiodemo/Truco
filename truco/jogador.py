class Jogador():

    def __init__(self, nome):
        self.nome = nome
        self.mao = []
        self.maoRank = []
        self.pontos = 0
        self.rodadas = 0
        self.envido = 0
        self.primeiro = False
        self.ultimo = False
        self.flor = False
        self.pediuTruco = False

    def mostrarOpcoes(self):
        print(f'pontos self.envido: {self.envido}')
        self.mostrarMao()
        if (len(self.mao) >= 2): self.calculaEnvido(self.mao)
        if (self.pediuTruco is False): 
            print('[4] Truco')
        if ((len(self.mao)) == 3 and self.flor is False and (self.checaFlor())):
            print('[5] Flor')
            self.flor = True
        if ((len(self.mao) >= 2) and (self.envido > 0)):
            print('[6] Envido')
            self.flor = True

    def criarMao(self, baralho):
        for i in range(3):
            self.mao.append(baralho.retirarCarta())

    def jogarCarta(self, carta_escolhida):
        return self.mao.pop(carta_escolhida)
    
    def mostrarMao(self):
        i = 0
        for carta in self.mao:
            carta.printarCarta(i)
            i += 1
        cartas = [(f"{carta.numero} de {carta.naipe}") for carta in self.mao]
        # print(cartas)
        # print('\n'.join(map('  '.join, zip(*(carta.desenharCarta(c) for c in cartas)))))

    def adicionarPontos(self, pontos):
        self.pontos += pontos

    def adicionarRodada(self):
        self.rodadas += 1
    
    def resetar(self):
        self.rodadas = 0
        self.mao = []
        self.flor = False
        self.pediuTruco = False

    def checaMao(self):
        return self.mao
    
    def calculaEnvido(self, mao):
        pontos_envido = []

        for i in range(len(mao)):
            for j in range(i+1, len(mao)):
                if(mao[i].retornarNaipe() == mao[j].retornarNaipe()):
                    pontos_envido.append(20 + (mao[0].retornaPontoEnvido(mao[i]) + mao[0].retornaPontoEnvido(mao[j])))
                else:
                    pontos_envido.append(mao[0].retornaPontoEnvido(mao[i]) + mao[0].retornaPontoEnvido(mao[j]))
        
        self.envido = max(pontos_envido)
        print(self.envido)
    
    def checaFlor(self):
        if all(carta.retornarNaipe() == self.mao[0].retornarNaipe() for carta in self.mao):
            # print('Flor do Jogador')
            return True
        return False
