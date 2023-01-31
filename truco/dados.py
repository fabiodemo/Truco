import pandas as pd
import os

class Dados():

    def __init__(self):
        self.registro_modelo = pd.read_csv('../modelo_registro.csv', index_col='idMao')
        self.dados = pd.read_csv('../dbtrucoimitacao_maos.csv', index_col='idMao').fillna(0)

    def inicializar_jogada(self, potuacao_cartas, mao_rank):
        
        self.registro_modelo.jogadorMao = 1
        self.registro_modelo.cartaAltaRobo = potuacao_cartas[mao_rank.index("Alta")]
        self.registro_modelo.cartaMediaRobo = potuacao_cartas[mao_rank.index("Media")]
        self.registro_modelo.cartaBaixaRobo = potuacao_cartas[mao_rank.index("Baixa")]
        self.registro_modelo.ganhadorPrimeiraRodada = 2
        self.registro_modelo.ganhadorSegundaRodada = 2
        self.registro_modelo.ganhadorTerceiraRodada = 2

        return self.registro_modelo

    def segunda_jogada(self, primeira_carta_robo, primeira_carta_humano):
        self.registro_modelo.primeiraCartaRobo = primeira_carta_robo.retornarNumero()
        self.registro.naipePrimeiraCartaRobo = primeira_carta_robo.retornarNaipe()
        self.registro_modelo.primeiraCartaHumano = primeira_carta_humano.retornarNumero()
        self.registro_modelo.naipePrimeiraCartaHumano = primeira_carta_humano.retornarNaipe()
    
    def terceira_jogada(self, segunda_carta_robo, segunda_carta_humano):
        self.registro_modelo.segundaCartaRobo = segunda_carta_robo.retornarNumero()
        self.registro.naipeSegundaCartaRobo = segunda_carta_robo.retornarNaipe()
        self.registro_modelo.SegundaCartaHumano = segunda_carta_humano.retornarNumero()
        self.registro_modelo.naipeSegundaCartaHumano = segunda_carta_humano.retornarNaipe()

    def finalizar_jogadas(self, terceira_carta_robo, terceira_carta_humano):
        self.registro_modelo.terceiraCartaRobo = terceira_carta_robo.retornarNumero()
        self.registro.naipeTerceiraCartaRobo = terceira_carta_robo.retornarNaipe()
        self.registro_modelo.terceiraCartaHumano = terceira_carta_humano.retornarNumero()
        self.registro_modelo.naipeTerceiraCartaHumano = terceira_carta_humano.retornarNaipe()

    def finalizar_jogo(self, df):
        if not(os.path.isfile('jogadas.csv')):
            df.to_csv('jogadas.csv', header=df.columns)
        else:
            df.to_csv('jogadas.csv', mode='a', header=False)

        # self.registro_modelo.to_csv('jogadas.csv')

    def subset_envido(self):
        pass

    def subset_truco(self):
        pass

    def carregar_modelo_zerado(self):
        self.registro_modelo = pd.read_csv('../modelo_registro.csv', index_col='idMao')
        return self.registro_modelo