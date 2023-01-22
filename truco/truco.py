
class Truco():
    
    def __init__(self):
        self.pontos_truco = 1
        self.jogador_pediu = 0
    
    def trucoAceito(self, aceitou):
        print("Truco")
        if(aceitou is False and self.pontos_truco == 1):
            self.pontos_truco = 1
            
        elif(aceitou is False and self.pontos_truco != 1):
            self.pontos_truco -= 1

        elif(self.pontos_truco == 1):
            self.pontos_truco += 1
        
        else:
            self.pontos_truco +=2
    
    def retornaTrucoPontos(self):
        return self.pontos_truco
    
    def resetarTrucoPontos(self):
        self.pontos_truco = 1