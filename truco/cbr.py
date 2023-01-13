import pandas as pd
from pontos import MANILHA, CARTAS_VALORES

class Cbr():

    def __init__(self):
        self.indice = 0
        self.casos = pd.read_csv(r'../dbtrucoimitacao_maos.csv', index_col='idMao').fillna(0)

    def codificarNaipe(self, naipe):
        if (x == 'ESPADAS'):
            return 1
        
        if (x == 'OUROS'):
            return 2
        
        if (x == 'BASTOS'):
            return 3
        
        if (x == 'COPAS'):
            return 4

    def atualizarDataframe(self, rodada):
        if (rodada == 1):
            colunas_string = [
                'naipeCartaAltaRobo', 
                'naipeCartaMediaRobo',
                'naipeCartaBaixaRobo', 
                'cartaBaixaRobo', 
                'cartaMediaRobo', 
                'cartaAltaRobo', 
                'naipePrimeiraCartaHumano', 
                'primeiraCartaHumano',
                'ganhadorPrimeiraRodada', 
                'ganhadorSegundaRodada', 
            ]

        elif (rodada == 2):
            colunas_string = [
                'naipeCartaAltaRobo', 
                'naipeCartaMediaRobo',
                'naipeCartaBaixaRobo', 
                'cartaBaixaRobo', 
                'cartaMediaRobo', 
                'cartaAltaRobo', 
                'primeiraCartaRobo',
                'naipePrimeiraCartaRobo',
                'naipePrimeiraCartaHumano', 
                'naipeSegundaCartaHumano',
                'primeiraCartaHumano',
                'segundaCartaHumano', 
                'ganhadorPrimeiraRodada', 
                'ganhadorSegundaRodada', 
            ]
            
        else:
            colunas_string = [
                'naipeCartaAltaRobo', 
                'naipeCartaMediaRobo',
                'naipeCartaBaixaRobo', 
                'cartaBaixaRobo', 
                'cartaMediaRobo', 
                'cartaAltaRobo', 
                'primeiraCartaRobo', 
                'naipePrimeiraCartaRobo',
                'segundaCartaRobo', 
                'naipeSegundaCartaRobo',
                'terceiraCartaRobo', 
                'naipePrimeiraCartaHumano', 'naipeSegundaCartaHumano','naipeTerceiraCartaHumano', 
                'primeiraCartaHumano',
                'segundaCartaHumano', 
                'terceiraCartaHumano',
                'ganhadorPrimeiraRodada', 
                'ganhadorSegundaRodada', 
                'ganhadorTerceiraRodada'
            ]

        df = self.casos
        print(df)
        colunas_int = [col for col in df.columns if col not in colunas_string]
        df[colunas_int] = df[colunas_int].astype('int')
        df.replace('ESPADAS', '1', inplace=True)
        df.replace('OURO', '2', inplace=True)
        df.replace('BASTOS', '3', inplace=True)
        df.replace('COPAS', '4', inplace=True)
        df[colunas_string] = df[colunas_string].astype('int')
        df = df[(df >= 0).all(axis=1)]
        
        return df

    def rodada1(self):
        df = self.atualizarDataframe(1)
        print('vai')
        pass
    
    def rodada2(self):
        df = self.atualizarDataframe(2)
        print('rodada2')
        return self.casos
    
    def rodada3(self):
        df = self.atualizarDataframe(3)
        return self.casos

    def zerarIndice(self):
        self.indice = 0