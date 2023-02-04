from sklearn.neighbors import NearestNeighbors
import pandas as pd
import warnings
from .pontos import MANILHA, CARTAS_VALORES
from .dados import Dados

class Cbr():

    def __init__(self):
        self.indice = 0
        self.dataset = self.carregar_dataset()
        self.casos = Dados()
        # self.casos = self.retornarSimilares()
        # self.nbrs = self.VizinhosProximos()

    def carregar_dataset(self):
        df = pd.read_csv('dbtrucoimitacao_maos.csv', index_col='idMao').fillna(0)
        df.replace('ESPADAS', '1', inplace=True)
        df.replace('OURO', '2', inplace=True)
        df.replace('BASTOS', '3', inplace=True)
        df.replace('COPAS', '4', inplace=True)

    def vizinhos_proximos(self):
        return NearestNeighbors(n_neighbors=100, algorithm='ball_tree').fit(self.casos.registro)

    def retornar_similares(self, registro):
        # registro = self.casos.carregar_modelo_zerado()

        warnings.simplefilter(action='ignore', category=UserWarning)
        df = self.vizinhos_proximos()
        distancias, indices = self.vizinhos_proximos((registro.to_numpy().reshape(1, -1)))
        # print(distancias, indices)
        jogadas_vencidas = self.casos.iloc[indices.tolist()[0]]
        jogadas_vencidas = jogadas_vencidas[((jogadas_vencidas.ganhadorPrimeiraRodada == 2) & (jogadas_vencidas.ganhadorSegundaRodada == 2) | (jogadas_vencidas.ganhadorPrimeiraRodada == 2) & (jogadas_vencidas.ganhadorTerceiraRodada == 2) | (jogadas_vencidas.ganhadorSegundaRodada == 2) & (jogadas_vencidas.ganhadorTerceiraRodada == 2))]
        # return jogadas_vencidas

        # df = cbr.retornarSimilares(self.modeloRegistro)
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
        
        return carta_escolhida

    def truco(self):
        pass
    
    def envido(self):
        pass
    
    def flor(self):
        pass

    def jogar_rodada(self, rodada):
        df = self.dados
        cols = df.columns
        novo_df = df.apply(lambda x: x > 0)
        novo_df.apply(lambda x: list(cols[x.values]), axis=1)
        pass
