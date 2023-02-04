import pandas as pd
import os

class Dados():
    def __init__(self):
        self.casos = self.tratamento_inicial_df()
        self.registro = pd.read_csv('modelo_registro.csv', index_col='idMao')

    def tratamento_inicial_df(self):
        df = pd.read_csv('dbtrucoimitacao_maos.csv', index_col='idMao')
        colunas_string = [
            'naipeCartaAltaRobo', 'naipeCartaMediaRobo','naipeCartaBaixaRobo', 'naipeCartaAltaHumano','naipeCartaMediaHumano', 'naipeCartaBaixaHumano','naipePrimeiraCartaRobo', 'naipePrimeiraCartaHumano',	'naipeSegundaCartaRobo', 'naipeSegundaCartaHumano','naipeTerceiraCartaRobo', 'naipeTerceiraCartaHumano',
            ]
        colunas_int = [col for col in df.columns if col not in colunas_string]
        df.replace('ESPADAS', '1', inplace=True)
        df.replace('OURO', '2', inplace=True)
        df.replace('BASTOS', '3', inplace=True)
        df.replace('COPAS', '4', inplace=True)
        df[colunas_string] = df[colunas_string].fillna(0)
        df[colunas_string] = df[colunas_string].astype('int16')
        return df


    def primeira_rodada(self, potuacao_cartas, mao_rank, qualidade_mao_bot):  
        self.registro.jogadorMao = 1
        self.registro.cartaAltaRobo = potuacao_cartas[mao_rank.index("Alta")]
        self.registro.cartaMediaRobo = potuacao_cartas[mao_rank.index("Media")]
        self.registro.cartaBaixaRobo = potuacao_cartas[mao_rank.index("Baixa")]
        self.registro.ganhadorPrimeiraRodada = 2
        self.registro.ganhadorSegundaRodada = 2
        self.registro.ganhadorTerceiraRodada = 2
        self.registro.qualidadeMaoBot = qualidade_mao_bot


    def segunda_rodada(self, primeira_carta_robo, primeira_carta_humano, ganhador_primeira_rodada):
        self.registro.ganhadorPrimeiraRodada = ganhador_primeira_rodada
        self.registro.primeiraCartaRobo = primeira_carta_robo.retornarNumero()
        self.registro.naipePrimeiraCartaRobo = primeira_carta_robo.retornarNaipe()
        self.registro.primeiraCartaHumano = primeira_carta_humano.retornarNumero()
        self.registro.naipePrimeiraCartaHumano = primeira_carta_humano.retornarNaipe()
    

    def terceira_rodada(self, segunda_carta_robo, segunda_carta_humano, ganhador_segunda_rodada):
        self.registro.ganhadorSegundaRodada = ganhador_segunda_rodada
        self.registro.segundaCartaRobo = segunda_carta_robo.retornarNumero()
        self.registro.naipeSegundaCartaRobo = segunda_carta_robo.retornarNaipe()
        self.registro.SegundaCartaHumano = segunda_carta_humano.retornarNumero()
        self.registro.naipeSegundaCartaHumano = segunda_carta_humano.retornarNaipe()


    def finalizar_rodadas(self, terceira_carta_robo, terceira_carta_humano, ganhador_terceira_rodada):
        self.registro.ganhadorTerceiraRodada = ganhador_terceira_rodada
        self.registro.terceiraCartaRobo = terceira_carta_robo.retornarNumero()
        self.registro.naipeTerceiraCartaRobo = terceira_carta_robo.retornarNaipe()
        self.registro.terceiraCartaHumano = terceira_carta_humano.retornarNumero()
        self.registro.naipeTerceiraCartaHumano = terceira_carta_humano.retornarNaipe()


    def envido(self, quem_envido, quem_real_envido, quem_falta_envido, quem_ganhou_envido):
        self.registro.quemEnvido = quem_envido
        self.registro.quemRealEnvido = quem_real_envido
        self.registro.quemFaltaEnvido = quem_falta_envido


    def truco(self, quem_truco, quem_retruco, quem_vale4, quem_negou_truco, quem_ganhou_truco):
        self.registro.quemTruco = quem_truco
        self.registro.quemRetruco = quem_retruco
        self.registro.quemValeQuatro = quem_vale4


    def flor(self, quem_flor, quem_contraflor, quem_contraflor_resto, pontos_flor_robo):
        self.registro.quemGanhouFlor = 2
        self.registro.quemFlor = quem_flor
        self.registro.quemContraFlor = quem_contraflor
        self.registro.quemContraFlorResto = quem_contraflor_resto
        self.registro.pontosFlorRobo = pontos_flor_robo
    

    def vencedor_envido(self, quem_ganhou_envido, quem_negou_envido):
        self.registro.quemGanhouEnvido = quem_ganhou_envido
        self.registro.quemNegouEnvido = quem_negou_envido


    def vencedor_truco(self, quem_ganhou_truco, quem_negou_truco):
        self.registro.quemNegouTruco = quem_negou_truco
        self.registro.quemGanhouTruco = quem_ganhou_truco


    def vencedor_flor(self, quem_ganhou_flor, quem_negou_flor):
        self.registro.quemGanhouFlor = quem_ganhou_flor
        self.registro.quemNegouFlor = quem_negou_flor


    def carregar_modelo_zerado(self):
        self.registro = pd.read_csv('../modelo_registro.csv', index_col='idMao')

    def retornar_registro(self):
        return self.registro
   
   
    def finalizar_jogo(self, df):
        if not(os.path.isfile('jogadas.csv')):
            df.to_csv('jogadas.csv', header=df.columns)
        else:
            df.to_csv('jogadas.csv', mode='a', header=False)

        # self.registro.to_csv('jogadas.csv')

    def resetar(self):
        self.casos = self.tratamento_inicial_df()
        self.registro = pd.read_csv('modelo_registro.csv', index_col='idMao')