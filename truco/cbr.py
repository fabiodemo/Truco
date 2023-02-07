from sklearn.neighbors import NearestNeighbors
import pandas as pd
import warnings
from .pontos import MANILHA, CARTAS_VALORES
from .dados import Dados

class Cbr():

    def __init__(self):
        self.indice = 0
        self.dataset = self.carregar_dataset()
        self.dados = Dados()
        # self.dados = self.retornarSimilares()
        self.nbrs = self.vizinhos_proximos()


    def carregar_dataset(self):
        df = pd.read_csv('dbtrucoimitacao_maos.csv', index_col='idMao').fillna(-66)
        df.replace('ESPADAS', '1', inplace=True)
        df.replace('OURO', '2', inplace=True)
        df.replace('BASTOS', '3', inplace=True)
        df.replace('COPAS', '4', inplace=True)
        return df


    def vizinhos_proximos(self, df=None):
        if (df is None):
            return NearestNeighbors(n_neighbors=100, algorithm='ball_tree').fit(self.dataset)
        return NearestNeighbors(n_neighbors=100, algorithm='ball_tree').fit(df)


    def jogar_carta(self, rodada, pontuacao_cartas):
        registro = self.dados.retornar_registro()
        warnings.simplefilter(action='ignore', category=UserWarning)
        distancias, indices = self.nbrs.kneighbors((registro.to_numpy().reshape(1, -1)))
        jogadas_vencidas = jogadas_aumentadas = jogadas_perdidas = self.dataset.iloc[indices.tolist()[0]]
        jogadas_vencidas = jogadas_vencidas[((jogadas_vencidas.quemGanhouTruco == 2) & (jogadas_vencidas.quemTruco == 2))]
        jogadas_vencidas = jogadas_vencidas[((jogadas_vencidas.quemRetruco == 2) & (jogadas_vencidas.quemValeQuatro == 2))]
        jogadas_perdidas = jogadas_perdidas[((jogadas_perdidas.quemGanhouTruco == 2) & ((jogadas_perdidas.quemTruco == 2) | jogadas_perdidas.quemRetruco == 2 | jogadas_perdidas.quemValeQuatro == 2 ))]

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
        registro = self.dados.retornar_registro()
        warnings.simplefilter(action='ignore', category=UserWarning)
        distancias, indices = self.nbrs.kneighbors((registro.to_numpy().reshape(1, -1)))
        jogadas_vencidas = jogadas_perdidas = self.dataset.iloc[indices.tolist()[0]]
        jogadas_vencidas = jogadas_vencidas[((jogadas_vencidas.quemGanhouTruco == 2) & (jogadas_vencidas.quemTruco == 2) & (jogadas_vencidas.quemGanhouTruco == 2) & (jogadas_vencidas.quemTruco == quem_pediu))]
        jogadas_perdidas = jogadas_perdidas[((jogadas_vencidas.quemGanhouTruco == 1) |((jogadas_perdidas.quemNegouTruco == 2) & ((jogadas_perdidas.quemTruco == 2) | jogadas_perdidas.quemRetruco == 2)))]
        # 'quemNegouTruco', 'quemGanhouTruco', 'quemTruco', 'quemRetruco', 
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


    def envido(self, quem_pediu):
        registro = self.dados.retornar_registro()
        warnings.simplefilter(action='ignore', category=UserWarning)
        distancias, indices = self.nbrs.kneighbors((registro.to_numpy().reshape(1, -1)))
        jogadas_vencidas = jogadas_perdidas = self.dataset.iloc[indices.tolist()[0]]
        jogadas_vencidas = jogadas_vencidas[((jogadas_vencidas.quemGanhouTruco == 2) & (jogadas_vencidas.quemTruco == 2))]
        jogadas_perdidas = jogadas_perdidas[((jogadas_perdidas.quemNegouTruco == 2) & ((jogadas_perdidas.quemTruco == 2) | jogadas_perdidas.quemRetruco == 2))]
        # 'quemPediuEnvido', 'quemPediuFaltaEnvido', 'quemPediuRealEnvido', 'pontosEnvidoRobo', 'pontosEnvidoHumano', 'quemNegouEnvido', 'quemGanhouEnvido', 'quemEscondeuPontosEnvido'
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

    def flor(self):
        pass


    def jogar_rodada(self, jogador2, rodada, pontuacao_cartas):

        # truco = self.truco(jogador2)
        # if (truco is True):
        #     return 4

        return self.jogar_carta(rodada, pontuacao_cartas)

    def enriquecer_agente(self, rodada=None, pontuacao_cartas=None, mao_rank=None, qualidade_mao_bot=None, carta_humano=None):
        if (rodada == 1):
            self.dados.primeira_rodada(pontuacao_cartas, mao_rank, qualidade_mao_bot, carta_humano)
        # if (rodada == 2):
        #     self.dados.segunda_rodada(carta_humano, ganhador)
        # if (rodada == 3):
        #     self.dados.terceira_rodada(carta_humano, ganhador)

    def enriquecer_jogadas_bot(self, rodada, carta_jogador_02):
        if (rodada == 2):
            self.dados.cartas_jogadas_pelo_bot('primeira', carta_jogador_02)
        if (rodada == 3):
            self.dados.cartas_jogadas_pelo_bot('segunda', carta_jogador_02)
        if (rodada == 4):
            self.dados.cartas_jogadas_pelo_bot('terceira', carta_jogador_02)