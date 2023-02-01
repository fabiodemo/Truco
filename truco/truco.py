from bot import Bot

class Truco():
    
    def __init__(self):
        self.valor_aposta = 1
        self.jogador_bloqueado = 0
        self.jogador_pediu = 0
        self.jogador_retruco = 0
        self.jogador_vale4 = 0
        self.estado_atual = ""
        self.jogador_fugiu = 0

    def reverter_jogador_bloqueado(self):
        if (self.jogador_bloqueado == 1):
            self.jogador_bloqueado = 2
        
        else:
            self.jogador_bloqueado = 1

    def redirecionar_pedir_truco(self, quemPediu, jogador1, jogador2):
        if(self.estado_atual == ""):
            estado = self.pedir_truco(quemPediu, jogador1, jogador2)
            self.estado_atual = "truco"
        elif(self.estado_atual == "truco"):
            estado = self.pedir_retruco(quemPediu, jogador1, jogador2)
            self.estado_atual = "truco"
        elif(self.estado_atual == "retruco"):
            estado = self.pedir_retruco(quemPediu, jogador1, jogador2)
            self.estado_atual = "vale4"
        return estado

    def pedir_truco(self, quemPediu, jogador1, jogador2):
        print("Truco")
        self.estado_atual = "truco"
        if(quemPediu == self.jogador_bloqueado):
            return None

        if(quemPediu == 1):
            escolha = jogador2.avaliarTruco()
            self.jogador_bloqueado = 1

        else:
            escolha = -1
            while(escolha not in [0, 1, 2]):
                escolha = int(input(f"{jogador1}, você aceita o pedido (a mão passa a valer {(self.valor_aposta)} pontos)"))
            self.jogador_bloqueado = 2
        

        if escolha == 0:
            print(f"fugiu")
            if(quemPediu == jogador1):
                jogador1.pontos += 1

            else:
                jogador2.pontos += 1

            return False

        elif escolha == 1:
            print(f"{jogador2} aceitou o pedido.")
            self.valor_aposta += self.valor_aposta
            return True
                
        elif escolha == 2:
            print(f"{jogador2} pediu Retruco.")
            self.reverter_jogador_bloqueado()
            return self.pedir_retruco(jogador2, jogador1, jogador2)


    def pedir_retruco(self, quemPediu, jogador1, jogador2):
        self.valor_aposta = 3
        self.estado_atual = "retruco"
        print("Retruco")
        if(quemPediu == self.jogador_bloqueado):
            return None

        if(quemPediu == 1):
            escolha = jogador2.avaliarTruco()
            self.jogador_bloqueado = 1

        else:
            escolha = -1
            while(escolha not in [0, 1, 2]):
                escolha = int(input(f"{jogador1}, você aceita o pedido (a mão passa a valer {(self.valor_aposta)} pontos)"))
            self.jogador_bloqueado = 2
        

        if escolha == 0:
            print(f"fugiu")
            if(quemPediu == jogador1):
                jogador1.pontos += 2

            else:
                jogador2.pontos += 2

            return False

        elif escolha == 1:
            print(f"{jogador2} aceitou o pedido.")
            self.valor_aposta += self.valor_aposta
            return True
                
        elif escolha == 2:
            print(f"{jogador2} pediu Retruco.")
            self.reverter_jogador_bloqueado()
            return self.pedir_vale4(jogador1, jogador1, jogador2)

    def pedir_vale4(self, quemPediu, jogador1, jogador2):
        self.valor_aposta = 4
        self.estado_atual = "vale4"
        print("Vale 4")
        if(quemPediu == self.jogador_bloqueado):
            return None

        if(quemPediu == 1):
            escolha = jogador2.avaliarTruco()
            self.jogador_bloqueado = 1

        else:
            escolha = -1
            while(escolha not in [0, 1]):
                escolha = int(input(f"{jogador1}, você aceita o pedido (a mão passa a valer {(self.valor_aposta)} pontos)"))
            self.jogador_bloqueado = 2
        

        if escolha == 0:
            print(f"fugiu")
            if(quemPediu == jogador1):
                jogador1.pontos += 3

            else:
                jogador2.pontos += 3

            return False

        elif escolha == 1:
            print(f"{jogador2} aceitou o pedido.")
            self.valor_aposta += self.valor_aposta
            return True


    def retornar_valor_aposta(self):
        return self.valor_aposta

    def retornar_quem_fugiu(self):
        return self.retornar_quem_fugiu
    
    def resetar_pontos_truco(self):
        self.valor_aposta = 1
        self.jogador_bloqueado = 0
        self.jogador_pediu = 0
        self.jogador_aumentou2 = 0
        self.jogador_aumentou4 = 0
        self.jogador_fugiu = 0