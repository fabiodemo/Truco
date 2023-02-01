import pandas as pd
import os

class Dados():

    def __init__(self):
        self.registro_modelo = self.tratamento_inicial_df()
        self.dados = pd.read_csv('../dbtrucoimitacao_maos.csv', index_col='idMao').fillna(0)

    def tratamento_inicial_df(self):
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
        return df

    def primeira_rodada(self, potuacao_cartas, mao_rank, qualidade_mao_bot):
        
        self.registro_modelo.jogadorMao = 1
        self.registro_modelo.cartaAltaRobo = potuacao_cartas[mao_rank.index("Alta")]
        self.registro_modelo.cartaMediaRobo = potuacao_cartas[mao_rank.index("Media")]
        self.registro_modelo.cartaBaixaRobo = potuacao_cartas[mao_rank.index("Baixa")]
        self.registro_modelo.ganhadorPrimeiraRodada = 2
        self.registro_modelo.ganhadorSegundaRodada = 2
        self.registro_modelo.ganhadorTerceiraRodada = 2
        self.registro_modelo.qualidadeMaoBot = qualidade_mao_bot

        return self.registro_modelo

    def segunda_rodada(self, primeira_carta_robo, primeira_carta_humano, ganhador_primeira_rodada):
        self.registro.ganhadorPrimeiraRodada = ganhador_primeira_rodada
        self.registro_modelo.primeiraCartaRobo = primeira_carta_robo.retornarNumero()
        self.registro_modelo.naipePrimeiraCartaRobo = primeira_carta_robo.retornarNaipe()
        self.registro_modelo.primeiraCartaHumano = primeira_carta_humano.retornarNumero()
        self.registro_modelo.naipePrimeiraCartaHumano = primeira_carta_humano.retornarNaipe()
    
    def terceira_rodada(self, segunda_carta_robo, segunda_carta_humano, ganhador_segunda_rodada):
        self.registro.ganhadorSegundaRodada = ganhador_segunda_rodada
        self.registro_modelo.segundaCartaRobo = segunda_carta_robo.retornarNumero()
        self.registro_modelo.naipeSegundaCartaRobo = segunda_carta_robo.retornarNaipe()
        self.registro_modelo.SegundaCartaHumano = segunda_carta_humano.retornarNumero()
        self.registro_modelo.naipeSegundaCartaHumano = segunda_carta_humano.retornarNaipe()

    def finalizar_rodadas(self, terceira_carta_robo, terceira_carta_humano, ganhador_terceira_rodada):
        self.registro.ganhadorTerceiraRodada = ganhador_terceira_rodada
        self.registro_modelo.terceiraCartaRobo = terceira_carta_robo.retornarNumero()
        self.registro_modelo.naipeTerceiraCartaRobo = terceira_carta_robo.retornarNaipe()
        self.registro_modelo.terceiraCartaHumano = terceira_carta_humano.retornarNumero()
        self.registro_modelo.naipeTerceiraCartaHumano = terceira_carta_humano.retornarNaipe()

    def finalizar_jogo(self, df):
        if not(os.path.isfile('jogadas.csv')):
            df.to_csv('jogadas.csv', header=df.columns)
        else:
            df.to_csv('jogadas.csv', mode='a', header=False)

        # self.registro_modelo.to_csv('jogadas.csv')

    def subset_envido(self, quem_envido, quem_real_envido, quem_falta_envido, quem_ganhou_envido):
        self.registro_modelo.quemEnvido = quem_envido
        self.registro_modelo.quemRealEnvido = quem_real_envido
        self.registro_modelo.quemFaltaEnvido = quem_falta_envido
        
    def subset_truco(self, quem_truco, quem_retruco, quem_vale4, quem_negou_truco, quem_ganhou_truco):
        self.registro_modelo.quemTruco = quem_truco
        self.registro_modelo.quemRetruco = quem_retruco
        self.registro_modelo.quemValeQuatro = quem_vale4

    def subset_flor(self, quem_flor, quem_contraflor, quem_contraflor_resto, pontos_flor_robo):
        self.registro_modelo.quemGanhouFlor = 2
        self.registro_modelo.quemFlor = quem_flor
        self.registro_modelo.quemContraFlor = quem_contraflor
        self.registro_modelo.quemContraFlorResto = quem_contraflor_resto
        self.registro_modelo.pontosFlorRobo = pontos_flor_robo
    
    def vencedor_envido(self, quem_ganhou_envido, quem_negou_envido):
        self.registro_modelo.quemGanhouEnvido = quem_ganhou_envido
        self.registro_modelo.quemNegouEnvido = quem_negou_envido

    def vencedor_truco(self, quem_ganhou_truco, quem_negou_truco):
        self.registro_modelo.quemNegouTruco = quem_negou_truco
        self.registro_modelo.quemGanhouTruco = quem_ganhou_truco

    def vencedor_flor(self, quem_ganhou_flor, quem_negou_flor):
        self.registro_modelo.quemGanhouFlor = quem_ganhou_flor
        self.registro_modelo.quemNegouFlor = quem_negou_flor


    def carregar_modelo_zerado(self):
        self.registro_modelo = pd.read_csv('../modelo_registro.csv', index_col='idMao')
        return self.registro_modelo