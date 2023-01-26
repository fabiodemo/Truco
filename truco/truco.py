from bot import Bot

class Truco():
    
    def __init__(self):
        self.valor_aposta = 1
        self.jogador_bloqueado = 0
        self.jogador_pediu = 0
        self.jogador_aumentou2 = 0
        self.jogador_aumentou4 = 0
    
    def truco(self, aceitou, quemPediu, jogador1, jogador2):
        print("Truco")
        if(quemPediu == self.jogador_bloqueado):
            return None

        if(quemPediu == 'jogador1'):
            escolha = jogador2.avaliarTruco()
            self.jogador_bloqueado = 1

        else:
            escolha = -1
            while(escolha not in [0, 1, 2]):
                escolha = int(input(f"{jogador1}, você aceita o pedido (a mão passa a valer {(self.valor_aposta)+1} pontos)"))
            self.jogador_bloqueado = 2
        

        if escolha == 0:
            print(f"fugiu")
            if(quemPediu == jogador1):
                jogador1.pontos += 1

            else:
                jogador2.pontos += 1

            return False

        elif escolha == 1:
            print(f"{self.jogador2} aceitou o pedido.")
            self.valor_aposta += self.valor_aposta
            return True
                
        elif escolha == 2:
            print(f"{self.jogador2} pediu Retruco.")
            self.pedir_retruco(self.jogador2)


    def pedir_retruco(self, quemPediu, jogador1, jogador2):
        self.valor_aposta = 3
        print("Retruco")
        if(quemPediu == self.jogador_bloqueado):
            return None

        if(quemPediu == 'jogador1'):
            escolha = jogador2.avaliarTruco()
            self.jogador_bloqueado = 1

        else:
            escolha = -1
            while(escolha not in [0, 1, 2]):
                escolha = int(input(f"{jogador1}, você aceita o pedido (a mão passa a valer {(self.valor_aposta)+1} pontos)"))
            self.jogador_bloqueado = 2
        

        if escolha == 0:
            print(f"fugiu")
            if(quemPediu == jogador1):
                jogador1.pontos += 1

            else:
                jogador2.pontos += 1

            return False

        elif escolha == 1:
            print(f"{self.jogador2} aceitou o pedido.")
            self.valor_aposta += self.valor_aposta
            return True
                
        elif escolha == 2:
            print(f"{self.jogador2} pediu Retruco.")
            self.pedir_retruco(self.jogador2)

    def pediu_vale4(self, quemPediu, jogador1, jogador2):
        self.valor_aposta = 4
        print("Vale 4")
        if(quemPediu == self.jogador_bloqueado):
            return None

        if(quemPediu == 'jogador1'):
            escolha = jogador2.avaliarTruco()
            self.jogador_bloqueado = 1

        else:
            escolha = -1
            while(escolha not in [0, 1, 2]):
                escolha = int(input(f"{jogador1}, você aceita o pedido (a mão passa a valer {(self.valor_aposta)+1} pontos)"))
            self.jogador_bloqueado = 2
        

        if escolha == 0:
            print(f"fugiu")
            if(quemPediu == jogador1):
                jogador1.pontos += 1

            else:
                jogador2.pontos += 1

            return False

        elif escolha == 1:
            print(f"{self.jogador2} aceitou o pedido.")
            self.valor_aposta += self.valor_aposta
            return True


    def retornaTrucoPontos(self):
        return self.valor_aposta
    
    def resetarTrucoPontos(self):
        self.valor_aposta = 1
        self.jogador_bloqueado = 0
        self.jogador_pediu = 0
        self.jogador_aumentou2 = 0
        self.jogador_aumentou4 = 0