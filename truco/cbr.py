from sklearn.neighbors import NearestNeighbors
import pandas as pd
import warnings
from pontos import MANILHA, CARTAS_VALORES
from dados import Dados

class Cbr():

    def __init__(self):
        self.indice = 0
        self.dataset = self.carregar_dataset()
        self.dados = Dados()
        # self.casos = self.retornarSimilares()
        # self.nbrs = self.VizinhosProximos()

    def carregar_dataset(self):
        df = pd.read_csv('../dbtrucoimitacao_maos.csv', index_col='idMao').fillna(0)
        df.replace('ESPADAS', '1', inplace=True)
        df.replace('OURO', '2', inplace=True)
        df.replace('BASTOS', '3', inplace=True)
        df.replace('COPAS', '4', inplace=True)

    def VizinhosProximos(self):
        self.nbrs = NearestNeighbors(n_neighbors=100, algorithm='ball_tree').fit(self.casos)

    def retornarSimilares(self, registro, colunas_string):
        registro = self.dados.carregar_modelo_zerado()
        colunas_string = [
            'naipeCartaAltaRobo', 'naipeCartaMediaRobo','naipeCartaBaixaRobo', 'naipeCartaAltaHumano','naipeCartaMediaHumano', 'naipeCartaBaixaHumano','naipePrimeiraCartaRobo', 'naipePrimeiraCartaHumano',	'naipeSegundaCartaRobo', 'naipeSegundaCartaHumano','naipeTerceiraCartaRobo', 'naipeTerceiraCartaHumano',
            ]
        df = pd.read_csv('../dbtrucoimitacao_maos.csv', index_col='idMao').fillna(0)
        colunas_int = [col for col in df.columns if col not in colunas_string]
        # df[colunas_int] = df[colunas_int].astype('int').apply(abs)
        df.replace('ESPADAS', '1', inplace=True)
        df.replace('OURO', '2', inplace=True)
        df.replace('BASTOS', '3', inplace=True)
        df.replace('COPAS', '4', inplace=True)
        df[colunas_string] = df[colunas_string].astype('int')
        # df.apply(abs)
        # df = df[(df >= 0).all(axis=1)]

        warnings.simplefilter(action='ignore', category=UserWarning)
        df = self.VizinhosProximos()
        distancias, indices = self.nbrs.kneighbors((registro.to_numpy().reshape(1, -1)))
        # print(distancias, indices)
        jogadas_vencidas = self.casos.iloc[indices.tolist()[0]]
        jogadas_vencidas = jogadas_vencidas[((jogadas_vencidas.ganhadorPrimeiraRodada == 2) & (jogadas_vencidas.ganhadorSegundaRodada == 2) | (jogadas_vencidas.ganhadorPrimeiraRodada == 2) & (jogadas_vencidas.ganhadorTerceiraRodada == 2) | (jogadas_vencidas.ganhadorSegundaRodada == 2) & (jogadas_vencidas.ganhadorTerceiraRodada == 2))]
        return jogadas_vencidas

    def cbr_truco(self):
        pass
    
    def cbr_envido(self):
        pass
    
    def cbr_jogada(self):

        pass

