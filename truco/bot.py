import random 
import pandas as pd

class Bot():
    def __init__(self, nome):
        self.nome = nome
        self.mao = []
        self.mao_rank = []
        self.indices = []
        self.pontuacao_cartas = []
        self.qualidade_mao = 0
        self.pontos = 0
        self.rodadas = 0
        self.envido = 0
        self.rodada = 1
        self.primeiro = False
        self.ultimo = False
        self.flor = False
        self.pediu_flor = False
        self.pediu_truco = False


    def criar_mao(self, baralho):
        """Cria a mão do jogador e insere três cartas do baralho a ela."""
        self.indices = [0, 1, 2]
        for i in range(3):
            self.mao.append(baralho.retirar_carta())
        self.flor = self.checa_flor()
        self.pontuacao_cartas, self.mao_rank = self.mao[0].classificar_carta(self.mao)
        self.qualidade_mao = self.calcular_qualidade_mao(self.pontuacao_cartas, self.mao_rank)


    def enriquecer_bot(self, cbr, carta_jogador_01):
        """Enriquece os dados com cartas jogadas pelo oponente, que serão utilizadas como entrada para cálculo de similaridade."""
        if(self.rodada == 1):
            cbr.enriquecer_agente(self.rodada, self.pontuacao_cartas, self.mao_rank, self.qualidade_mao, carta_jogador_01)
        else:
            pass


    def enriquecer_cartas_bot(self, cbr, carta_jogador_02):
        """Enriquece os dados com cartas jogadas pelo bot, que serão utilizadas como entrada para cálculo de similaridade."""
        cbr.enriquecer_jogadas_bot(carta_jogador_02)


    def jogar_carta(self, cbr, truco):
        """Joga a carta, removendo da mão do jogador."""
        # jogada = self.avaliar_jogada()
        # Envido
        if ((len(self.mao) == 3)):
            self.calcula_envido(self.mao)
            envido = cbr.envido(1, self.envido)
            if (envido is True):
                return 6
        # Flor
        if ((len(self.mao)) == 3 and self.flor is False and (self.checa_flor())):
            flor = cbr.flor()
            if (flor is True):
                return 5

        # Pedir truco
        truco = cbr.truco(1)
        if (truco is True):
            return 4

        # Manda o valor de acordo com a rodada, para o CBR escolher as colunas/campos necessários
        escolha = cbr.jogar_carta(self.rodada, self.pontuacao_cartas)
        print(escolha)
        self.ajustar_indices(escolha)
        self.rodada += 1
        # Verificar cartas na mão antes de jogar
        return escolha
        # return self.mao.pop(escolha)


    def calcula_envido(self, mao):
        """Realização do cálculo de envido."""
        pontos_envido = []
        for i in range(len(mao)):
            for j in range(i+1, len(mao)):
                if (mao[i].retornar_naipe() == mao[j].retornar_naipe()):
                    pontos_envido.append(20 + (mao[0].retornar_pontos_envido(mao[i]) + mao[0].retornar_pontos_envido(mao[j])))
                else:
                    pontos_envido.append(max(mao[0].retornar_pontos_envido(mao[i]), mao[0].retornar_pontos_envido(mao[j])))
        
        return max(pontos_envido)


    def retorna_pontos_envido(self):
        """Retorna os pontos do envido."""
        return self.envido


    def ajustar_indices(self, i):
        """Ajusta os índices, para que bot possa ter opçoões de 0 até o tamanho da self.mao para jogar."""
        # print(f'\n{self.mao_rank},{self.indices},{self.pontuacao_cartas},{self.mao}')
        self.mao_rank.pop(i)
        self.indices.pop(i)
        self.pontuacao_cartas.pop(i)
        # self.mao.pop(i)


    def mostrar_mao(self):
        """Exibe as cartas na mão do bot."""
        i = 0
        for carta in self.mao:
            carta.exibir_carta(i)
            i += 1
        

    def adicionar_pontos(self, pontos):
        """Adiciona pontos a pontuação acumulada do jogador."""
        self.pontos += pontos
    

    def adicionar_rodada(self):
        """Adiciona uma rodada ganha ao jogador."""
        self.rodadas += 1


    def checa_mao(self):
        return self.mao


    def checa_flor(self):
        # print('checa_flor')
        if all(carta.retornar_naipe() == self.mao[0].retornar_naipe() for carta in self.mao):
            print('Flor do Bot!')
            return True
        return False


    def avaliar_truco(self):
        return 2
        # if (self.qualidade_mao > 50):
        #     return 2

        # elif (self.qualidade_mao > 35):
        #     return 1

        # else:
        #     return 0
    
    # implementar retruco do bot
    def avaliar_aumentar_truco(self, possibilidade, cbr):
        if (possibilidade):
            return True
        return False


    def avaliar_envido(self):
        return None


    def calcular_qualidade_mao(self, lista_pontuacao, lista_mao_rank):
        """Calcula a qualidade da mão do bot, baseado na média harmônica da codificação."""
        m1 = (2 / ((1/lista_pontuacao[int(lista_mao_rank.index('Alta'))]) + (1/lista_pontuacao[int(lista_mao_rank.index('Media'))])))
        m2 = ((2 * lista_pontuacao[int(lista_mao_rank.index('Media'))]) + (lista_pontuacao[int(lista_mao_rank.index('Baixa'))])/2+1)
        m3 = ((2 * m1) + m2) / (2+1)
        print(m3)
        
        self.qualidade_mao = m3


    def resetar(self):
        """Resetar variáveis ligadas a rodada."""
        self.mao = []
        self.mao_rank = []
        self.indices = []
        self.pontuacao_cartas = []
        self.qualidade_mao = 0
        self.rodadas = 0
        self.envido = 0
        self.rodada = 1
        self.flor = False
        self.pediu_flor = False
        self.pediu_truco = False


'''
- Centralizar toda a CBR em uma unica função, que retorna qual seria o tipo de jogada;
- Quando necessário usar outra inteligência/agente, só substitui-la diretamente na classe bot.
'''        