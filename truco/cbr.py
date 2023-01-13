from sklearn.neighbors import NearestNeighbors
import pandas as pd
from pontos import MANILHA, CARTAS_VALORES

class Cbr():

    def __init__(self):
        self.indice = 0
        self.casos = self.atualizarDataframe()
        self.nbrs = self.VizinhosProximos()

    def codificarNaipe(self, naipe):
        if (naipe == 'ESPADAS'):
            return 1
        
        if (naipe == 'OUROS'):
            return 2
        
        if (naipe == 'BASTOS'):
            return 3
        
        if (naipe == 'COPAS'):
            return 4

    def atualizarDataframe(self):
        df = pd.read_csv('../dbtrucoimitacao_maos.csv', index_col='idMao').fillna(0)
        colunas_string = [
            'naipeCartaAltaRobo', 'naipeCartaMediaRobo','naipeCartaBaixaRobo', 'naipeCartaAltaHumano','naipeCartaMediaHumano', 'naipeCartaBaixaHumano','naipePrimeiraCartaRobo', 'naipePrimeiraCartaHumano',	'naipeSegundaCartaRobo', 'naipeSegundaCartaHumano','naipeTerceiraCartaRobo', 'naipeTerceiraCartaHumano',
            ]
        colunas_int = [col for col in df.columns if col not in colunas_string]
        df[colunas_int] = df[colunas_int].astype('int').apply(abs)
        df.replace('ESPADAS', '1', inplace=True)
        df.replace('OURO', '2', inplace=True)
        df.replace('BASTOS', '3', inplace=True)
        df.replace('COPAS', '4', inplace=True)
        df[colunas_string] = df[colunas_string].astype('int')
        # df.apply(abs)
        df = df[(df >= 0).all(axis=1)]
        
        return df

    def VizinhosProximos(self):
        self.nbrs = NearestNeighbors(n_neighbors=100, algorithm='ball_tree').fit(self.casos)

    def retornarSimilares(self, registro):
        df = self.VizinhosProximos()
        # teste_distancia, teste_indices = nbrs.kneighbors(teste_registro.to_numpy().reshape(1, -1))
        distancias, indices = self.nbrs.kneighbors(self.casos)
        jogadas_vencidas = self.casos.iloc[registro.tolist()[0]]
        jogadas_vencidas = [((jogadas_vencidas.ganhadorPrimeiraRodada == 2) & (jogadas_vencidas.ganhadorSegundaRodada == 2) | (jogadas_vencidas.ganhadorPrimeiraRodada == 2) & (jogadas_vencidas.ganhadorTerceiraRodada == 2) | (jogadas_vencidas.ganhadorSegundaRodada == 2) & (jogadas_vencidas.ganhadorTerceiraRodada == 2))]
        return jogadas_vencidas