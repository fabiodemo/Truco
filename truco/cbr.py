from sklearn.neighbors import NearestNeighbors
import pandas as pd
import warnings
from .dados import Dados

class Cbr():
    def __init__(self):
        self.indice = 0
        self.dados = Dados()
        self.dataset = self.dados.retornar_casos()
        # self.dados = self.retornarSimilares()
        self.nbrs = self.vizinhos_proximos()


    def carregar_dataset(self):
        """Carrega o dataset, caso necessário"""
        df = pd.read_csv('dbtrucoimitacao_maos.csv', index_col='idMao').fillna(-100)
        df.replace('ESPADAS', '1', inplace=True)
        df.replace('OURO', '2', inplace=True)
        df.replace('BASTOS', '3', inplace=True)
        df.replace('COPAS', '4', inplace=True)
        return df


    def vizinhos_proximos(self, df=None):
        """Cálculo dos 100 Nearest Neighbors."""
        if (df is None):
            return NearestNeighbors(n_neighbors=100, algorithm='ball_tree').fit(self.dataset)
        return NearestNeighbors(n_neighbors=100, algorithm='ball_tree').fit(df)


    def jogar_carta(self, rodada, pontuacao_cartas):
        """Método que considera as jogadas em que o bot saiu vitorioso e retorna a pontuação mais próxima a ser jogada em determinada rodada."""
        registro = self.dados.retornar_registro()
        warnings.simplefilter(action='ignore', category=UserWarning)
        distancias, indices = self.nbrs.kneighbors((registro.to_numpy().reshape(1, -1)))
        jogadas_vencidas = self.dataset.iloc[indices.tolist()[0]]
        jogadas_vencidas = jogadas_vencidas[((jogadas_vencidas.ganhadorPrimeiraRodada == 2) & (jogadas_vencidas.ganhadorSegundaRodada == 2) | (jogadas_vencidas.ganhadorPrimeiraRodada == 2) & (jogadas_vencidas.ganhadorTerceiraRodada == 2) | (jogadas_vencidas.ganhadorSegundaRodada == 2) & (jogadas_vencidas.ganhadorTerceiraRodada == 2))]

        ordem_carta_jogada = 'CartaRobo'
        if ((rodada) == 3): ordem_carta_jogada = 'primeira' + ordem_carta_jogada
        elif ((rodada) == 2): ordem_carta_jogada = 'segunda' + ordem_carta_jogada
        elif ((rodada) == 1): ordem_carta_jogada = 'terceira' + ordem_carta_jogada
        valor_referencia = jogadas_vencidas[ordem_carta_jogada].value_counts().index.to_list()[0]
        if (valor_referencia <= 0): 
            return -1
        carta_escolhida = min(pontuacao_cartas, key=lambda x:abs(x-valor_referencia))
        # print(jogadas_vencidas[ordem_carta_jogada].value_counts())
        print(pontuacao_cartas)
        print(carta_escolhida)
        # return carta_escolhida
        return pontuacao_cartas.index(int(carta_escolhida))

    def truco(self, quem_pediu):
        """Método que considera o pedido de truco e retorna as opções para aceitar, aumentar ou fugir."""
        registro = self.dados.retornar_registro()
        warnings.simplefilter(action='ignore', category=UserWarning)
        distancias, indices = self.nbrs.kneighbors((registro.to_numpy().reshape(1, -1)))
        jogadas = jogadas_aumentadas = jogadas_perdidas = self.dataset.iloc[indices.tolist()[0]]
        jogadas = jogadas[((jogadas.quemTruco == quem_pediu))]
        # 'quemNegouTruco', 'quemGanhouTruco', 'quemTruco', 'quemRetruco', 

        vencidas = jogadas['quemGanhouTruco'].value_counts().index.to_list()[0]
        negadas = jogadas['quemNegouTruco'].value_counts().index.to_list()[0]
        retruco = jogadas['quemRetruco'].value_counts().index.to_list()[0]

        print(vencidas, negadas, retruco)

        # carta_escolhida = min(pontuacao_cartas, key=lambda x:abs(x-valor_referencia))
        # print(jogadas_vencidas[ordem_carta_jogada].value_counts())
        # return carta_escolhida
        # return pontuacao_cartas.index(int(carta_escolhida))
        return False


    def envido(self, quem_pediu, pontos_envido_robo):
        """Método que considera o pedido de envido e retorna as opções para aceitar, pedir real envido, falta envido ou fugir."""
        registro = self.dados.retornar_registro()
        warnings.simplefilter(action='ignore', category=UserWarning)
        distancias, indices = self.nbrs.kneighbors((registro.to_numpy().reshape(1, -1)))
        jogadas = self.dataset.iloc[indices.tolist()[0]]
        jogadas = jogadas[((jogadas.pontosEnvidoRobo > jogadas.pontosEnvidoHumano))]
        # 'quemPediuEnvido', 'quemPediuFaltaEnvido', 'quemPediuRealEnvido', 'pontosEnvidoRobo', 'pontosEnvidoHumano', 'quemNegouEnvido', 'quemGanhouEnvido', 'quemEscondeuPontosEnvido'
        # print(jogadas)
        ganhas = jogadas['quemGanhouEnvido'].value_counts().index.to_list()[0]
        aumentadas = jogadas['quemPediuRealEnvido'].value_counts().index.to_list()[0]
        perdidas = jogadas['quemGanhouEnvido'].value_counts().index.to_list()[0]
        pontos_jogador = jogadas['pontosEnvidoHumano'].value_counts().index.to_list()[0]

        print(ganhas, aumentadas, perdidas, pontos_jogador)
        if (quem_pediu == 1):
            if (ganhas > aumentadas and ganhas > perdidas):
                return 1
            elif (aumentadas > ganhas and aumentadas > perdidas):
                return 2
            else:
                return 0
        else:
            if (pontos_envido_robo > pontos_jogador and pontos_envido_robo > 0):
                return 1

        return None

    def enriquecer_agente(self, rodada=None, pontuacao_cartas=None, mao_rank=None, qualidade_mao_bot=None, carta_humano=None):
        """Controlador do método pertencente a classe Dados, que enriquecerá o conhecimento do bot com a carta jogada pelo humano."""
        if (rodada == 1):
            self.dados.primeira_rodada(pontuacao_cartas, mao_rank, qualidade_mao_bot, carta_humano)
        # if (rodada == 2):
        #     self.dados.segunda_rodada(carta_humano, ganhador)
        # if (rodada == 3):
        #     self.dados.terceira_rodada(carta_humano, ganhador)

    def enriquecer_jogadas_bot(self, rodada, carta_jogador_02):
        """Controlador do método pertencente a classe Dados, que enriquecerá o conhecimento do bot com a carta a qual ele jogou."""
        if (rodada == 2):
            self.dados.cartas_jogadas_pelo_bot('primeira', carta_jogador_02)
        if (rodada == 3):
            self.dados.cartas_jogadas_pelo_bot('segunda', carta_jogador_02)
        if (rodada == 4):
            self.dados.cartas_jogadas_pelo_bot('terceira', carta_jogador_02)