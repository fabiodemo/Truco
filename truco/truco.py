class Truco():
    def __init__(self):
        self.valor_aposta = 1
        self.jogador_bloqueado = 0
        self.jogador_pediu = 0
        self.jogador_retruco = 0
        self.jogador_vale_quatro = 0
        self.jogador_fugiu = 0
        self.estado_atual = ""


    def reverter_jogador_bloqueado(self):
        """Lógica para impedir que o mesmo jogador não peça o aumento de aposta seguidamente."""
        if (self.jogador_bloqueado == 1):
            self.jogador_bloqueado = 2
        
        else:
            self.jogador_bloqueado = 1


    def inicializar_jogador_bloqueado(self, quem_pediu):
        """Inicialização do jogador que foi bloqueado e não pode pedir aumento da aposta do jogo."""
        self.jogador_bloqueado = quem_pediu


    def controlar_truco(self, quem_pediu, jogador1, jogador2):
        """Controlador de métodos, para selecionar o que pode ser chamado ou não."""
        print(self.jogador_bloqueado, self.estado_atual)
        if (quem_pediu == self.jogador_bloqueado):
            return None
        else:
            self.inicializar_jogador_bloqueado(quem_pediu)

        if (self.estado_atual == ""):
            estado = self.pedir_truco(quem_pediu, jogador1, jogador2)
            self.estado_atual = "truco"
        elif (self.estado_atual == "truco"):
            estado = self.pedir_retruco(quem_pediu, jogador1, jogador2)
            self.estado_atual = "truco"
        elif (self.estado_atual == "retruco"):
            estado = self.pedir_retruco(quem_pediu, jogador1, jogador2)
            self.estado_atual = "vale_quatro"
        elif (self.estado_atual == "vale_quatro"):
            return None

        return estado


    def pedir_truco(self, quem_pediu, jogador1, jogador2):
        """Aumenta a aposta inicial do jogo, que passa a valer 2 pontos."""
        print("Truco")
        self.estado_atual = "truco"

        if (quem_pediu == 1):
            escolha = jogador2.avaliar_truco()
            self.jogador_bloqueado = 1

        else:
            escolha = -1
            while(escolha not in [0, 1, 2]):
                escolha = int(input(f"{quem_pediu}, você aceita o pedido (a mão passa a valer {(self.valor_aposta)} pontos)"))
            self.jogador_bloqueado = 2
        

        if escolha == 0:
            if (quem_pediu == 1):
                jogador1.pontos += 1

            else:
                jogador2.pontos += 1

            return False

        elif escolha == 1:
            print(f"Jogador {quem_pediu} aceitou o pedido.")
            # self.valor_aposta += self.valor_aposta
            return True
                
        elif escolha == 2:
            print(f"Jogador {quem_pediu} pediu Truco.")
            self.reverter_jogador_bloqueado()
            return self.pedir_retruco(self.jogador_bloqueado, jogador1, jogador2)


    def pedir_retruco(self, quem_pediu, jogador1, jogador2):
        """Aumenta a aposta, que passa a valer 3 pontos."""
        self.valor_aposta = 3
        self.estado_atual = "retruco"
        print("Retruco")

        if (quem_pediu == 1):
            escolha = jogador2.avaliar_retruco()
            self.jogador_bloqueado = 1

        else:
            escolha = -1
            while(escolha not in [0, 1, 2]):
                escolha = int(input(f"Jogador {quem_pediu}, você aceita o pedido (a mão passa a valer {(self.valor_aposta)} pontos)"))
            self.jogador_bloqueado = 2
        

        if escolha == 0:
            if (quem_pediu == 1):
                jogador1.pontos += 2

            else:
                jogador2.pontos += 2

            return False

        elif escolha == 1:
            print(f"Jogador {quem_pediu} aceitou o pedido.")
            # self.valor_aposta += self.valor_aposta
            return True
                
        elif escolha == 2:
            print(f"Jogador {quem_pediu} pediu Retruco.")
            self.reverter_jogador_bloqueado()
            return self.pedir_vale_quatro(self.jogador_bloqueado, jogador1, jogador2)


    def pedir_vale_quatro(self, quem_pediu, jogador1, jogador2):
        """Aumenta a aposta, que passa a valer 4 pontos"""
        self.valor_aposta = 4
        print("Vale 4")

        if (quem_pediu == 1):
            escolha = jogador2.avaliar_vale_quatro()
            self.jogador_bloqueado = 1

        else:
            escolha = -1
            while(escolha not in [0, 1]):
                escolha = int(input(f"Jogador {quem_pediu}, você aceita o pedido (a mão passa a valer {(self.valor_aposta)} pontos)"))
            self.jogador_bloqueado = 2
        

        if escolha == 0:
            if (quem_pediu == 1):
                jogador1.pontos += 3

            else:
                jogador2.pontos += 3

            return False

        elif escolha == 1:
            print(f"Jogador {quem_pediu} aceitou o pedido.")
            # self.valor_aposta += self.valor_aposta
            return True


    def retornar_valor_aposta(self):
        """Retorna o valor atual de pontos (normal, truco, retruco, vale quatro)."""
        return self.valor_aposta


    def retornar_quem_fugiu(self):
        """Retorna o jogador que fugiu do truco."""
        return self.retornar_quem_fugiu
    
    
    def resetar_pontos_truco(self):
        """Reset dos pontos da classe truco."""
        self.valor_aposta = 1
        self.jogador_bloqueado = 0
        self.jogador_pediu = 0
        self.jogador_aumentou2 = 0
        self.jogador_aumentou4 = 0
        self.jogador_fugiu = 0
        self.estado_atual = ""
