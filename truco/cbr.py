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
        df = pd.read_csv('dbtrucoimitacao_maos.csv', index_col='idMao').fillna(0)
        df.replace('ESPADAS', '1', inplace=True)
        df.replace('OURO', '2', inplace=True)
        df.replace('BASTOS', '3', inplace=True)
        df.replace('COPAS', '4', inplace=True)
        return df


    def vizinhos_proximos(self):
        return NearestNeighbors(n_neighbors=100, algorithm='ball_tree').fit(self.dataset)


    def vizinhos_proximos_truco(self):
        return NearestNeighbors(n_neighbors=100, algorithm='ball_tree').fit(self.dataset)


    def vizinhos_proximos_truco(self):
        return NearestNeighbors(n_neighbors=100, algorithm='ball_tree').fit(self.dataset)


    def jogar_carta(self, rodada, pontuacaoCartas):
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
        print(valor_referencia)
        if (valor_referencia <= 0): 
            return -1
        
        carta_escolhida = min(self.pontuacaoCartas, key=lambda x:abs(x-valor_referencia))
        return carta_escolhida


    def truco(self):
        pass


    def envido(self):
        pass


    def flor(self):
        pass


    def jogar_rodada(self, jogador2, rodada, pontuacaoCartas):
        if (len(jogador2.checaMao()) >= 3 and jogador2.flor is True and jogador2.pediu_flor is False):
            flor = self.flor()
            if (flor is True):
                return 5
        
        if (len(jogador2.checaMao()) >= 3 and jogador2.flor is False):
            envido = self.envido()
            if (envido is True):
                return 6

        self.truco()
        self.jogar_carta()

        pass