
class Truco():
    
    def __init__(self):
        self.pontos_truco = 1
        self.jogador_bloqueado = 0
        self.jogador_pediu = 0
        self.jogador_aumentou2 = 0
        self.jogador_aumentou4 = 0
    
    def truco(self, aceitou, quemPediu):
        print("Truco")
        if(quemPediu == self.jogador_bloqueado):
            return
        if(self.pontos_truco == 1):
            self.pediuTruco()
            
        elif(aceitou is False and self.pontos_truco != 1):
            self.trucoRejeitou()

        else:
            self.trucoAumentou()
        
    def trucoRejeitou(self, aceitou):
        print("Rejeitou Truco")
        self.pontos_truco += 1

    def pediuTruco(self, aceitou):
        self.pontos_truco += 1     

    def trucoAumentou(self, aceitou):
        self.pontos_truco +=2

    def retornaTrucoPontos(self):
        return self.pontos_truco
    
    def resetarTrucoPontos(self):
        self.pontos_truco = 1