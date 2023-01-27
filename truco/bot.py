import random 
import pandas as pd

class Bot():

    def __init__(self, nome):
        self.nome = nome
        self.mao = []
        self.maoRank = []
        self.indices = []
        self.pontuacaoCartas = []
        self.forcaMao = 0
        self.pontos = 0
        self.rodadas = 0
        self.envido = 0
        self.primeiro = False
        self.ultimo = False
        self.flor = False
        self.pediuTruco = False

    def criarMao(self, baralho):
        self.indices = [0, 1, 2]
        
        # Mudar forma de classificação dos dados vindos da base de casos, para ter uma métrica extra de inserção
        for i in range(3):
            self.mao.append(baralho.retirarCarta())
        self.flor = self.checaFlor()
        self.pontuacaoCartas, self.maoRank = self.mao[0].classificarCarta(self.mao)
        self.forcaMao = self.calcular_forca_mao(self.pontuacaoCartas(), self.maoRank())
    
    def jogarCarta(self, cbr):
        df = cbr.retornarSimilares(self.modeloRegistro)
        carta_escolhida = 0
        ordem_carta_jogada = 'CartaRobo'

        if (len(self.indices) == 3): ordem_carta_jogada = 'primeira' + ordem_carta_jogada
        elif (len(self.indices) == 2): ordem_carta_jogada = 'segunda' + ordem_carta_jogada
        elif (len(self.indices) == 1): ordem_carta_jogada = 'terceira' + ordem_carta_jogada

        for i in reversed(range(len(df[ordem_carta_jogada].value_counts().index.to_list()))): 
            aux = df[ordem_carta_jogada].value_counts().index.to_list()[i]
            
            if(carta_escolhida in self.pontuacaoCartas):
                carta_escolhida = aux

        if(carta_escolhida == 0):
            valor_referencia = df[ordem_carta_jogada].value_counts().index.to_list()[0]
            carta_escolhida = min(self.pontuacaoCartas, key=lambda x:abs(x-valor_referencia))

        indice = self.pontuacaoCartas.index(carta_escolhida)
        self.indices.remove(indice)
        self.pontuacaoCartas.remove(self.pontuacaoCartas[self.pontuacaoCartas.index(carta_escolhida)])
        self.indices = self.AjustaIndicesMao(len(self.indices))
        return self.mao.pop(indice)


    def AjustaIndicesMao(self, tam_mao):
        if(tam_mao) == 2:
            return [0, 1]
        
        if(tam_mao) == 1:
            return [0]

    def mostrarMao(self):
        i = 0
        for carta in self.mao:
            carta.printarCarta(i)
            i += 1
        
    def adicionarPontos(self, pontos):
        self.pontos += pontos
    
    def adicionarRodada(self):
        self.rodadas += 1
    
    def resetar(self):
        self.rodadas = 0
        self.mao = []
        self.flor = False

    def checaMao(self):
        return self.mao
    
    def calculaInvido(self):
        self.invido += 1

    def checaFlor(self):
        # print('checaflor')
        if all(carta.retornarNaipe() == self.mao[0].retornarNaipe() for carta in self.mao):
            print('Flor do Bot!')
            self.flor = True
            return True
        return False
    
    def avaliarJogadaHumano(self):
        pass

    def avaliarTruco(self):
        return 2
        # if (self.forcaMao > 50):
        #     return 2

        # elif (self.forcaMao > 35):
        #     return 1

        # else:
        #     return 0
    
    # implementar retruco do bot
    def avaliarAumentarTruco(self, possibilidade, cbr):
        if (possibilidade):
            return True
        return False

    def avaliarEnvido(self):
        return None

    def calcular_forca_mao(self, lista_pontuacao, lista_maorank):
        m1 = (2 / ((1/lista_pontuacao[int(lista_maorank.index('Alta'))]) + (1/lista_pontuacao[int(lista_maorank.index('Media'))])))
        m2 = ((2 * lista_pontuacao[int(lista_maorank.index('Media'))]) + (lista_pontuacao[int(lista_maorank.index('Baixa'))])/2+1)
        m3 = ((2 * m1) + m2) / (2+1)
        print(m3)
        
        self.forcaMao = m3

    def jogada_bot(self):
        jogada = self.avaliar_jogada()
        # Envido
        if ((len(self.mao) == 3) and (self.envido > 0)):
            self.calculaEnvido(self.mao)
        # Flor
        if ((len(self.mao)) == 3 and self.flor is False and (self.checaFlor())):
            print('[5] Flor')
        # Pedir truco
        if (len(self.mao) >= 2): 
            print('[4] Truco')
        # Verificar cartas na mão antes de jogar
    
    def avaliar_jogada(self):
        return 1

    # def caseBasedReasoning(self):

'''
- Centralizar toda a CBR em uma unica função, que retorna qual seria o tipo de jogada;
- Quando necessário usar outra inteligência/agente, só substitui-la diretamente na classe bot.
'''        