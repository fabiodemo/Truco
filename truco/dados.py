import pandas as pd
import os

class Dados():

    def __init__(self):
        self.modeloRegistro = pd.read_csv('../modelo_registro.csv', index_col='idMao')
        self.dados = pd.read_csv('../dbtrucoimitacao_maos.csv', index_col='idMao').fillna(0)

    def inicializarRegistro(self):
        
        self.modeloRegistro.jogadorMao = 1
        self.modeloRegistro.cartaAltaRobo = self.pontuacaoCartas[self.maoRank.index("Alta")]
        self.modeloRegistro.cartaMediaRobo = self.pontuacaoCartas[self.maoRank.index("Media")]
        self.modeloRegistro.cartaBaixaRobo = self.pontuacaoCartas[self.maoRank.index("Baixa")]
        self.modeloRegistro.ganhadorPrimeiraRodada = 2
        self.modeloRegistro.ganhadorSegundaRodada = 2
        self.modeloRegistro.ganhadorTerceiraRodada = 2

    def exportar_jogadas_csv(self, df):
        if not(os.path.isfile('jogadas.csv')):
            df.to_csv('jogadas.csv', header=df.columns)
        else:
            df.to_csv('jogadas.csv', mode='a', header=False)

        # self.modeloRegistro.to_csv('jogadas.csv')

    def carregar_modelo_zerado(self):
        registro = pd.read_csv('../modelo_registro.csv', index_col='idMao')
        return registro